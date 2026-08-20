# -*- coding: utf-8 -*-
"""Sinh toàn bộ 31 trang tĩnh của Infinite Studio Makerspace (bản Pastel Filament)."""
import os, re, html
from data import *

OUT = "/home/claude/site"
PAL = ["mint", "bubble", "butter", "sky", "lilac", "peach"]


# ---------------------------------------------------------------- thông tin thật
SITE = {
    "DIACHI":   "25/11 Đường số 6, Khu phố 6, Hiệp Bình, TP. Hồ Chí Minh",
    "GIOMOCUA": "9:00 — 17:00, Thứ 2 — Thứ 6",
    "ZALO":     "0816193459",
    "EMAIL":    "infinitebuildshop@gmail.com",
    "FACEBOOK": "https://www.facebook.com/profile.php?id=61590361168112",
    "SHOPEE":   "https://shopee.vn/infinitebuilds?entryPoint=ShopBySearch&amp;searchKeyword=infinite%20build",
    "MAPS":     "https://share.google/0KVPB5H3gwupVOjRF",
}

def ph(cap, i=0, extra=""):
    """Ô ảnh placeholder pastel (site mẫu không dùng file ảnh, chỉ có caption)."""
    return ('<div class="ph ph-%s layerlines %s"><em>%s</em></div>' % (PAL[i % 6], extra, cap))


LOGO = """<a class="logo" href="{P}index.html">
      <img class="mark" src="{P}assets/logo.png" alt="Infinite Builds" width="256" height="256">
      <span class="ltxt"><b>Infinite Studio Makerspace</b></span>
    </a>"""

NAVITEMS = [("index.html", "Home"), ("services.html", "Services"), ("about.html", "About"),
            ("location.html", "Location"), ("news.html", "News"), ("contact.html", "Contact")]


def header(active):
    nav = "".join('<a %shref="{P}%s">%s</a>' % ('class="on" ' if h == active else "", h, t)
                  for h, t in NAVITEMS)
    mob = nav + ''.join('<a href="{P}%s">%s</a>' % (h, t) for h, t in [
        ("makerspace/3d-printing.html", "3D Print"), ("makerspace/laser-cutting.html", "Laser Cut"),
        ("makerspace/paper-craft.html", "Cricut"), ("services.html#pricing", "Bảng giá"),
        ("services.html#workshops", "Workshop")])
    return """<header>
  <div class="wrap hd">
    %s
    <nav class="mainnav">%s</nav>
    <div class="hd-r">
      <a class="btn btn-sm" href="{P}contact.html">Join</a>
      <button class="burger" id="burger" aria-label="Menu">☰</button>
    </div>
  </div>
</header>
<div class="mobmenu" id="mobmenu"><div class="mobmenu__in">%s</div></div>""" % (LOGO, nav, mob)


