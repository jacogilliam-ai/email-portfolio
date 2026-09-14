#!/usr/bin/env python3
"""Stamp every local asset reference with a short content hash.

Filenames stay stable (hero.jpg is still hero.jpg for anyone editing the Figma),
but the URL changes the moment the bytes change, so browsers and the Pages CDN
cannot serve a stale image. Re-run after replacing any asset.
"""
import hashlib, pathlib, re

here = pathlib.Path(__file__).parent
def h(name):
    p = here / name
    return hashlib.sha1(p.read_bytes()).hexdigest()[:8] if p.exists() else None

assets = [f.name for f in here.iterdir() if f.suffix.lower() in (".jpg", ".png")]
pages  = ["email.html", "email-2.html", "email-3.html", "index.html"]

for page in pages:
    p = here / page
    if not p.exists(): continue
    s = orig = p.read_text()
    for a in assets:
        d = h(a)
        s = re.sub(rf'(src="{re.escape(a)})(\?v=[0-9a-f]+)?"', rf'\1?v={d}"', s)
    if s != orig:
        p.write_text(s); print(f"  stamped {page}")

# iframe srcs point at pages, hash those too
idx = here / "index.html"
s = idx.read_text()
for page in ("email.html", "email-2.html", "email-3.html"):
    d = hashlib.sha1((here/page).read_bytes()).hexdigest()[:8]
    s = re.sub(rf'({re.escape(page)})\?v=[0-9a-zA-Z]+', rf'\1?v={d}', s)
idx.write_text(s); print("  stamped iframe srcs")
