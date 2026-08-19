# -*- coding: utf-8 -*-
"""Định nghĩa 31 trang."""
from build import *

# =============================================================== TRANG CHỦ
HOUSE = """<div class="house">
  <div class="hfloat hf-1"><i style="background:var(--mint-deep)"></i> Community</div>
  <div class="hfloat hf-2"><i style="background:var(--lilac-deep)"></i> Workshop</div>
  <div class="hfloat hf-3"><i style="background:var(--peach-deep)"></i> 3D Print · Laser Cut · Cricut</div>
  <svg viewBox="0 0 520 440" role="img" aria-label="Minh hoạ xưởng Infinite Maker Space với bốn khu vực">
    <defs>
      <linearGradient id="roof" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="#FFC7DD"/><stop offset="1" stop-color="#D5C9F7"/></linearGradient>
      <pattern id="ll" width="6" height="5" patternUnits="userSpaceOnUse">
        <rect width="6" height="1" fill="#fff" opacity=".55"/></pattern>
    </defs>
    <path d="M260 24 500 218 20 218Z" fill="url(#roof)" stroke="#2A2340" stroke-width="4" stroke-linejoin="round"/>
    <path d="M260 24 500 218 20 218Z" fill="url(#ll)" opacity=".45"/>
    <rect x="392" y="70" width="30" height="70" rx="10" fill="#FFC9B4" stroke="#2A2340" stroke-width="4"/>
    <rect x="238" y="122" width="46" height="46" rx="8" fill="#FFFBF4" stroke="#2A2340" stroke-width="4"/>
    <path d="M261 122v46M238 145h46" stroke="#2A2340" stroke-width="4"/>
    <rect x="46" y="218" width="428" height="182" rx="20" fill="#FFFBF4" stroke="#2A2340" stroke-width="4"/>
    <rect x="66" y="236" width="190" height="70" rx="12" fill="#B9EBD8"/>
    <rect x="66" y="236" width="190" height="70" rx="12" fill="url(#ll)" opacity=".5"/>
    <rect x="266" y="236" width="190" height="70" rx="12" fill="#FFC9B4"/>
    <rect x="266" y="236" width="190" height="70" rx="12" fill="url(#ll)" opacity=".5"/>
    <rect x="66" y="316" width="190" height="70" rx="12" fill="#D5C9F7"/>
    <rect x="66" y="316" width="190" height="70" rx="12" fill="url(#ll)" opacity=".5"/>
    <rect x="266" y="316" width="190" height="70" rx="12" fill="#FFE7AE"/>
    <rect x="266" y="316" width="190" height="70" rx="12" fill="url(#ll)" opacity=".5"/>
    <g stroke="#2A2340" stroke-width="3.4" stroke-linecap="round" fill="none">
      <path d="M136 258h50M161 258v22"/><rect x="150" y="280" width="22" height="14" rx="4" fill="#FF8F6B" stroke="none"/>
      <path d="M336 258h50M361 258v24"/><path d="M355 286l6-6 6 6"/>
      <rect x="147" y="336" width="28" height="34" rx="5"/><path d="M154 346h14M154 354h14"/>
      <circle cx="352" cy="346" r="9"/><path d="M338 370c0-9 6-14 14-14s14 5 14 14"/>
      <circle cx="378" cy="348" r="7" fill="#FFC7DD" stroke="none"/>
    </g>
    <rect x="196" y="400" width="128" height="14" rx="7" fill="#FFE7AE" stroke="#2A2340" stroke-width="4"/>
    <circle cx="24" cy="378" r="22" fill="#B9EBD8" stroke="#2A2340" stroke-width="4"/>
    <circle cx="496" cy="384" r="18" fill="#BCDFFA" stroke="#2A2340" stroke-width="4"/>
  </svg>
</div>"""

ZONES = [
    ("3d-printing", "3D Print", ["Bambu Lab A1", "Bambu Lab A2L"],
     "Hai máy in FDM luôn sẵn sàng cho prototype, miniature, chi tiết sản phẩm và sản xuất lô nhỏ.",
     "Xem máy &amp; sản phẩm in 3D →", "Ảnh: máy in 3D đang chạy, cận cảnh lớp nhựa đang hình thành"),
    ("laser-cutting", "Laser Cut", ["Máy cắt laser khổ lớn"],
     "Một máy cắt laser khổ lớn, cắt và khắc gỗ, mica và nhiều vật liệu tấm khác.",
     "Xem máy &amp; sản phẩm cắt laser →", "Ảnh: tia laser đang cắt tấm gỗ, khói mỏng bay lên"),
    ("paper-craft", "Cricut", ["Máy in màu", "Máy cắt Cricut"],
     "Khu thủ công giấy: một máy in màu, một máy cắt Cricut và đầy đủ dụng cụ làm tay.",
     "Xem khu thủ công giấy →", "Ảnh: bàn tay đang bóc sticker vừa cắt bằng Cricut"),
]

zones_html = "".join("""<a class="card rv" href="{P}makerspace/%s.html">
  <div class="ph ph-%s layerlines"><em>%s</em></div>
  <div class="cbody"><h3>%s</h3><div class="chips">%s</div><p>%s</p>
  <span class="cgo">%s</span></div></a>""" % (
    z[0], PAL[i * 2 % 6], z[5], z[1],
    "".join('<span class="chipsm">%s</span>' % t for t in z[2]), z[3], z[4])
    for i, z in enumerate(ZONES))

