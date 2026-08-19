# -*- coding: utf-8 -*-
"""
Dựng gói thay thế khớp ĐÚNG cấu trúc repo hiện tại của M:
website nằm ngay ở gốc repo (index.html, about.html, assets/, projects/ ...).

  gốc repo  -> bản Netlify (giữ nguyên cài đặt publish directory hiện tại)
  docs/     -> bản GitHub Pages (thư mục + index.html, link tương đối)
  build/    -> mã nguồn sinh trang
"""
import os, re, shutil

SRC = "site"
OUT = "thay-vao-repo"

if os.path.exists(OUT):
    shutil.rmtree(OUT)
shutil.copytree(SRC, OUT)
for junk in ("__pycache__",):
    p = os.path.join(OUT, junk)
    if os.path.exists(p):
        shutil.rmtree(p)

# netlify.toml: site ở gốc repo
nt = open(os.path.join(OUT, "netlify.toml"), encoding="utf-8").read()
nt = nt.replace('publish = "."', 'publish = "."')
open(os.path.join(OUT, "netlify.toml"), "w", encoding="utf-8").write(nt)

# robots.txt: không cho index bản dự phòng docs/
rb = open(os.path.join(OUT, "robots.txt"), encoding="utf-8").read()
if "Disallow: /docs/" not in rb:
    rb = rb.replace("Allow: /\n", "Allow: /\nDisallow: /docs/\n")
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(rb)

# ---------------------------------------------------------------- docs/
DOCS = os.path.join(OUT, "docs")
shutil.copytree(SRC, DOCS)
for junk in ("__pycache__", "netlify.toml", "serve.py", "README.md"):
    p = os.path.join(DOCS, junk)
    if os.path.isdir(p):
        shutil.rmtree(p)
    elif os.path.exists(p):
        os.remove(p)

moved = 0
for r, d, f in os.walk(DOCS):
    for x in list(f):
        if not x.endswith(".html") or x in ("index.html", "404.html"):
            continue
        newdir = os.path.join(r, x[:-5])
        os.makedirs(newdir, exist_ok=True)
        shutil.move(os.path.join(r, x), os.path.join(newdir, "index.html"))
        moved += 1


def to_rel(url, depth):
    up = "../" * depth if depth else ""
    path, sep, frag = url.partition("#")
    if path in ("", "/"):
        return (up or "./") + (sep + frag if sep else "")
    p = path.lstrip("/")
    if re.search(r"\.(css|js|svg|xml|txt|png|jpg|webp|ico)$", p):
        return up + p + (sep + frag if sep else "")
    return up + p + "/" + (sep + frag if sep else "")


count = 0
for r, d, f in os.walk(DOCS):
    for x in f:
        if not x.endswith(".html"):
            continue
        p = os.path.join(r, x)
        depth = os.path.relpath(p, DOCS).count(os.sep)
        s = open(p, encoding="utf-8").read()

        def rep(m):
            global count
            count += 1
            return '%s="%s"' % (m.group(1), to_rel(m.group(2), depth))

        s = re.sub(r'\b(href|src)="(/[^"]*)"', rep, s)
        open(p, "w", encoding="utf-8").write(s)

sm = open(os.path.join(DOCS, "sitemap.xml"), encoding="utf-8").read()
sm = re.sub(r"<loc>https://TEN-MIEN-CUA-BAN/([^<]*?)\.html</loc>",
            r"<loc>https://TEN-MIEN-CUA-BAN/\1/</loc>", sm)
open(os.path.join(DOCS, "sitemap.xml"), "w", encoding="utf-8").write(sm)
open(os.path.join(DOCS, ".nojekyll"), "w").write("")

# ---------------------------------------------------------------- nguồn
os.makedirs(os.path.join(OUT, "build"), exist_ok=True)
for f in ("data.py", "build.py", "pages.py", "make_repo2.py"):
    shutil.copy(f, os.path.join(OUT, "build", f))

open(os.path.join(OUT, ".gitignore"), "w", encoding="utf-8").write(
    "__pycache__/\n*.pyc\n.DS_Store\n.netlify/\n")

root_html = [x for x in os.listdir(OUT) if x.endswith(".html")]
print("file .html ở gốc:", sorted(root_html))
print("thư mục ở gốc  :", sorted(x for x in os.listdir(OUT) if os.path.isdir(os.path.join(OUT, x))))
print("docs/: chuyển", moved, "trang, đổi", count, "link sang tương đối")
