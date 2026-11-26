# One-off: download pages whose Runway task IDs appear in a list_recent dump.
import json, re, subprocess, sys, os, csv
urls = {}
for f in sys.argv[1:]:
    for a in json.load(open(f))["assets"]:
        m = re.search(r"/images/([0-9a-f-]{36})/", a.get("url", ""))
        if m: urls[m.group(1)] = a["url"]
for book in ["hockey", "soccer", "baseball"]:
    d = f"{book}-teddy-bears-vol1/pages"
    for row in csv.DictReader(open(f"{d}/tasks.tsv"), delimiter="\t"):
        out = f"{d}/p{row['page']}.png"
        if os.path.exists(out) or row["task_id"] not in urls: continue
        subprocess.run(["curl", "-sS", "--retry", "3", "-o", out, urls[row["task_id"]]], check=True)
        print("got", out)