home = """<section class="hero">
  <div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div>
  <div class="wrap hero__grid">
    <div>
      <span class="tagpill">✿ Đang mở đăng ký thành viên</span>
      <h1 class="d1">Where ideas<br>become <span class="accent">reality</span>.</h1>
      <p class="lead">Infinite Maker Space là không gian dành cho những người trẻ yêu thích sáng tạo, in 3D,
      thiết kế 3D, cắt laser và DIY — với máy móc, hướng dẫn và cộng đồng sẵn sàng giúp bạn biến ý tưởng
      thành sản phẩm thật.</p>
      <div class="hero__actions">%s%s</div>
    </div>
    %s
  </div>
  <div class="wrap"><div class="swatches layerlines">
    <div style="background:var(--mint)"></div><div style="background:var(--sky)"></div>
    <div style="background:var(--lilac)"></div><div style="background:var(--bubble)"></div>
    <div style="background:var(--peach)"></div><div style="background:var(--butter)"></div>
  </div></div>
</section>
%s
<section class="sec" id="space">
  <div class="wrap">
    <div class="split-head">
      <div class="rv"><span class="lab">01 — Maker Space</span>
        <h2 class="d2 mb-s">Ba khu vực,<br>một <span class="accent">xưởng</span>.</h2></div>
      <p class="lead rv">Bấm vào từng khu để xem hình máy móc, sản phẩm đã làm và những gì bạn có thể tạo ra ở đó.</p>
    </div>
    <div class="grid g3">%s</div>
  </div>
</section>
<section class="sec-sm">
  <div class="wrap">
    <div class="rv"><span class="lab">02 — Infinite Maker Space in Numbers</span>
      <h2 class="d2 mb-l">Con số tới <span class="accent">hôm nay</span>.</h2></div>
    <div class="grid g4">
      <div class="tile t-mint stat rv"><div class="tile__orb"></div><b><span class="num" data-count="3000">0</span>+</b><span>Sản phẩm hoàn thành</span></div>
      <div class="tile t-butter stat rv"><div class="tile__orb"></div><b>24H</b><span>Thời gian phản hồi</span></div>
      <div class="tile t-lilac stat rv"><div class="tile__orb"></div><b><span class="num" data-count="9">0</span>+</b><span>Máy móc chuyên dụng</span></div>
      <div class="tile t-bubble stat rv"><div class="tile__orb"></div><b><span class="num" data-count="20">0</span>+</b><span>Workshop sắp tổ chức</span></div>
    </div>
  </div>
</section>
<section class="sec" id="pricing">
  <div class="wrap">
    <div class="sechead rv"><span class="lab">Pricing</span>
      <h2 class="d2 mb-s">Chọn cách bạn<br>muốn <span class="accent">làm</span>.</h2>
      <p class="lead">Hai gói, ba khu vực, không phí ẩn. Tháng đầu tiên luôn rẻ hơn để bạn thử trước khi quyết định gắn bó.</p></div>
    %s
  </div>
</section>
<section class="sec" id="made">
  <div class="wrap">
    <div class="split-head">
      <div class="rv"><span class="lab">03 — What We Make</span>
        <h2 class="d2 mb-s">Thiết kế ở đây.<br>Làm ra ở <span class="accent">đây</span>.</h2></div>
      <p class="lead rv">Bảy dòng sản phẩm đang được đội ngũ Infinite Studio sản xuất và xuất khẩu sang thị trường Mỹ
      cùng nhiều nước châu Âu. Bấm vào từng sản phẩm để xem câu chuyện đằng sau nó.</p>
    </div>
    %s
    <div class="filters rv" data-filterset="madeGrid" style="margin-top:34px">
      <button class="pf on" data-f="all">Tất cả</button><button class="pf" data-f="3d">In 3D</button>
      <button class="pf" data-f="laser">Cắt laser</button><button class="pf" data-f="dien-tu">Điện tử</button>
      <button class="pf" data-f="giao-duc">Giáo dục</button>
    </div>
    <div class="grid g4" id="madeGrid">%s</div>
  </div>
</section>
%s
<div class="tint layerlines">
  <div class="wrap tint__in">
    <div class="rv"><span class="lab">04 — Workshops</span>
      <h2 class="d2 mb-s">Học bằng cách <span class="accent">tự làm</span>.</h2>
      <p class="lead">Bốn lớp được đăng ký nhiều nhất. Xem đủ tám workshop và giá từng lớp trong mục Services.</p></div>
    <div class="rv">%s</div>
  </div>
</div>
<section class="sec" id="workshops">
  <div class="wrap">
    <div class="grid g4">%s</div>
    <p class="wnote rv">Bấm vào từng lớp để xem chi tiết. Lịch cụ thể cập nhật hàng tháng — nhắn Zalo để biết lớp gần nhất còn chỗ.</p>
  </div>
</section>
%s""" % (
    btn("Khám phá không gian", "#space"), btn("Xem bảng giá", "{P}services.html#pricing", "btn-soft"),
    HOUSE,
    marquee(["Maker", "Creator", "In 3D", "Thiết kế 3D", "Cắt laser", "Thủ công giấy", "DIY", "Prototype", "Cộng đồng"], "butter"),
    zones_html, PLANS,
    flow(["Ý tưởng", "Thiết kế", "Prototype", "Sản xuất", "Đóng gói", "Xuất khẩu"]),
    "".join(pcard(p, i) for i, p in enumerate(PROJECTS)),
    marquee(GUIDES[:3], "mint"),
    btn("Xem tất cả workshop", "{P}services.html#workshops", "btn-line"),
    "".join(wcard(w) for w in WORKSHOPS[:4]),
    cta("Ý tưởng của bạn có thể là <span class='accent'>cái tiếp theo</span>.",
        "Dù bạn đang dựng bản prototype đầu tiên, học một kỹ năng mới hay muốn biến ý tưởng thành sản phẩm bán được — Infinite là nơi để bắt đầu.",
        btn("Tham gia Infinite", "{P}contact.html") + btn("Xem dịch vụ", "{P}services.html", "btn-line")))

write("index.html", "Infinite Maker Space — Where Ideas Become Reality",
      "Không gian sáng tạo dành cho maker và creators. In 3D, thiết kế 3D, cắt laser, thủ công giấy và workshop tại TP. Hồ Chí Minh.",
      home, "index.html")

# =============================================================== SERVICES
SERVICE_BLOCKS = [
 ("Dịch vụ 01","In 3D",["Dự án cá nhân","Bài tập sinh viên","Prototype","Phát triển sản phẩm","Sản xuất lô nhỏ","In số lượng lớn"],
  "Bắt đầu dự án in 3D","{P}makerspace/3d-printing.html","mint"),
 ("Dịch vụ 02","Cắt laser",["Cắt gỗ","Cắt mica","Khắc bề mặt","Prototype","Đồ trang trí","Sản phẩm DIY","Sản xuất theo lô"],
  "Bắt đầu dự án cắt laser","{P}makerspace/laser-cutting.html","peach"),
 ("Dịch vụ 03","Thủ công giấy",["Cắt Cricut","In màu","Sticker","Nhãn dán","Bao bì","Mô hình giấy","Đồ handmade"],
  "Bắt đầu dự án giấy","{P}makerspace/paper-craft.html","lilac"),
]
svc = "".join("""<article class="tile t-%s rv"><div class="tile__orb"></div>
  <div class="pname">%s</div><h3 class="d3" style="margin-top:10px">%s</h3>
  <div class="chips" style="margin-top:16px">%s</div>
  <div style="margin-top:22px"><a class="btn btn-line" href="%s">%s <span class="arrow">→</span></a></div>
</article>""" % (c, lab, name, "".join('<span class="chipsm">%s</span>' % t for t in tags), href, cta_)
  for lab, name, tags, cta_, href, c in SERVICE_BLOCKS)

NOTES = [("Vật liệu","Chưa bao gồm trong phí thành viên. Bạn có thể mang vật liệu riêng hoặc mua tại xưởng theo bảng giá niêm yết."),
 ("Training ban đầu","Bắt buộc với mọi máy trước lần dùng đầu tiên — miễn phí cho thành viên."),
 ("Đặt lịch máy","Đặt trước qua Zalo hoặc tại quầy. Mỗi lượt tối đa 3 giờ liên tục, gia hạn được nếu không có người chờ."),
 ("Giới hạn sử dụng","Không giới hạn số giờ trong giờ mở cửa, nhưng ưu tiên chia đều khi đông người."),
 ("An toàn","Bắt buộc đeo kính bảo hộ ở khu laser, buộc tóc gọn, không để máy chạy khi không có người trông."),
 ("Vật tư tiêu hao","Nhựa in, tấm gỗ, mica, giấy và lưỡi dao Cricut tính phí riêng theo mức dùng thực tế.")]