FOOTER = """<footer>
  <div class="wrap">
    <div class="fgrid">
      <div class="fbrand">
        %s
        <p>Không gian sáng tạo dành cho maker và creators.</p>
        <p class="addr">{{DIACHI}}</p>
      </div>
      <div>
        <h4>Menu</h4>
        <ul><li><a href="{P}index.html">Home</a></li><li><a href="{P}services.html">Services</a></li>
        <li><a href="{P}about.html">About</a></li><li><a href="{P}location.html">Location</a></li>
        <li><a href="{P}news.html">News</a></li><li><a href="{P}contact.html">Contact</a></li></ul>
      </div>
      <div>
        <h4>Makerspace</h4>
        <ul><li><a href="{P}makerspace/3d-printing.html">3D Print</a></li>
        <li><a href="{P}makerspace/laser-cutting.html">Laser Cut</a></li>
        <li><a href="{P}makerspace/paper-craft.html">Cricut &amp; Thủ công giấy</a></li>
        <li><a href="{P}services.html#workshops">Workshop</a></li>
        <li><a href="{P}services.html#business">Sản xuất số lượng lớn</a></li>
        <li><a href="{P}services.html#pricing">Bảng giá</a></li></ul>
      </div>
      <div>
        <h4>Chính sách</h4>
        <ul><li><a href="{P}policies/an-toan.html">Nội quy an toàn</a></li>
        <li><a href="{P}policies/thanh-vien.html">Chính sách thành viên</a></li>
        <li><a href="{P}policies/doi-tra.html">Đổi trả &amp; bảo hành</a></li>
        <li><a href="{P}policies/bao-mat.html">Chính sách bảo mật</a></li>
        <li><a href="{P}policies/dieu-khoan.html">Điều khoản sử dụng</a></li>
        <li><a href="{P}policies/faq.html">Câu hỏi thường gặp</a></li></ul>
      </div>
      <div>
        <div class="fblock"><h4>Liên hệ &amp; theo dõi</h4>
          <ul><li><a href="https://zalo.me/{{ZALO}}">Zalo</a></li>
          <li><a href="mailto:{{EMAIL}}">{{EMAIL}}</a></li>
          <li><a href="{{FACEBOOK}}">Facebook</a></li>
          <li><a href="{{SHOPEE}}">Shopee</a></li></ul></div>
        <div class="fblock"><h4>Giờ mở cửa</h4><p>{{GIOMOCUA}}</p></div>
        <div class="fblock"><h4>Địa chỉ</h4><p>{{DIACHI}}</p></div>
        <div class="fblock"><h4>Hotline / Zalo</h4><p>{{ZALO}}</p></div>
        <div class="fblock"><h4>Email</h4><p>{{EMAIL}}</p></div>
      </div>
    </div>
    <div class="fmark">Infinite Studio Makerspace</div>
    <div class="fbot">
      <span>© <span class="js-year">2026</span> Infinite Studio Makerspace</span>
      <span>Không gian sáng tạo dành cho maker và creators</span>
    </div>
  </div>
</footer>
<div class="mbar">
  <a class="btn btn-soft btn-sm" href="https://zalo.me/{{ZALO}}">Chat Zalo</a>
  <a class="btn btn-sm" href="{P}contact.html">Join Infinite</a>
</div>""" % LOGO

SHELL = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="icon" href="{P}assets/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800&amp;family=Be+Vietnam+Pro:wght@300;400;500;600;700;800&amp;display=swap">
<link rel="stylesheet" href="{P}assets/ib.v2.css">
</head>
<body>
%(header)s
%(body)s
%(footer)s
<script src="{P}assets/ib.v2.js" defer></script>
</body>
</html>
"""

PAGES = []


def write(path, title, desc, body, active=""):
    doc = SHELL % dict(title=title, desc=desc, header=header(active), body=body, footer=FOOTER)
    # Cách dẫn link copy y hệt website mẫu: URL gốc tuyệt đối, không đuôi .html
    doc = doc.replace("{P}", "/")
    doc = re.sub(r'href="/index\.html', 'href="/', doc)
    doc = re.sub(r'href="(/[^"#]*?)\.html', r'href="\1', doc)
    for k, v in SITE.items():
        doc = doc.replace("{{%s}}" % k, v)
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(doc)
    PAGES.append(path)


# ---------- khối dùng lại ----------
def crumb(items):
    """items: [(label, href|None)]"""
    parts = []
    for lab, href in items:
        parts.append('<a href="%s">%s</a>' % (href, lab) if href else "<b>%s</b>" % lab)
    return '<div class="wrap crumb">%s</div>' % '<span>·</span>'.join(parts)


def phero(lab, h1, lead, actions="", cls=""):
    return """<section class="phero %s">
  <div class="blob b1"></div><div class="blob b2"></div>
  <div class="wrap"><div class="phero__in">
    %s<h1 class="d1">%s</h1><p class="lead">%s</p>%s
  </div></div>
</section>""" % (cls, '<span class="lab">%s</span>' % lab if lab else "", h1, lead,
                 '<div class="actions">%s</div>' % actions if actions else "")


def btn(label, href, kind=""):
    return '<a class="btn %s" href="%s">%s <span class="arrow">→</span></a>' % (kind, href, label)


def flow(steps):
    return '<div class="flow rv">%s</div>' % "".join(
        '<div class="step"><b>%02d</b><span>%s</span></div>' % (i + 1, s) for i, s in enumerate(steps))


def gallery(caps, start=0):
    return '<div class="gal">%s</div>' % "".join(
        ph(c, start + i, "rv") for i, c in enumerate(caps))


def cta(h2, lead, actions):
    return """<section class="cta">
  <div class="wrap">
    <h2 class="d2 rv">%s</h2><p class="lead rv">%s</p>
    <div class="actions rv">%s</div>
  </div>
