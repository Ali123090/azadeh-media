#!/bin/bash
set -e
ID="$DRIVE_ID"; NAME="$NAME"
mkdir -p work assets/private
curl -sL -o work/in.bin "https://drive.usercontent.google.com/download?id=${ID}&export=download&confirm=t"
SIZE=$(stat -c%s work/in.bin); echo "downloaded $SIZE bytes"
HEAD=$(head -c 200 work/in.bin | tr -d "\0" | tr "\n" " " | cut -c1-150)
if [ "$SIZE" -lt 100000 ] || echo "$HEAD" | grep -qi "<html\|<!doctype"; then echo "DOWNLOAD_FAILED (file not shared publicly?)"; head -c 300 work/in.bin; python3 -c "import json,sys;print(json.dumps({'error':'download failed','size':$SIZE,'head':sys.argv[1]}))" "$HEAD" > assets/private/$NAME.status.json; exit 0; fi
sudo apt-get -qq update >/dev/null && sudo apt-get -qq install -y ffmpeg >/dev/null
ffprobe -v error -show_entries format=duration:stream=width,height,codec_type,r_frame_rate -of json work/in.bin > work/probe.json
pip -q install faster-whisper==1.0.3 >/dev/null
python3 - <<'PY'
from faster_whisper import WhisperModel
import json
m=WhisperModel("medium", device="cpu", compute_type="int8")
segs,info=m.transcribe("work/in.bin", language="fa", word_timestamps=True, vad_filter=True)
out=[]
for s in segs:
    out.append({"start":s.start,"end":s.end,"text":s.text,"words":[{"w":w.word,"s":w.start,"e":w.end} for w in (s.words or [])]})
json.dump({"segments":out},open("work/transcript.json","w"),ensure_ascii=False)
print("segments",len(out))
PY
echo "$PUBKEY" | base64 -d > work/pub.pem
openssl rand -hex 32 > work/key.txt
tar -C work -cf work/bundle.tar in.bin transcript.json probe.json
openssl enc -aes-256-cbc -pbkdf2 -salt -in work/bundle.tar -out assets/private/$NAME.enc -pass file:work/key.txt
openssl pkeyutl -encrypt -pubin -inkey work/pub.pem -in work/key.txt -out assets/private/$NAME.key.enc
echo "{\"ok\":true,\"size\":$SIZE}" > assets/private/$NAME.status.json
ls -la assets/private