services_body = crumb([("Home","{P}index.html"),("Services",None)]) + phero(
 "Services","Từ ý tưởng đến <span class='accent'>sản phẩm</span>.",
 "Dù bạn đang làm bản prototype đầu tiên hay cần sản xuất hàng trăm sản phẩm, Infinite có máy móc và người hỗ trợ để bạn dựng được nó.",
 "".join('<span class="tagpill">%s</span>' % t for t in ["In 3D","Cắt laser","Thủ công giấy","Sản xuất lô lớn","Workshop"])
) + """
<section class="sec sec-t0"><div class="wrap"><div class="grid g3">%s</div></div></section>

<section class="sec sec-t0" id="business"><div class="wrap">
  <div class="sechead rv"><span class="lab">Dịch vụ 04</span>
    <h2 class="d2 mb-s">Nhận in 3D và cắt laser <span class="accent">số lượng lớn</span>.</h2>
    <p class="lead">Infinite nhận sản xuất cho doanh nghiệp, thương hiệu, startup, agency, cửa hàng bán lẻ và ban tổ chức
    sự kiện. Bạn gửi ý tưởng hoặc file thiết kế, chúng tôi lo phần còn lại — kể cả đóng gói.</p></div>
  <div class="grid g2">
    <div class="tile t-sky rv"><div class="tile__orb"></div><h3>Chúng tôi phục vụ</h3>
      <div class="chips" style="margin-top:14px">%s</div></div>
    <div class="tile t-butter rv"><div class="tile__orb"></div><h3>Hạng mục thường nhận</h3>
      <div class="chips" style="margin-top:14px">%s</div></div>
  </div>
  <div class="actions rv" style="margin-top:26px">%s</div>
</div></section>

<section class="sec sec-t0" id="pricing"><div class="wrap">
  <div class="sechead rv"><span class="lab">Pricing</span>
    <h2 class="d2 mb-s">Chọn cách bạn muốn <span class="accent">làm</span>.</h2>
    <p class="lead">Hai gói, ba khu vực, không phí ẩn. Tháng đầu tiên luôn rẻ hơn để bạn thử trước khi quyết định gắn bó.</p></div>
  %s
  <div class="sechead rv" style="margin-top:60px;margin-bottom:24px"><span class="lab">Trước khi đăng ký, bạn nên biết</span></div>
  <div class="grid g3">%s</div>
  <p class="wnote rv">Xem đầy đủ tại <a href="{P}policies/thanh-vien.html"><b>Chính sách thành viên</b></a>
  và <a href="{P}policies/an-toan.html"><b>Nội quy an toàn xưởng</b></a>.</p>
</div></section>

<section class="sec sec-t0" id="workshops"><div class="wrap">
  <div class="sechead rv"><span class="lab">Workshops</span>
    <h2 class="d2 mb-s">Học bằng cách <span class="accent">tự làm</span>.</h2>
    <p class="lead">Tám lớp thực hành giúp bạn làm quen máy móc, làm ra một sản phẩm thật và gặp những maker khác.
    Học phí đã bao gồm vật liệu.</p></div>
  <div class="grid g4">%s</div>
  <p class="wnote rv">Bấm vào từng lớp để xem chi tiết. Lịch cụ thể cập nhật hàng tháng — nhắn Zalo để biết lớp gần nhất còn chỗ.</p>
</div></section>
""" % (svc,
 "".join('<span class="chipsm">%s</span>' % t for t in ["Doanh nghiệp","Thương hiệu","Startup","Agency sáng tạo","Cửa hàng bán lẻ","Ban tổ chức sự kiện","Trường học"]),
 "".join('<span class="chipsm">%s</span>' % t for t in ["Quà tặng nhân viên","Quà tri ân khách hàng","Trang trí sự kiện","Kệ và standee trưng bày","Biển hiệu khắc laser","Sản phẩm bán lẻ","Bao bì đặc biệt","Sản xuất lô nhỏ theo yêu cầu"]),
 btn("Yêu cầu báo giá","{P}contact.html"),
 PLANS,
 "".join('<div class="card rv" style="padding:26px"><h3 style="font-size:1rem;font-family:var(--font-b)">%s</h3><p style="font-size:.93rem;color:var(--ink-60);margin-top:7px">%s</p></div>' % n for n in NOTES),
 "".join(wcard(w) for w in WORKSHOPS)
) + cta("Chưa biết nên dùng <span class='accent'>công nghệ nào</span>?",
 "Nhắn cho Infinite một dòng mô tả thứ bạn muốn làm. Team sẽ tư vấn cách làm phù hợp và chi phí dự kiến trong vòng 24 giờ.",
 btn("Nhắn Zalo","https://zalo.me/{{ZALO}}") + btn("Gửi brief qua email","mailto:{{EMAIL}}","btn-line"))

write("services.html","Services, Workshop & Bảng giá — Infinite Maker Space",
 "In 3D, cắt laser, thủ công giấy, sản xuất số lượng lớn, bảng giá thành viên và 8 workshop thực hành tại Infinite Maker Space.",
 services_body, "services.html")

# =============================================================== ABOUT
vals = "".join("""<article class="tile t-%s rv"><div class="tile__orb"></div>
  <div class="tnum">%02d</div><div class="pname" style="margin-top:8px">%s</div>
  <h3 style="margin-top:6px">%s</h3><p>%s</p></article>""" % (PAL[i % 6], i + 1, en, vi, txt)
  for i, (en, vi, txt) in enumerate(VALUES))

guides = "".join("""<div class="tile t-%s rv"><div class="tile__orb"></div>
  <div class="tnum">%02d</div><h3 style="margin-top:8px;font-size:1.06rem">%s</h3></div>""" % (PAL[i % 6], i + 1, g)
  for i, g in enumerate(GUIDES))

team = "".join("""<div class="card rv" style="padding:22px;text-align:center;align-items:center">
  <div style="width:56px;height:56px;border-radius:50%%;margin:0 auto 12px;display:grid;place-items:center;
  background:var(--%s);font-family:var(--font-d);font-weight:800">%s</div>
  <b style="font-size:.98rem">%s</b><span style="font-size:.8rem;color:var(--ink-40)">%s</span></div>""" % (
    PAL[i % 6], "".join(w[0] for w in n.split()[-2:]).upper(), n, r) for i, (n, r) in enumerate(TEAM))

