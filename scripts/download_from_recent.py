# One-off: download pages whose Runway task IDs appear in a list_recent dump.
import json, re, subprocess, sys, os, csv
urls = {}
for f in sys.argv[1:]:
    for a in json.load(open(f))["assets"]:
        m = re.search(r"/images/([0-9a-f-]{36})/", a.get("url", ""))
        if m: urls[m.group(1)] = a["url"]
for book in ["hockey", "soccer", "baseball"]:
    d = f"{book}-teddy-bears-vol1/pages"
    last = {}
    for row in csv.DictReader(open(f"{d}/tasks.tsv"), delimiter="\t"):
        last[row["page"]] = row["task_id"]   # later rows (QC fixes) win
    for page, tid in last.items():
        out = f"{d}/p{page}.png"
        if tid not in urls: continue
        if os.path.exists(out) and not os.path.exists(out + ".stale"): continue
        subprocess.run(["curl", "-sS", "--retry", "3", "-o", out, urls[tid]], check=True)
        if os.path.exists(out + ".stale"): os.remove(out + ".stale")
        print("got", out)
