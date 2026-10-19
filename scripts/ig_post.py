import json, os, urllib.request
TOKEN=os.environ["APIFY_TOKEN"].strip(); URL=os.environ["POST_URL"]; OUT=os.environ.get("OUT","assets/research/post")
req=urllib.request.Request(f"https://api.apify.com/v2/acts/apify~instagram-scraper/run-sync-get-dataset-items?token={TOKEN}&timeout=200",
    data=json.dumps({"directUrls":[URL],"resultsType":"posts","resultsLimit":1,"addParentData":True}).encode(),headers={"Content-Type":"application/json"})
items=json.load(urllib.request.urlopen(req,timeout=240))
os.makedirs(os.path.dirname(OUT) or ".",exist_ok=True)
json.dump(items,open(OUT+".json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
v=(items[0].get("videoUrl") if items else None)
if v:
    urllib.request.urlretrieve(v, OUT+".mp4"); print("video", os.path.getsize(OUT+".mp4"))
print("items", len(items))