about_body = crumb([("Home","{P}index.html"),("About",None)]) + phero(
 "About","Không gian sáng tạo dành cho <span class='accent'>maker và creators</span>.",
 "Infinite Maker Space không chỉ là một xưởng máy, mà là cộng đồng kết nối những cá nhân đam mê sáng tạo, tự tay chế tạo (DIY) và đổi mới công nghệ."
) + """
<section class="sec sec-t0"><div class="wrap">
  %s
  <p class="lead rv" style="margin-top:28px;max-width:60ch">Dù bạn là sinh viên, kiến trúc sư, artist hay founder của một
  hardware startup, chúng tôi cung cấp đầy đủ công cụ cần thiết để bạn bắt đầu — và cả những người sẵn sàng chỉ bạn cách dùng chúng.</p>
</div></section>

<section class="sec sec-t0"><div class="wrap">
  <div class="tint layerlines" style="border-radius:var(--r-xl);padding:56px 44px">
    <div class="rv" style="max-width:760px;position:relative;z-index:2">
      <span class="lab">Sứ mệnh của chúng tôi</span>
      <h2 class="d2 mb-s">Tạo không gian để thế hệ maker trẻ Việt Nam được học hỏi, sáng tạo, toả sáng và biến ý tưởng thành hiện thực.</h2>
    </div>
  </div>
</div></section>

<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><span class="lab">Những điều chúng tôi nói với chính mình</span>
    <h2 class="d2 mb-s">Năm câu <span class="accent">dẫn đường</span>.</h2></div>
  <div class="grid g3">%s</div>
</div></section>

<section class="sec sec-t0"><div class="wrap">
  <div class="grid g2" style="align-items:center">
    <div class="rv">%s</div>
    <div class="rv"><span class="lab">Founder</span>
      <h2 class="d3" style="margin-top:14px">Hoàng Nhật Minh</h2>
      <p style="color:var(--ink-40);font-size:.9rem;letter-spacing:.06em">Founder · Infinite Studio</p>
      <div class="quote">“Tôi luôn muốn tạo một không gian để các bạn trẻ có tài năng được đến học hỏi và toả sáng —
      nơi mở ra cho họ cơ hội phát triển lớn mạnh hơn.”</div>
      <p class="lead" style="margin-top:0">“Give young makers the space to learn, create and shine.”</p>
    </div>
  </div>
</div></section>

<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><span class="lab">Our values</span>
    <h2 class="d2 mb-s">Chúng tôi tin vào <span class="accent">điều này</span>.</h2></div>
  <div class="grid g3">%s</div>
</div></section>

<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><span class="lab">Core team</span>
    <h2 class="d2 mb-s">Những người đứng sau <span class="accent">Infinite</span>.</h2></div>
  <div class="grid g4">%s</div>
</div></section>
""" % (ph("Ảnh toàn cảnh xưởng: nhiều người đang làm việc ở các khu vực khác nhau", 0, "wide rv"),
       guides,
       ph("Ảnh chân dung founder Hoàng Nhật Minh trong xưởng", 3, "rv") .replace('class="ph', 'style="aspect-ratio:4/5;border-radius:var(--r-xl);box-shadow:var(--shadow-lift)" class="ph'),
       vals, team
) + cta("Đến làm <span class='accent'>cùng chúng tôi</span>.",
 "Ghé xưởng một buổi, xem máy chạy, nói chuyện với team. Không cần đặt lịch trước, nhưng nhắn Zalo thì chúng tôi sẽ chuẩn bị sẵn sàng hơn.",
 btn("Xem địa điểm","{P}location.html","btn-line") + btn("Tham gia Infinite","{P}contact.html"))

write("about.html","About — Infinite Maker Space",
 "Infinite Maker Space là cộng đồng maker tại TP. Hồ Chí Minh: sứ mệnh, giá trị, founder và core team.",
 about_body, "about.html")

# =============================================================== LOCATION
SPOTS = ["Ảnh: toàn cảnh xưởng nhìn từ cửa vào","Ảnh: khu 3D Print với hai máy Bambu Lab đang chạy",
 "Ảnh: khu Laser Cut, máy đang cắt","Ảnh: khu Cricut với máy in màu và giấy màu",
 "Ảnh: bàn làm việc dài với dụng cụ bày sẵn","Ảnh: kệ trưng bày sản phẩm đã làm tại xưởng",
 "Ảnh: team đang làm việc cùng nhau","Ảnh: một buổi workshop đông người"]

INFO = [("Địa chỉ","{{DIACHI}}"),("Giờ mở cửa","{{GIOMOCUA}}"),
 ("Zalo",'<a href="https://zalo.me/{{ZALO}}"><b>{{ZALO}}</b></a>'),
 ("Email",'<a href="mailto:{{EMAIL}}"><b>{{EMAIL}}</b></a>'),
 ("Đi lại","Có chỗ để xe máy trước cửa. Nếu đi ô tô, gửi xe ở bãi gần đó rồi đi bộ sang.")]

loc_body = crumb([("Home","{P}index.html"),("Location",None)]) + phero(
 "Location","Infinite Maker Space <span class='accent'>TP. Hồ Chí Minh</span>",
 "Một nơi để dựng, để thử, để làm chung và để tạo ra thứ gì đó có thật."
) + """
<section class="sec sec-t0"><div class="wrap">%s</div></section>
<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><span class="lab">Bên trong xưởng</span>
    <h2 class="d2 mb-s">Tám góc, một <span class="accent">xưởng</span>.</h2></div>
  <div class="gal">%s</div>
</div></section>
<section class="sec sec-t0"><div class="wrap">
  <div class="grid g2" style="align-items:start">
    <div class="rv"><span class="lab">Ghé thăm</span>
      <div class="info" style="margin-top:20px">%s</div>
      <div class="actions" style="margin-top:24px">%s</div></div>
    <div class="rv">%s</div>
  </div>
</div></section>
""" % (ph("Ảnh full-width: mặt tiền hoặc toàn cảnh không gian, chụp ngang", 1, "wide rv"),
 "".join(ph(c, i, "rv") for i, c in enumerate(SPOTS)),
 "".join('<div><span class="k">%s</span><span class="v">%s</span></div>' % kv for kv in INFO),
 btn("Chỉ đường","https://maps.google.com"),
 ph("Google Maps — dán mã iframe của Google Maps vào đây", 4, "rv").replace('class="ph','style="aspect-ratio:4/3;border-radius:var(--r-xl);box-shadow:var(--shadow-lift)" class="ph')
) + cta("Đến làm <span class='accent'>thứ gì đó</span>.",
 "Ghé xem không gian, thử một máy, hỏi bất cứ điều gì. Cửa mở cả tuần.",
 btn("Mở Google Maps","https://maps.google.com") + btn("Tham gia Maker Space","{P}contact.html","btn-line"))

write("location.html","Location — Infinite Maker Space TP. Hồ Chí Minh",
 "Địa chỉ, giờ mở cửa, chỗ để xe và cách đi tới Infinite Maker Space.", loc_body, "location.html")

# =============================================================== CONTACT
OPTS = ["Gói cơ bản — 450K/tháng","Gói Premium — 750K/tháng","Gói 3 tháng","Dự án in 3D",
 "Dự án cắt laser","Dự án thủ công giấy","Sản xuất số lượng lớn cho doanh nghiệp",
 "Đăng ký workshop","Tham quan không gian"]