</section>""" % (h2, lead, actions)


def marquee(words, tone="butter"):
    span = "".join("<span>%s</span>" % w for w in words)
    return '<div class="mq mq-%s"><div class="mq__track">%s%s</div></div>' % (tone, span, span)


def wcard(w, P="{P}"):
    return """<a class="wcard rv" href="%sservices/workshops/%s.html">
  <div class="wcat">%s</div><h3>%s</h3><p>%s</p>
  <div class="chips"><span class="chipsm">%s</span><span class="chipsm">%s</span><span class="chipsm">%s</span></div>
  <div class="wprice">%s <span>Chi tiết →</span></div></a>""" % (
        P, w["slug"], w["cat"], w["title"], w["desc"], w["level"], w["hours"], w["cap"], w["price"])


def pcard(p, i=0):
    return """<a class="card rv" href="{P}projects/%s.html" data-cat="%s">
  <div class="ph ph-%s layerlines sq"><span class="ctag">%s</span><em>%s</em></div>
  <div class="cbody"><h3>%s</h3><p>%s</p><span class="cgo">Xem sản phẩm →</span></div></a>""" % (
        p["slug"], p["cat"], PAL[i % 6], p["tag"], p["hero"], p["nav"], p["blurb"])


PLANS = """<div class="plans">
  <article class="plan plan-a rv"><div class="plan__orb"></div>
    <div class="pname">Basic · Gói cơ bản</div>
    <div class="price">450<small>K / tháng</small></div>
    <p class="sub">Một khu vực do bạn chọn</p>
    <ul><li>Chọn 1 trong 3 khu: Laser Cut, In 3D hoặc Thủ công giấy</li>
    <li>Training an toàn và vận hành máy buổi đầu</li>
    <li>Đặt lịch máy qua hệ thống booking</li>
    <li>Chỗ ngồi làm việc trong giờ mở cửa</li></ul>
    <div class="deals"><div class="deal"><b>350K</b><span>Tháng đầu tiên</span></div>
    <div class="deal"><b>1.050K</b><span>Gói 3 tháng</span></div></div>
    <a class="btn btn-line" href="{P}contact.html">Chọn gói Basic <span class="arrow">→</span></a>
  </article>
  <article class="plan plan-b rv"><div class="ribbon">Phổ biến</div><div class="plan__orb"></div>
    <div class="pname">Premium</div>
    <div class="price">750<small>K / tháng</small></div>
    <p class="sub">Trọn cả ba khu vực</p>
    <ul><li>Toàn quyền dùng cả 3 khu: Laser Cut, In 3D và Thủ công giấy</li>
    <li>Training đầy đủ cho mọi máy trong xưởng</li>
    <li>Ưu tiên đặt lịch máy vào giờ cao điểm</li>
    <li>Ưu đãi khi đăng ký workshop</li>
    <li>Kho để đồ cá nhân trong xưởng</li></ul>
    <div class="deals"><div class="deal"><b>500K</b><span>Tháng đầu tiên</span></div>
    <div class="deal"><b>1.500K</b><span>Gói 3 tháng</span></div></div>
    <a class="btn" href="{P}contact.html">Chọn gói Premium <span class="arrow">→</span></a>
  </article>
</div>
<div class="packs rv"><div class="pack-h">3-Month Packages · Gói 3 tháng</div>
  <div class="packrow">
    <div class="pack"><b>1.050K</b><span>Basic · 3 tháng</span><i>Tiết kiệm 300K so với trả từng tháng</i></div>
    <div class="pack"><b>1.500K</b><span>Premium · 3 tháng</span><i>Tiết kiệm 750K so với trả từng tháng</i></div>
  </div></div>"""
