#!/usr/bin/env python3
"""
Server xem thử tại máy — bắt chước Pretty URLs của Netlify.

Website này dùng đường dẫn không đuôi (/services, /policies/faq) đúng như bản mẫu,
nên mở thẳng file index.html bằng trình duyệt sẽ không click sang trang khác được.
Chạy file này thì mọi thứ hoạt động y như khi đã deploy.

    python3 serve.py

Rồi mở http://localhost:8000
"""
import http.server
import os
import socketserver

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))


class PrettyURLHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def translate_path(self, path):
        p = super().translate_path(path)
        # Thứ tự giống Netlify: file .html được ưu tiên hơn thư mục cùng tên.
        # (site có cả services.html lẫn thư mục services/, cả news.html lẫn news/)
        if os.path.isfile(p):
            return p
        if not p.endswith(".html") and os.path.isfile(p + ".html"):
            return p + ".html"
        if os.path.isdir(p):
            index = os.path.join(p, "index.html")
            if os.path.isfile(index):
                return index
        return p

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            page = os.path.join(ROOT, "404.html")
            if os.path.exists(page):
                body = open(page, "rb").read()
                self.send_response(404)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
        super().send_error(code, message, explain)

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), PrettyURLHandler) as httpd:
        print("Infinite Maker Space đang chạy tại  http://localhost:%d" % PORT)
        print("Nhấn Ctrl+C để dừng.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nĐã dừng.")