contact_body = crumb([("Home","{P}index.html"),("Contact",None)]) + phero(
 "Contact","Cùng làm <span class='accent'>thứ gì đó</span>.",
 "Có một ý tưởng, một dự án, hay chỉ muốn ghé xem không gian? Nhắn cho Infinite."
) + """
<section class="sec sec-t0"><div class="wrap">
  <div class="grid g2">
    <div class="tile t-mint rv"><div class="tile__orb"></div><h3>Zalo</h3>
      <p>Cách nhanh nhất để hỏi về máy móc, giá vật liệu, lịch workshop hoặc đặt lịch tham quan.
      Thường phản hồi trong vài phút giờ hành chính.</p>
      <div style="margin-top:20px"><a class="btn btn-line" href="https://zalo.me/{{ZALO}}">Nhắn tin Zalo <span class="arrow">→</span></a></div></div>
    <div class="tile t-sky rv"><div class="tile__orb"></div><h3>Email</h3>
      <p>Có brief dự án hoặc file thiết kế? Gửi kèm số lượng và thời hạn mong muốn, chúng tôi báo giá trong vòng 24 giờ.</p>
      <div style="margin-top:20px"><a class="btn btn-line" href="mailto:{{EMAIL}}">Gửi email <span class="arrow">→</span></a></div></div>
  </div>
</div></section>

<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><h2 class="d2">Kể cho chúng tôi thứ bạn <span class="accent">muốn làm</span>.</h2></div>
  <form class="form rv" id="contactForm" style="max-width:760px">
    <div class="f2">
      <div class="field"><label for="ten">Họ và tên</label><input id="ten" name="ten" required></div>
      <div class="field"><label for="sdt">Số điện thoại</label><input id="sdt" name="sdt" type="tel" required></div>
    </div>
    <div class="field"><label for="qt">Bạn quan tâm đến</label>
      <select id="qt" name="qt">%s</select></div>
    <div class="field"><label for="mota">Mô tả dự án</label>
      <textarea id="mota" name="mota" placeholder="Bạn muốn làm gì? Kích thước, số lượng, thời hạn mong muốn…"></textarea></div>
    <div><button class="btn" type="submit">Gửi yêu cầu <span class="arrow">→</span></button></div>
    <p class="okmsg" id="formOk">Đã nhận yêu cầu — Infinite sẽ liên hệ lại trong vòng 24 giờ. Cảm ơn bạn!</p>
    <p class="formnote">Form demo — khi deploy hãy nối vào Netlify Forms, Formspree hoặc backend của bạn.</p>
  </form>
</div></section>
""" % "".join("<option>%s</option>" % o for o in OPTS) + cta(
 "Chưa biết bắt đầu <span class='accent'>từ đâu</span>?",
 "Nhắn một dòng mô tả ý tưởng. Team sẽ nói cho bạn biết nên dùng công nghệ nào, mất bao lâu và tốn khoảng bao nhiêu.",
 btn("Nhắn Zalo","https://zalo.me/{{ZALO}}") + btn("Xem bảng giá","{P}services.html#pricing","btn-line"))

write("contact.html","Contact — Infinite Maker Space",
 "Liên hệ Infinite Maker Space qua Zalo, email hoặc form. Đăng ký thành viên, đặt gia công, đăng ký workshop.",
 contact_body, "contact.html")

# =============================================================== NEWS
news_cards = "".join("""<a class="card rv" href="{P}news/article.html" data-cat="%s">
  <div class="ph ph-%s layerlines"><span class="ctag">%s</span><em>Ảnh minh hoạ bài viết</em></div>
  <div class="cbody"><h3>%s</h3><p>%s</p><span class="cgo">Bài mẫu · 5 phút đọc</span></div></a>""" % (
   cat, PAL[i % 6], catname, title, ex) for i, (title, cat, catname, ex) in enumerate(NEWS))

news_body = crumb([("Home","{P}index.html"),("News",None)]) + phero(
 "News","Blog &amp; <span class='accent'>câu chuyện</span>",
 "Kiến thức maker, nhật ký workshop và câu chuyện đằng sau những sản phẩm được làm tại Infinite."
) + """
<section class="sec sec-t0"><div class="wrap">
  <div class="filters rv" data-filterset="newsGrid">
    <button class="pf on" data-f="all">Tất cả</button><button class="pf" data-f="maker">Maker Space</button>
    <button class="pf" data-f="workshop">Workshop</button><button class="pf" data-f="sanpham">Sản phẩm</button>
  </div>
  <div class="grid g3" id="newsGrid">%s</div>
</div></section>
""" % news_cards + cta("Muốn ghé xem <span class='accent'>tận nơi</span>?",
 "Đọc thì hay, nhưng nghe tiếng máy chạy và cầm sản phẩm trên tay vẫn khác.",
 btn("Xem địa điểm","{P}location.html","btn-line") + btn("Bắt đầu dự án của bạn","{P}contact.html"))

write("news.html","Blog & câu chuyện — Infinite Maker Space",
 "Kiến thức maker, nhật ký workshop và câu chuyện sản phẩm từ Infinite Maker Space.", news_body, "news.html")

# =============================================================== NEWS ARTICLE
art_body = crumb([("Home","{P}index.html"),("News","{P}news.html"),("Bài viết mẫu",None)]) + """
<section class="phero"><div class="blob b1"></div><div class="blob b2"></div>
  <div class="wrap"><div class="phero__in">
    <span class="lab">Makerspace Stories</span>
    <h1 class="d1">What is a <span class="accent">makerspace</span>?</h1>
    <p class="lead">Makerspace là gì, vì sao mô hình này lan rộng, và một không gian như vậy thay đổi cách người trẻ học kỹ năng ra sao.</p>
    <p class="formnote" style="margin-top:18px">Infinite Studio · 5 phút đọc</p>
  </div></div>
</section>
<section class="sec sec-t0"><div class="wrap">%s</div></section>
<section class="sec sec-t0"><div class="wrap">
  <div class="prose rv">
    <div class="callout">Đây là bố cục mẫu cho một bài viết. Thay toàn bộ phần chữ bên dưới bằng nội dung thật của bạn,
    giữ nguyên các thẻ để định dạng không bị vỡ.</div>
    <p>Đoạn mở đầu nên trả lời thẳng câu hỏi trong tiêu đề trong vòng ba câu. Người đọc trên điện thoại thường
    quyết định đọc tiếp hay không trong mười giây đầu.</p>
    <h2>Makerspace khác gì một xưởng thông thường</h2>
    <div class="quote">“Một xưởng có máy. Một makerspace có máy, có người biết dùng máy, và có những người khác
    cũng đang làm dở một thứ gì đó ở bàn bên cạnh.”</div>
    <p>Viết tiếp phần thân bài ở đây. Chia thành các đoạn ngắn, mỗi đoạn một ý.</p>
    %s
    <h2>Bắt đầu từ đâu nếu bạn chưa biết gì</h2>
    <p>Đoạn này phù hợp để liệt kê các bước cụ thể:</p>
    <ul><li>Ghé xem không gian một buổi, không cần đăng ký trước</li>
    <li>Tham gia một workshop nhập môn để làm quen máy</li>
    <li>Bắt đầu dự án nhỏ đầu tiên, chấp nhận nó sẽ chưa đẹp</li>
    <li>Hỏi người ngồi cạnh — đó là phần giá trị nhất của makerspace</li></ul>
    <h2>Kết</h2>
    <p>Đoạn kết nên dẫn người đọc sang hành động tiếp theo: ghé xem không gian, đăng ký workshop, hoặc nhắn tin hỏi thêm.</p>
  </div>
</div></section>
<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><span class="lab">Related articles</span><h2 class="d2 mb-s">Đọc <span class="accent">tiếp</span>.</h2></div>
  <div class="grid g3">%s</div>
</div></section>
""" % (ph("Ảnh hero bài viết: toàn cảnh xưởng có người đang làm việc", 2, "wide rv"),
 ph("Ảnh minh hoạ trong bài: cận cảnh một công đoạn cụ thể", 5, "rv").replace('class="ph','style="aspect-ratio:16/9;border-radius:var(--r-lg);margin:26px 0" class="ph'),
 "".join("""<a class="card rv" href="{P}news/article.html">
  <div class="ph ph-%s layerlines"><span class="ctag">%s</span><em>Ảnh minh hoạ bài viết</em></div>
  <div class="cbody"><h3>%s</h3><p>%s</p><span class="cgo">Bài mẫu · 5 phút đọc</span></div></a>""" % r
  for r in [("mint","Makerspace Stories","Beginner’s Guide to 3D Printing","Mọi thứ người mới cần biết trước lần in đầu tiên."),
            ("bubble","Made at Infinite","How We Made a Miniature Dollhouse","Từ bản vẽ đến bộ nội thất tí hon hoàn chỉnh."),
            ("butter","Workshops","Lịch workshop tháng này","Các buổi học sắp mở và cách đăng ký.")])
) + cta("Visit <span class='accent'>Infinite Maker Space</span>.",
 "Đọc xong rồi thì ghé xem tận nơi. Cửa mở cả tuần, không cần hẹn trước.",
 btn("Xem địa điểm","{P}location.html","btn-line") + btn("Tham gia Infinite","{P}contact.html"))

