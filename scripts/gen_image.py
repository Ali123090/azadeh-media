import json, os, sys, base64, urllib.request, urllib.error, datetime
KEY = os.environ.get("GEMINI_API_KEY", "").strip()
JOBS = json.loads(os.environ.get("JOBS", "[]"))
BASE = "https://generativelanguage.googleapis.com/v1beta"
LOG = "assets/gen-log.txt"
lines = [f"=== run {datetime.datetime.utcnow().isoformat()}Z ==="]
def log(s): print(s); lines.append(s)
def call(url, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 headers={"Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req, timeout=180)), None
    except urllib.error.HTTPError as e:
        try: msg = json.load(e).get("error", {}).get("message", "")
        except Exception: msg = str(e)
        return None, f"HTTP {e.code}: {msg[:300]}"
if not KEY:
    log("GEMINI_API_KEY secret is missing")
else:
    models, err = call(f"{BASE}/models?key={KEY}&pageSize=200")
    names = [m["name"] for m in (models or {}).get("models", []) if "image" in m["name"].lower() and "generateContent" in m.get("supportedGenerationMethods", [])]
    log("image models: " + ", ".join(names) if names else f"no image models found ({err})")
    pref = sorted(names, key=lambda n: (0 if "flash" in n else 1, n))
    for prompt, path, aspect in JOBS:
        done = False
        for m in pref:
            body = {"contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {"responseModalities": ["IMAGE", "TEXT"], "imageConfig": {"aspectRatio": aspect}}}
            res, err = call(f"{BASE}/{m}:generateContent?key={KEY}", body)
            if err and "imageConfig" in err:
                body["generationConfig"].pop("imageConfig"); res, err = call(f"{BASE}/{m}:generateContent?key={KEY}", body)
            if err: log(f"{path}: {m} -> {err}"); continue
            parts = [p for c in res.get("candidates", []) for p in c.get("content", {}).get("parts", [])]
            img = next((p for p in parts if "inlineData" in p or "inline_data" in p), None)
            if not img: log(f"{path}: {m} -> no image in response"); continue
            d = img.get("inlineData") or img.get("inline_data")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "wb").write(base64.b64decode(d["data"]))
            log(f"{path}: OK via {m} ({os.path.getsize(path)} bytes)"); done = True; break
        if not done: log(f"{path}: FAILED")
os.makedirs("assets", exist_ok=True)
old = open(LOG, encoding="utf-8").read() if os.path.exists(LOG) else ""
open(LOG, "w", encoding="utf-8").write(old + "\n".join(lines) + "\n")
