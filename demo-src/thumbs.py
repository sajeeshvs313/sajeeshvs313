"""Render a screenshot thumbnail for every demo (needs Chromium + Pillow)."""
import os, subprocess, sys, tempfile
from PIL import Image
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "demo"))
OUT = os.path.join(ROOT, "assets", "thumbs"); os.makedirs(OUT, exist_ok=True)
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
slugs = [d for d in sorted(os.listdir(ROOT)) if os.path.exists(os.path.join(ROOT, d, "index.html"))]
for s in slugs:
    tmp = tempfile.mktemp(suffix=".png")
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--window-size=1280,840",
                    "--virtual-time-budget=12000", f"--screenshot={tmp}", f"file://{ROOT}/{s}/index.html"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    im = Image.open(tmp).convert("RGB").crop((0, 37, 1280, 837)).resize((960, 600), Image.LANCZOS)
    im.save(os.path.join(OUT, s + ".jpg"), "JPEG", quality=80, optimize=True, progressive=True)
    os.remove(tmp)
print("thumbs:", len(slugs))