write("news/article.html","What is a makerspace? — Infinite Maker Space",
 "Makerspace là gì, vì sao mô hình này lan rộng, và nó thay đổi cách người trẻ học kỹ năng ra sao.",
 art_body, "news.html")

# =============================================================== MAKERSPACE
MK = [
 dict(slug="3d-printing", nav="3D Print", h1="3D Print.",
  sub="Không gian dành cho prototype, sản phẩm sáng tạo, miniature, product design và sản xuất lô nhỏ. Máy luôn sẵn sàng, và luôn có người chỉ bạn cách dùng.",
  chips=["Prototype","Miniature","Thiết kế sản phẩm","Lô nhỏ","FDM"],
  toolslab="Máy trong khu vực", toolsh="Hai máy in, chạy gần như <span class='accent'>cả ngày</span>.",
  tools=[("Bambu Lab A1","Máy in FDM tốc độ cao, đổi màu tự động, phù hợp cho hầu hết dự án hằng ngày.",
          ["Prototype","Miniatur","Đồ trang trí","Chi tiết máy"],"Ảnh máy Bambu Lab A1 đang in"),
         ("Bambu Lab A2L","Khổ in lớn hơn, dành cho chi tiết to hoặc in nhiều sản phẩm cùng lúc.",
          ["Sản phẩm khổ lớn","Lô nhỏ","Vỏ hộp","Khuôn"],"Ảnh máy Bambu Lab A2L với bản in khổ lớn"),
         ("Khu hoàn thiện","Bàn gỡ support, chà nhám, sơn và lắp ráp — phần quyết định sản phẩm nhìn nghiệp dư hay chuyên nghiệp.",
          ["Gỡ support","Chà nhám","Sơn","Lắp ráp"],"Ảnh bàn hoàn thiện với dụng cụ chà nhám và sơn")],
  canlab="Có thể làm gì ở đây", canh="Bạn có thể in ra <span class='accent'>những gì</span>?",
  can=["Miniatures","Prototype","Product parts","Displays","Decor","Functional products","Custom projects"],
  flowh="Từ file đến sản phẩm <span class='accent'>cầm được trên tay</span>.",
  steps=["Ý tưởng","Dựng 3D","Slicing","In","Hoàn thiện","Thành phẩm"],
  projs=["miniatures","keycaps","desktop-lights","stem-kits","spider-enclosures"],
  ctah="Bắt đầu dự án in 3D <span class='accent'>của bạn</span>.",
  ctal="Mang theo file, hoặc chỉ mang theo ý tưởng. Team sẽ giúp bạn chọn vật liệu, thông số và cách in tiết kiệm nhất.",
  ctab="Bắt đầu dự án in 3D", hero="Ảnh: máy in 3D đang chạy, cận cảnh lớp nhựa đang hình thành"),

 dict(slug="laser-cutting", nav="Laser Cut", h1="Laser Cut.",
  sub="Biến thiết kế digital thành sản phẩm thật từ gỗ, acrylic và nhiều loại vật liệu phù hợp khác — chính xác tới từng milimet.",
  chips=["Gỗ","Mica","Khắc","DIY Kit","Biển hiệu"],
  toolslab="Máy trong khu vực", toolsh="Từ file trên máy tính thành <span class='accent'>vật cầm được</span>.",
  tools=[("Large-format Laser Cutter","Máy cắt khổ lớn, cắt và khắc được gỗ, acrylic, da, giấy dày và nhiều vật liệu khác.",
          ["Cắt","Khắc","Khổ lớn","Lô nhỏ"],"Ảnh máy cắt laser khổ lớn đang hoạt động"),
         ("Khu vực làm việc","Bàn chuẩn bị vật liệu, khu gỡ chi tiết và lắp ráp thử ngay sau khi cắt.",
          ["Bàn lắp ráp","Kho vật liệu","Hút khói"],"Ảnh bàn lắp ráp với các chi tiết vừa cắt"),
         ("Quá trình cắt","Xem tia laser chạy theo đường vector là phần thú vị nhất của quy trình.",
          ["Vector","Kerf","Nhiều lớp"],"Ảnh tia laser đang cắt tấm gỗ, khói mỏng bay lên")],
  canlab="Có thể làm gì ở đây", canh="Chúng tôi cắt ra <span class='accent'>những gì</span>.",
  can=["Book Nook","DIY Kit","Decor","Acrylic product","Signage","Prototype","Packaging component"],
  flowh="Từ bản vector đến <span class='accent'>bộ kit đóng hộp</span>.",
  steps=["Thiết kế","File vector","Cắt thử","Cắt chính","Lắp ráp","Đóng gói"],
  projs=["stem-kits","book-nook","laser-decor","spider-enclosures"],
  ctah="Bắt đầu dự án <span class='accent'>cắt laser</span>.",
  ctal="Gửi file vector hoặc bản phác thảo. Chúng tôi sẽ tư vấn vật liệu, độ dày và cách ghép mối phù hợp.",
  ctab="Bắt đầu dự án cắt laser", hero="Ảnh: tia laser đang cắt tấm gỗ, khói mỏng bay lên"),

 dict(slug="paper-craft", nav="Cricut & Thủ công giấy", h1="Cricut &amp; thủ công giấy.",
  sub="Cricut · Printing · Paper Making — không gian dành cho paper craft, sticker, packaging và các dự án DIY bằng giấy.",
  chips=["Cricut","Sticker","Bao bì","Mô hình giấy","Nhãn dán"],
  toolslab="Công cụ trong khu", toolsh="Ba công cụ, <span class='accent'>vô số cách dùng</span>.",
  tools=[("Color Printer","In màu chất lượng cao trên giấy, decal và vật liệu mỏng trước khi cắt.",
          ["Sticker in","Nhãn","Bản in thử","Giấy gói"],"Ảnh máy in màu đang in một tờ sticker"),
         ("Cricut Cutting Machine","Cắt chính xác các hình phức tạp trên giấy, decal, vinyl và vật liệu mỏng.",
          ["Sticker cắt hình","Chữ dán","Chi tiết nhỏ","Thiệp"],"Ảnh máy Cricut đang cắt một tấm decal"),
         ("Hand Tools","Dao trổ, thước, keo, dụng cụ gấp và bo góc — phần thủ công không máy nào thay được.",
          ["Gấp","Dán","Bo góc","Hoàn thiện"],"Ảnh bộ dụng cụ thủ công bày trên bàn gỗ")],
  canlab="Có thể làm gì ở đây", canh="Bạn có thể làm ra <span class='accent'>những gì</span>.",
  can=["Stickers","Cards","Packaging","Paper models","Paper decor","DIY craft","Labels","Custom creative projects"],
  flowh="Từ file thiết kế đến <span class='accent'>tấm sticker bóc được</span>.",
  steps=["Thiết kế","In màu","Cắt Cricut","Bóc &amp; gấp","Hoàn thiện"],
  projs=[], ctah="Bắt đầu <span class='accent'>làm thôi</span>.",
  ctal="Chỉ cần một file thiết kế và vài tờ giấy. Paper Craft Lab là nơi dễ bắt đầu nhất với người mới.",
  ctab="Bắt đầu dự án giấy", hero="Ảnh: một dự án paper craft đang được thực hiện trên bàn"),
]

