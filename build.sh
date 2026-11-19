#!/bin/sh
# Rebuild entry.png from build.py with the local Chromium.
# No network and no external assets: index.html is generated here and rendered
# from a file:// URL at exactly 1024x1024.
set -eu
cd "$(dirname "$0")"

python3 build.py

chromium --headless --disable-gpu --no-sandbox --hide-scrollbars \
         --disable-background-networking --disable-component-update \
         --disable-sync --no-first-run --disable-extensions \
         --force-device-scale-factor=1 --window-size=1024,1024 \
         --virtual-time-budget=3000 --screenshot=entry.png index.html 2>/dev/null

python3 - <<'PY'
from PIL import Image
im = Image.open("entry.png")
im.load()
assert im.size == (1024, 1024), im.size
print("entry.png", im.size, im.mode)
PY
