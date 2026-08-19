# Infinite Maker Space — website "Pastel Filament"

Website tĩnh 31 trang. **Nội dung, sơ đồ trang, cách dẫn link và cách vận hành copy nguyên từ bản mẫu**; chỉ màu sắc, typography và phong cách chuyển sang hệ pastel nhựa in 3D.

---

## Xem thử tại máy

Đường dẫn dùng kiểu không đuôi (`/services`, `/policies/faq`) đúng như bản mẫu, nên mở thẳng `index.html` bằng trình duyệt sẽ không click sang trang khác được. Chạy server kèm sẵn:

```bash
python3 serve.py
```

Rồi mở **http://localhost:8000** — mọi thứ hoạt động y như khi đã deploy. Ctrl+C để dừng.

## Deploy

Kéo cả thư mục thả vào Netlify. Không cần build, không cần cài gì. `netlify.toml` đã có sẵn.

Netlify tự phục vụ `services.html` tại `/services` (Pretty URLs, bật mặc định) — giống hệt bản mẫu.

> Nếu dùng host khác: cần bật tính năng "clean URLs / extensionless". Vercel và Cloudflare Pages có sẵn. GitHub Pages **không** có — với GitHub Pages thì phải đổi link sang dạng `.html`.

### Trước khi công bố

**1. Tên miền** — trong `sitemap.xml` và `robots.txt`, thay `TEN-MIEN-CUA-BAN` bằng tên miền thật.

**2. Thông tin liên hệ** — tìm và thay trong toàn bộ file `.html`:

| Placeholder | Thay bằng |
|---|---|
| `{{DIACHI}}` | địa chỉ xưởng |
| `{{GIOMOCUA}}` | giờ mở cửa |
| `{{ZALO}}` | số Zalo (dùng cho cả link `zalo.me/...`) |
| `{{EMAIL}}` | email liên hệ |
| `{{FACEBOOK}}` `{{SHOPEE}}` `{{TIKTOK}}` | link mạng xã hội |

```bash
# macOS
grep -rl '{{ZALO}}' . --include='*.html' | xargs sed -i '' 's|{{ZALO}}|0901234567|g'
# Linux
grep -rl '{{ZALO}}' . --include='*.html' | xargs sed -i 's|{{ZALO}}|0901234567|g'
```

**3. Form liên hệ** — `contact.html` đang là form demo (chỉ hiện lời cảm ơn). Để nhận thư thật, thêm thuộc tính `netlify` vào thẻ `<form>`, hoặc trỏ `action` sang Formspree/backend của bạn.

---

## Sơ đồ trang — 31 URL, giống hệt bản mẫu

```
/                                Trang chủ
├── /services                    Dịch vụ · Bảng giá · Workshop
│   ├── #pricing #workshops #business        (neo trong trang)
│   └── /services/workshops/     8 lớp: nhap-mon-in-3d · ban-in-dau-tien ·
│                                dung-hinh-3d-cho-nguoi-moi · nhap-mon-thiet-ke-san-pham ·
│                                cat-laser-101 · thiet-ke-du-an-laser-dau-tien ·
│                                workshop-cricut · mo-hinh-giay
├── /about                       Sứ mệnh · 5 câu dẫn đường · founder · giá trị · team
├── /location                    Địa chỉ · giờ mở cửa · 8 góc xưởng
├── /news                        Blog (lọc 3 chủ đề)
│   └── /news/article            Bố cục bài viết mẫu
├── /contact                     Liên hệ + form
├── /makerspace/                 3d-printing · laser-cutting · paper-craft
├── /projects/                   miniatures · keycaps · desktop-lights · stem-kits ·
│                                book-nook · laser-decor · spider-enclosures
└── /policies/                   an-toan · thanh-vien · doi-tra · bao-mat · dieu-khoan · faq
```

Ngoài ra: `404.html`, `sitemap.xml`, `robots.txt`, `favicon.svg`.

**Cách dẫn link:** link trong trang viết KHÔNG đuôi (`/services`), `sitemap.xml` khai báo CÓ đuôi (`/services.html`) — copy đúng quy ước của bản mẫu.

## Vận hành

| Chức năng | Ở đâu |
|---|---|
| Header dính, mờ nền khi cuộn | mọi trang |
| Menu mobile (nút ☰) | mọi trang, dưới 1080px |
| Thanh Zalo/Join cố định đáy | mọi trang, dưới 680px |
| Chữ chạy ngang (marquee) | trang chủ, 2 dải |
| Đếm số khi cuộn tới | trang chủ, mục Numbers |
| Lọc thẻ theo chủ đề | trang chủ (sản phẩm), /news (bài viết) |
| Hiện dần khi cuộn | mọi trang |
| Neo trong trang | `#space` `#made` `#pricing` `#workshops` `#business` |
| Form liên hệ | /contact |
| Trang 404 | mọi URL không tồn tại |

## Hệ thiết kế

| Token | Màu | | Token | Màu |
|---|---|---|---|---|
| `--mint` | `#B9EBD8` | | `--bubble` | `#FFC7DD` |
| `--sky` | `#BCDFFA` | | `--cream` | `#FFFBF4` (nền) |
| `--lilac` | `#D5C9F7` | | `--ink` | `#2A2340` (chữ) |
| `--peach` | `#FFC9B4` | | `--butter` | `#FFE7AE` |

- Font: **Bricolage Grotesque** (tiêu đề) + **Be Vietnam Pro** (nội dung) — cả hai có đủ bộ ký tự tiếng Việt.
- `.layerlines` — sọc ngang rất mờ, mô phỏng đường in của máy in FDM.
- Nút bấm có cạnh dày `box-shadow 0 5px 0`, nhấn xuống thì lún như khối nhựa đúc.
- **Đổi màu toàn site:** sửa biến trong `:root` ở đầu `assets/ib.css` — một chỗ, cả 31 trang đổi theo.

## Ảnh

Bản mẫu không dùng file ảnh nào — mỗi chỗ cần ảnh là một ô pastel kèm chú thích mô tả nên chụp gì. Bản này giữ đúng như vậy. Khi có ảnh thật, thay `<div class="ph ...">…</div>` bằng `<img src="..." alt="...">`.

## Đã kiểm tra

- Bấm link duyệt hết **31/31 URL** — tất cả trả 200, CSS nạp đủ, không tràn ngang
- **1.544** link và asset nội bộ — không có link chết, không thiếu anchor
- 3 khổ màn hình 1440 / 768 / 390px
- Menu mobile, đếm số, 2 bộ lọc, neo trong trang, form, header dính, trang 404 — chạy đúng
- Có hỗ trợ `prefers-reduced-motion`
