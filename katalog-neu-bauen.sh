#!/usr/bin/env bash
# Erzeugt .claude-plugin/marketplace.json neu aus dem aktuellen Stand des Original-Repos.
# Aufruf: bash katalog-neu-bauen.sh
set -euo pipefail
cd "$(dirname "$0")"
RAW="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/.claude-plugin/marketplace.json"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "==> Hole Original-Katalog"
curl -fsSL "$RAW" -o "$TMP/upstream.json"

python3 - "$TMP/upstream.json" <<'PY'
import json, sys, os
src=json.load(open(sys.argv[1], encoding='utf-8'))
UP="https://github.com/Klotzkette/claude-fuer-deutsches-recht.git"
out={"$schema":src.get("$schema"),"name":"deutsches-recht-proxy",
 "description":"Proxy-Marketplace: verweist per git-subdir auf die Plugins in Klotzkette/claude-fuer-deutsches-recht. Umgeht die Groessenbegrenzung, da nur der jeweils benoetigte Unterordner geklont wird.",
 "owner":src.get("owner"),"version":"1.0.0","plugins":[]}
skip=[]
for p in src["plugins"]:
    s=p.get("source")
    if not isinstance(s,str) or not s.startswith("./"): skip.append(p.get("name")); continue
    e={k:p[k] for k in ("name","description","version","author") if k in p}
    e["source"]={"source":"git-subdir","url":UP,"path":s[2:],"ref":"main"}
    out["plugins"].append(e)
os.makedirs(".claude-plugin", exist_ok=True)
json.dump(out, open(".claude-plugin/marketplace.json","w",encoding='utf-8'), ensure_ascii=False, indent=2)
print(f"==> {len(out['plugins'])} Plugins im Katalog" + (f", uebersprungen: {skip}" if skip else ""))
PY

echo "==> Fertig. Jetzt committen und pushen:"
echo "    git add -A && git commit -m 'Katalog aktualisiert' && git push"
