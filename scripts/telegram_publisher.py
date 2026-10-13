"""Telegram auto-publisher (runs on GitHub Actions).
Reads queue/telegram/*.json and publishes due items to the channel.
State is kept in queue/telegram/_state.json and committed back by the workflow."""
import json, os, sys, glob, datetime as dt, urllib.request, urllib.parse, uuid, mimetypes

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
CHAT = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
QDIR = "queue/telegram"
STATE = os.path.join(QDIR, "_state.json")
TEHRAN = dt.timezone(dt.timedelta(hours=3, minutes=30))
MAX_FAILS = 5

def api(method, fields, file_field=None, file_path=None):
    url = f"https://api.telegram.org/bot{TOKEN}/{method}"
    if file_path:
        b = uuid.uuid4().hex
        body = bytearray()
        for k, v in fields.items():
            body += f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
        ctype = mimetypes.guess_type(file_path)[0] or "application/octet-stream"
        body += f'--{b}\r\nContent-Disposition: form-data; name="{file_field}"; filename="{os.path.basename(file_path)}"\r\nContent-Type: {ctype}\r\n\r\n'.encode()
        body += open(file_path, "rb").read() + f"\r\n--{b}--\r\n".encode()
        req = urllib.request.Request(url, data=bytes(body), headers={"Content-Type": f"multipart/form-data; boundary={b}"})
    else:
        req = urllib.request.Request(url, data=urllib.parse.urlencode(fields).encode())
    try:
        r = json.load(urllib.request.urlopen(req, timeout=120))
    except urllib.error.HTTPError as e:
        r = json.load(e)
    if not r.get("ok"):
        raise RuntimeError(f"Telegram error: {r.get('description')}")
    return r.get("result")

def load_state():
    try: return json.load(open(STATE, encoding="utf-8"))
    except Exception: return {"posted": {}, "fails": {}}

def save_state(s):
    json.dump(s, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

def parse_time(t):
    x = dt.datetime.fromisoformat(t)
    return x if x.tzinfo else x.replace(tzinfo=TEHRAN)

def send(item, state):
    kind = item.get("type", "text")
    cap = item.get("caption") or item.get("text") or ""
    if kind == "text":
        return api("sendMessage", {"chat_id": CHAT, "text": cap})
    if kind in ("delete", "caption"):
        t = item.get("target")
        mid = (state["posted"].get(t) or {}).get("message_id")
        if not mid: raise RuntimeError(f"No message_id for target {t}")
        if kind == "delete":
            api("deleteMessage", {"chat_id": CHAT, "message_id": mid}); return {}
        return api("editMessageCaption", {"chat_id": CHAT, "message_id": mid, "caption": cap})
    m = {"photo": "sendPhoto", "video": "sendVideo", "document": "sendDocument"}
    if kind not in m: raise RuntimeError(f"Unknown type {kind}")
    path = item.get("media")
    if not path or not os.path.exists(path): raise RuntimeError(f"Media not found: {path}")
    f = {"chat_id": CHAT}
    if cap: f["caption"] = cap
    return api(m[kind], f, kind, path)

def run():
    state = load_state(); now = dt.datetime.now(dt.timezone.utc); changed = False
    for p in sorted(glob.glob(os.path.join(QDIR, "*.json"))):
        name = os.path.basename(p)
        if name.startswith("_") or name in state["posted"]: continue
        try: item = json.load(open(p, encoding="utf-8"))
        except Exception as e: print(f"{name}: unreadable: {e}"); continue
        if item.get("enabled") is False: continue
        try: when = parse_time(item["publish_at"])
        except Exception: print(f"{name}: invalid publish_at"); continue
        if when > now: continue
        if (now - when).total_seconds() > 6*3600 and not item.get("allow_late"):
            state["posted"][name] = {"status": "skipped_late", "at": now.isoformat()}; changed = True
            print(f"{name}: skipped (more than 6h late)"); continue
        try:
            res = send(item, state) or {}
            state["posted"][name] = {"status": "sent", "at": now.isoformat(), "message_id": res.get("message_id")}
            state["fails"].pop(name, None); print(f"{name}: published OK")
        except Exception as e:
            n = state["fails"].get(name, 0) + 1; state["fails"][name] = n
            print(f"{name}: failed ({n}/{MAX_FAILS}): {e}")
            if n >= MAX_FAILS: state["posted"][name] = {"status": "failed", "at": now.isoformat()}
        changed = True
    if changed: save_state(state)

if __name__ == "__main__":
    if not TOKEN or not CHAT:
        print("TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID secrets are missing."); sys.exit(1)
    mode = sys.argv[1] if len(sys.argv) > 1 else "run"
    if mode == "test":
        me = api("getMe", {}); print(f"Bot OK: @{me.get('username')}")
        ch = api("getChat", {"chat_id": CHAT}); print(f"Channel OK: {ch.get('title')}")
        r = api("sendMessage", {"chat_id": CHAT, "text": "پیام آزمایشی انتشار خودکار ✓"}); print(f"Test message sent: {r.get('message_id')}")
    else:
        run()