BYSLUG = {p["slug"]: p for p in PROJECTS}

for mi, m in enumerate(MK):
    tools = "".join("""<article class="card rv"><div class="ph ph-%s layerlines"><em>%s</em></div>
      <div class="cbody"><h3>%s</h3><p>%s</p><div class="chips">%s</div></div></article>""" % (
        PAL[(mi * 2 + i) % 6], t[3], t[0], t[1], "".join('<span class="chipsm">%s</span>' % c for c in t[2]))
      for i, t in enumerate(m["tools"]))
    made = ""
    if m["projs"]:
        made = """<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><span class="lab">Made at Infinite</span>
    <h2 class="d2 mb-s">Đã làm ra bằng <span class="accent">chính khu này</span>.</h2></div>
  <div class="grid g4">%s</div></div></section>""" % "".join(
            pcard(BYSLUG[s], j) for j, s in enumerate(m["projs"]))
    body = crumb([("Home","{P}index.html"),("Maker Space",None),(m["nav"],None)]) + phero(
        "Maker Space", m["h1"], m["sub"],
        "".join('<span class="tagpill">%s</span>' % c for c in m["chips"])
    ) + """
<section class="sec sec-t0"><div class="wrap">%s</div></section>
<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><span class="lab">%s</span><h2 class="d2 mb-s">%s</h2></div>
  <div class="grid g3">%s</div></div></section>
<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><span class="lab">%s</span><h2 class="d2 mb-s">%s</h2></div>
  <div class="chips rv">%s</div></div></section>
<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><span class="lab">Quy trình</span><h2 class="d2 mb-s">%s</h2></div>
  %s</div></section>
%s""" % (ph(m["hero"], mi, "wide rv"), m["toolslab"], m["toolsh"], tools,
         m["canlab"], m["canh"],
         "".join('<span class="tagpill">%s</span>' % c for c in m["can"]),
         m["flowh"], flow(m["steps"]), made
    ) + cta(m["ctah"], m["ctal"],
            btn(m["ctab"], "{P}contact.html") + btn("Xem bảng giá", "{P}services.html#pricing", "btn-line"))
    write("makerspace/%s.html" % m["slug"], "%s — Infinite Maker Space" % m["nav"], m["sub"][:155],
          body, "")

# =============================================================== PROJECTS
for pi, p in enumerate(PROJECTS):
    others = [q for q in PROJECTS if q["slug"] != p["slug"]][:3]
    body = crumb([("Home","{P}index.html"),("Made at Infinite","{P}index.html#made"),(p["nav"],None)]) + phero(
        "Made at Infinite", p["h1"], p["sub"],
        '<span class="tagpill">%s</span>' % p["tag"]
    ) + """
<section class="sec sec-t0"><div class="wrap">%s</div></section>
<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><span class="lab">Quy trình</span><h2 class="d2 mb-s">%s</h2></div>
  %s
  <div class="grid g2" style="margin-top:44px">
    <div class="tile t-%s rv"><div class="tile__orb"></div><h3>Công nghệ sử dụng</h3>
      <div class="chips" style="margin-top:14px">%s</div></div>
    <div class="card rv" style="padding:30px"><h3>Câu chuyện sản phẩm</h3>
      <p style="margin-top:10px;color:var(--ink-60)">%s</p></div>
  </div>
</div></section>
<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><span class="lab">Gallery</span><h2 class="d2 mb-s">Hình ảnh <span class="accent">dự án</span>.</h2></div>
  %s
</div></section>
<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><span class="lab">Sản phẩm khác</span><h2 class="d2 mb-s">Xem <span class="accent">thêm</span>.</h2></div>
  <div class="grid g3">%s</div>
</div></section>
""" % (ph(p["hero"], pi, "wide rv"), p["flow"], flow(p["steps"]), PAL[pi % 6],
       "".join('<span class="chipsm">%s</span>' % t for t in p["tech"]), STORY,
       gallery(p["gal"], pi), "".join(pcard(q, j) for j, q in enumerate(others))
    ) + cta("Ý tưởng của bạn có thể là <span class='accent'>cái tiếp theo</span>.",
            "Mọi dự án ở trên đều bắt đầu từ một câu hỏi kiểu “làm cái này được không?”. Câu trả lời thường là được.",
            btn("Bắt đầu dự án của bạn","{P}contact.html") + btn("Xem dịch vụ","{P}services.html","btn-line"))
    write("projects/%s.html" % p["slug"], "%s — Made at Infinite" % p["nav"], p["blurb"][:155],
          body, "")

