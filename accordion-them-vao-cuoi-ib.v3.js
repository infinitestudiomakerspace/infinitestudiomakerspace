
/* === BEGIN ACCORDION V2 =====================================
   Chỉ một mục được mở tại một thời điểm.
   - Mở mục khác  -> mục đang mở đóng lại VÀ đóng luôn mọi mục con
                     bên trong nó (vd: các câu hỏi trong "Câu hỏi thường gặp")
   - Áp dụng cho cả khối .acc (trang chính sách) và .faq (danh sách câu hỏi)
   - Sau khi mở, tự cuộn mục vừa mở vào tầm nhìn nếu nó bị trôi khỏi màn hình
   Nếu bạn đã dán bản cũ trước đó: XOÁ bản cũ đi, chỉ giữ đoạn này.
   ============================================================ */
(function () {
  function closeInside(el) {
    el.querySelectorAll('details[open]').forEach(function (d) { d.open = false; });
  }

  function headerOffset() {
    var h = document.querySelector('header') || document.querySelector('.hdr');
    return (h ? h.getBoundingClientRect().height : 0) + 14;
  }

  function ensureVisible(d) {
    requestAnimationFrame(function () {
      var s = d.querySelector('summary');
      if (!s) return;
      var off = headerOffset();
      var top = s.getBoundingClientRect().top;
      if (top < off || top > window.innerHeight - 80) {
        window.scrollTo({
          top: top + window.pageYOffset - off,
          behavior: 'smooth'
        });
      }
    });
  }

  document.querySelectorAll('.acc, .faq').forEach(function (group) {
    var items = group.querySelectorAll(':scope > details');
    items.forEach(function (d) {
      d.addEventListener('toggle', function () {
        if (d.open) {
          items.forEach(function (o) {
            if (o !== d && o.open) { closeInside(o); o.open = false; }
          });
          ensureVisible(d);
        } else {
          closeInside(d);
        }
      });
    });
  });
})();
/* === END ACCORDION V2 ====================================== */
