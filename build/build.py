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
    "FACEBOOK": "https://www.facebook.com/share/1HADr55sNW/?mibextid=wwXIfr",
    "INSTAGRAM": "https://www.instagram.com/infinite.stu/",
    "MESSENGER": "https://m.me/61590361168112",
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
        ("makerspace/paper-craft.html", "Paper Craft"), ("services.html#pricing", "Pricing"),
        ("services.html#workshops", "Workshops")])
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


ICONS = {
 "zalo": '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M12 3.4c-5 0-8.8 3.3-8.8 7.4 0 2.3 1.2 4.4 3.2 5.7-.2 1-.6 2-1.3 2.8 1.5-.2 3-.9 4-1.6.9.3 1.9.4 2.9.4 5 0 8.8-3.3 8.8-7.3S17 3.4 12 3.4Z"/><path fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" d="M9.3 8.2h5.4l-5.4 5h5.4"/></svg>',
 "fb": '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path fill="currentColor" d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.7-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12Z"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path fill="currentColor" d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4 1.3-.1 1.7-.1 4.8-.1Zm0 3.1A6.7 6.7 0 1 0 18.7 12 6.7 6.7 0 0 0 12 5.3Zm0 11A4.3 4.3 0 1 1 16.3 12 4.3 4.3 0 0 1 12 16.3Zm6.9-11.2a1.6 1.6 0 1 1-1.6-1.6 1.6 1.6 0 0 1 1.6 1.6Z"/></svg>',
 "shopee": '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round" d="M4.6 8h14.8l-1 12.1H5.6L4.6 8Z"/><path fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" d="M8.4 8V6.6a3.6 3.6 0 0 1 7.2 0V8"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path fill="currentColor" d="M3 5.5h18c.6 0 1 .4 1 1v11c0 .6-.4 1-1 1H3c-.6 0-1-.4-1-1v-11c0-.6.4-1 1-1Zm1.7 1.8L12 12.4l7.3-5.1H4.7Z"/></svg>',
 "mess": '<svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true"><path fill="currentColor" d="M12 2C6.3 2 2 6.2 2 11.8c0 3 1.3 5.7 3.5 7.5v3.2l3.2-1.8c1 .3 2.1.4 3.3.4 5.7 0 10-4.2 10-9.8S17.7 2 12 2Zm1 12.4-2.6-2.7-4.9 2.7 5.4-5.7 2.6 2.7 4.8-2.7-5.3 5.7Z"/></svg>',
}

FOOTER = """<footer>
  <div class="wrap">
    <div class="fgrid">
      <div class="fbrand">
        %(logo)s
        <p>Không gian sáng tạo dành cho maker và creators.</p>
        <p class="addr">{{DIACHI}}</p>
        <p class="addr">{{GIOMOCUA}}</p>
      </div>
      <div>
        <h4>Makerspace</h4>
        <ul><li><a href="{P}services.html#business">Small-Batch &amp; Mass Production</a></li>
        <li><a href="{P}makerspace/3d-printing.html">3D Print</a></li>
        <li><a href="{P}makerspace/laser-cutting.html">Laser Cut</a></li>
        <li><a href="{P}makerspace/paper-craft.html">Paper Craft</a></li>
        <li><a href="{P}services.html#workshops">Workshops</a></li>
        <li><a href="{P}services.html#pricing">Pricing</a></li></ul>
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
        <h4>Contact</h4>
        <div class="fsocial">
          <a href="https://zalo.me/{{ZALO}}" aria-label="Zalo" title="Zalo" target="_blank" rel="noopener">%(zalo)s</a>
          <a href="{{FACEBOOK}}" aria-label="Facebook" title="Facebook" target="_blank" rel="noopener">%(fb)s</a>
          <a href="{{INSTAGRAM}}" aria-label="Instagram" title="Instagram" target="_blank" rel="noopener">%(ig)s</a>
          <a href="{{SHOPEE}}" aria-label="Shopee" title="Shopee" target="_blank" rel="noopener">%(shopee)s</a>
          <a href="mailto:{{EMAIL}}" aria-label="Email" title="Email">%(mail)s</a>
        </div>
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
</div>
<div class="chatdock">
  <a class="cbtn cbtn-mess" href="{{MESSENGER}}" target="_blank" rel="noopener"
     aria-label="Chat Messenger"><span class="cico">%(mess)s</span><span class="ctxt">Messenger</span></a>
  <a class="cbtn cbtn-zalo" href="https://zalo.me/{{ZALO}}" target="_blank" rel="noopener"
     aria-label="Chat Zalo"><span class="cico">%(zalo)s</span><span class="ctxt">Zalo</span></a>
</div>""" % dict(ICONS, logo=LOGO)

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
<link rel="stylesheet" href="{P}assets/ib.v3.css">
</head>
<body>
%(header)s
%(body)s
%(footer)s
<script src="{P}assets/ib.v3.js" defer></script>
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
    has_img = bool(p.get("img"))
    media = ('<img src="{P}%s" alt="%s" loading="lazy" width="640" height="640">' % (p["img"], html.escape(p["nav"], quote=True))
              if has_img else "<em>%s</em>" % p["hero"])
    return """<a class="card rv" href="{P}projects/%s.html" data-cat="%s">
  <div class="ph ph-%s%s sq"><span class="ctag">%s</span>%s</div>
  <div class="cbody"><h3>%s</h3><p>%s</p><span class="cgo">Xem sản phẩm →</span></div></a>""" % (
        p["slug"], p["cat"], PAL[i % 6], "" if has_img else " layerlines", p["tag"], media, p["nav"], p["blurb"])


PLANS = """<div class="plans">
  <article class="plan plan-a rv"><div class="plan__orb"></div>
    <div class="pname">Basic</div>
    <div class="price">350<small>K / tháng</small><span class="pnote">Chỉ áp dụng tháng đầu tiên</span></div>
    <ul><li>Chọn 1 trong 3 khu: Laser Cut, In 3D hoặc Thủ công giấy</li>
    <li>Training an toàn và vận hành máy trong quá trình sử dụng máy</li>
    <li>Đặt lịch máy qua hệ thống booking</li></ul>
    <div class="deals"><div class="deal"><b>500K</b><span>Mỗi tháng</span></div>
    <div class="deal"><b>1.050K</b><span class="hl">Gói 3 tháng</span><i>Tiết kiệm 450K so với trả từng tháng</i></div></div>
    <a class="btn btn-line" href="{P}contact.html">Chọn gói Basic <span class="arrow">→</span></a>
  </article>
  <article class="plan plan-b rv"><div class="ribbon">Phổ biến</div><div class="plan__orb"></div>
    <div class="pname">Premium</div>
    <div class="price">500<small>K / tháng</small><span class="pnote">Chỉ áp dụng tháng đầu tiên</span></div>
    <ul><li>Toàn quyền dùng cả 3 khu: Laser Cut, In 3D và Thủ công giấy</li>
    <li>Training đầy đủ cho mọi máy trong xưởng</li>
    <li>Ưu tiên đặt lịch máy vào giờ cao điểm</li></ul>
    <div class="deals"><div class="deal"><b>800K</b><span>Mỗi tháng</span></div>
    <div class="deal"><b>1.500K</b><span class="hl">Gói 3 tháng</span><i>Tiết kiệm 900K so với trả từng tháng</i></div></div>
    <a class="btn" href="{P}contact.html">Chọn gói Premium <span class="arrow">→</span></a>
  </article>
</div>"""
