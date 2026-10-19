"""Pull public Instagram reels via Apify and rank them by views. Runs on GitHub Actions."""
import json, os, urllib.request, urllib.error, datetime
TOKEN = os.environ.get("APIFY_TOKEN", "").strip()
CFG = json.loads(os.environ.get("CFG", "{}"))
OUT = CFG.get("out", "assets/research/reels.json")
def run(actor, payload):
    url = f"https://api.apify.com/v2/acts/{actor}/run-sync-get-dataset-items?token={TOKEN}&timeout=280"
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    try: return json.load(urllib.request.urlopen(req, timeout=300)), None
    except urllib.error.HTTPError as e: return [], f"HTTP {e.code}: {e.read()[:300]}"
    except Exception as e: return [], str(e)
items, log = [], []
if not TOKEN: log.append("APIFY_TOKEN missing")
else:
    if CFG.get("usernames"):
        r, err = run("apify~instagram-reel-scraper", {"username": CFG["usernames"], "resultsLimit": CFG.get("per_user", 30)})
        log.append(f"profiles: {len(r)} items {err or ''}"); items += r
    if CFG.get("hashtags"):
        r, err = run("apify~instagram-hashtag-scraper", {"hashtags": CFG["hashtags"], "resultsType": "reels", "resultsLimit": CFG.get("per_tag", 40)})
        log.append(f"hashtags: {len(r)} items {err or ''}"); items += r
rows, seen = [], set()
for it in items:
    url = it.get("url") or it.get("shortCode")
    if not url or url in seen: continue
    seen.add(url)
    rows.append({"owner": it.get("ownerUsername"), "url": url, "date": it.get("timestamp"),
                 "views": it.get("videoPlayCount") or it.get("videoViewCount") or 0,
                 "likes": it.get("likesCount"), "comments": it.get("commentsCount"),
                 "duration": it.get("videoDuration"), "caption": (it.get("caption") or "")[:700]})
rows.sort(key=lambda r: r["views"] or 0, reverse=True)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump({"generated": datetime.datetime.utcnow().isoformat() + "Z", "log": log, "count": len(rows), "reels": rows},
          open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("\n".join(log), len(rows))
