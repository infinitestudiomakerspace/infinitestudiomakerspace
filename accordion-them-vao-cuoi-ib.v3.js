
/* ============================================================
   Accordion: mở mục này thì mục đang mở tự đóng lại
   Dán TOÀN BỘ đoạn dưới vào CUỐI file assets/ib.v3.js
   Muốn áp dụng cho cả trang FAQ: đổi '.acc' thành '.acc, .faq'
   ============================================================ */
document.querySelectorAll('.acc').forEach(function (acc) {
  acc.querySelectorAll(':scope > details').forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (!d.open) return;
      acc.querySelectorAll(':scope > details[open]').forEach(function (o) {
        if (o !== d) o.open = false;
      });
    });
  });
});