# =============================================================== WORKSHOPS
for wi, w in enumerate(WORKSHOPS):
    others = [x for x in WORKSHOPS if x["slug"] != w["slug"]][:3]
    rows = [("Chủ đề", w["cat"]), ("Trình độ", w["level"]), ("Lịch học", w["sched"]),
            ("Thời lượng", w["hours"]), ("Số người", "Tối đa " + w["cap"]),
            ("Học phí", "<b>%s</b>" % w["price"]), ("Địa điểm", "{{DIACHI}}"),
            ("Người hướng dẫn", "Tên người hướng dẫn"), ("Cần mang theo", BRING)]
    body = crumb([("Home","{P}index.html"),("Services","{P}services.html"),
                  ("Workshops","{P}services.html#workshops"),(w["title"],None)]) + phero(
        "Workshop", w["title"], w["desc"],
        '<span class="tagpill">%s</span><span class="tagpill">%s</span><span class="tagpill">%s</span><span class="tagpill">%s</span>'
        % (w["cat"], w["level"], w["hours"], "Tối đa " + w["cap"])
    ) + """
<section class="sec sec-t0"><div class="wrap">%s</div></section>
<section class="sec sec-t0"><div class="wrap">
  <div class="grid g2" style="align-items:start">
    <div class="rv">
      <span class="lab">Buổi học này</span>
      <h2 class="d2 mb-s">Bạn sẽ <span class="accent">làm ra</span>.</h2>
      <div class="tile t-mint" style="margin-top:20px;padding:26px 28px"><h3>%s</h3></div>
      <h3 style="margin-top:32px">Bạn sẽ học được</h3>
      <div class="prose" style="margin-top:14px"><ul>%s</ul></div>
      <div class="actions" style="margin-top:26px">%s</div>
      <p class="formnote" style="margin-top:14px">Học phí đã bao gồm toàn bộ vật liệu và sản phẩm bạn mang về.</p>
    </div>
    <div class="rv"><span class="lab">Thông tin lớp</span>
      <div class="info" style="margin-top:20px">%s</div></div>
  </div>
</div></section>
<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><span class="lab">Hình ảnh lớp học</span>
    <h2 class="d2 mb-s">Không khí <span class="accent">buổi học</span>.</h2></div>
  %s
</div></section>
<section class="sec sec-t0"><div class="wrap">
  <div class="sechead rv"><span class="lab">Workshop khác</span>
    <h2 class="d2 mb-s">Có thể bạn <span class="accent">cũng thích</span>.</h2></div>
  <div class="grid g3">%s</div>
  <div style="text-align:center;margin-top:36px">%s</div>
</div></section>
""" % (ph(w["hero"], wi, "wide rv"), w["make"],
       "".join("<li>%s</li>" % l for l in w["learn"]),
       btn("Đăng ký workshop","{P}contact.html"),
       "".join('<div><span class="k">%s</span><span class="v">%s</span></div>' % r for r in rows),
       gallery(WGAL, wi + 1),
       "".join(wcard(x) for x in others),
       btn("Xem tất cả workshop","{P}services.html#workshops","btn-line")
    ) + cta("Muốn mở lớp riêng <span class='accent'>cho nhóm</span>?",
            "Infinite nhận tổ chức workshop riêng cho lớp học, công ty hoặc nhóm bạn từ 6 người trở lên — nội dung điều chỉnh theo nhu cầu.",
            btn("Nhắn Zalo","https://zalo.me/{{ZALO}}") + btn("Gửi email","mailto:{{EMAIL}}","btn-line"))
    write("services/workshops/%s.html" % w["slug"], "%s — Workshop tại Infinite Maker Space" % w["title"],
          w["desc"][:155], body, "services.html")

# =============================================================== POLICIES
POLNAV = [(p["slug"], p["nav"]) for p in POLICIES] + [("faq", "Câu hỏi thường gặp")]

def polnav(cur):
    return '<div class="chips rv">%s</div>' % "".join(
        '<a class="tagpill" href="{P}policies/%s.html">%s →</a>' % (s, n)
        for s, n in POLNAV if s != cur)

POLCTA = cta("Còn thắc mắc <span class='accent'>gì khác</span>?",
    "Nhắn Zalo là nhanh nhất — thường có người trả lời trong vài phút vào giờ hành chính.",
    btn("Nhắn Zalo","https://zalo.me/{{ZALO}}") + btn("Gửi email","mailto:{{EMAIL}}","btn-line"))

for pol in POLICIES:
    secs = ""
    for h2, blocks in pol["secs"]:
        secs += "<h2>%s</h2>" % h2
        for kind, val in blocks:
            if kind == "p":
                secs += "<p>%s</p>" % val
            else:
                secs += "<ul>%s</ul>" % "".join("<li>%s</li>" % x for x in val)
    body = crumb([("Home","{P}index.html"),("Chính sách",None),(pol["nav"],None)]) + phero(
        "Chính sách", pol["h1"], pol["lead"]
    ) + """
<section class="sec sec-t0"><div class="wrap">
  <div class="prose rv">
    <div class="updated">%s</div>
    %s
    %s
  </div>
  <div style="margin-top:56px"><span class="lab">Các trang khác</span><div style="margin-top:14px">%s</div></div>
</div></section>
""" % (UPDATED, '<div class="callout">%s</div>' % pol["callout"] if pol["callout"] else "",
       secs, polnav(pol["slug"])) + POLCTA
    write("policies/%s.html" % pol["slug"], "%s — Infinite Maker Space" % pol["nav"],
          pol["lead"][:155], body, "")

# ---- FAQ ----
faq_body = crumb([("Home","{P}index.html"),("Chính sách",None),("Câu hỏi thường gặp",None)]) + phero(
 "Chính sách","Câu hỏi <span class='accent'>thường gặp</span>",
 "Những câu được hỏi nhiều nhất qua Zalo, gom lại một chỗ cho bạn đỡ phải nhắn."
) + """
<section class="sec sec-t0"><div class="wrap">
  <div class="updated rv">%s</div>
  <div class="prose rv" style="max-width:820px">%s</div>
  <div style="margin-top:56px"><span class="lab">Các trang khác</span><div style="margin-top:14px">%s</div></div>
</div></section>
""" % (UPDATED,
 "".join('<h2>%s</h2><p>%s</p>' % qa for qa in FAQ),
 polnav("faq")) + POLCTA
write("policies/faq.html","Câu hỏi thường gặp — Infinite Maker Space",
 "Những câu hỏi được hỏi nhiều nhất về Infinite Maker Space: thành viên, vật liệu, gia công, workshop.",
 faq_body, "")

# =============================================================== 404
nf = """<section class="phero"><div class="blob b1"></div><div class="blob b2"></div>
  <div class="wrap"><div class="phero__in">
    <span class="lab">404</span>
    <h1 class="d1">Trang này chưa <span class="accent">được dựng</span>.</h1>
    <p class="lead">Có thể đường dẫn bị gõ sai, hoặc trang đã được đổi tên. Thử quay lại trang chủ hoặc xem danh sách dịch vụ.</p>
    <div class="actions">%s%s</div>
  </div></div>
</section>""" % (btn("Về trang chủ","{P}index.html"), btn("Xem dịch vụ","{P}services.html","btn-line"))
write("404.html","404 — Infinite Maker Space","Không tìm thấy trang.", nf, "")

print("Đã sinh %d trang:" % len(PAGES))
for p in sorted(PAGES):
    print("  ", p)
