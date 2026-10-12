import base64,json,os,sys,urllib.request
tok=os.environ["GH_TOKEN"];repo=os.environ['GH_REPO']
def up(local,remote,msg):
    url=f"https://api.github.com/repos/{repo}/contents/{remote}"
    h={"Authorization":f"Bearer {tok}","Accept":"application/vnd.github+json","Content-Type":"application/json"}
    sha=None
    try:
        r=urllib.request.urlopen(urllib.request.Request(url,headers=h));sha=json.load(r)['sha']
    except Exception: pass
    body={"message":msg,"content":base64.b64encode(open(local,'rb').read()).decode()}
    if sha: body["sha"]=sha
    r=urllib.request.urlopen(urllib.request.Request(url,data=json.dumps(body).encode(),headers=h,method="PUT"))
    d=json.load(r);return f"https://raw.githubusercontent.com/{repo}/main/{remote}"
if __name__=="__main__":
    for a in sys.argv[1:]:
        l,rm=a.split("=>");print(up(l,rm,"upload "+rm))
