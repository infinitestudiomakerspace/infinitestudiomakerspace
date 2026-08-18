/* ==========================================================================
   INFINITE MAKER SPACE — tương tác (gọn nhẹ, không thư viện ngoài)
   ========================================================================== */
(function () {
  'use strict';
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return [].slice.call((c || document).querySelectorAll(s)); };

  /* ---------- năm hiện tại ---------- */
  $$('.js-year').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- header ---------- */
  var hdr = $('header'), last = 0;
  addEventListener('scroll', function () {
    var y = scrollY;
    if (hdr) {
      hdr.classList.toggle('solid', y > 24);
      hdr.classList.toggle('hide',
        y > last && y > 420 && !document.body.classList.contains('menu-open'));
    }
    last = y;
  }, { passive: true });

  /* ---------- menu mobile ---------- */
  var burger = $('.burger');
  if (burger) {
    burger.addEventListener('click', function () {
      document.body.classList.toggle('menu-open');
    });
    $$('.mobmenu a').forEach(function (a) {
      a.addEventListener('click', function () { document.body.classList.remove('menu-open'); });
    });
  }

  /* ---------- ngôi nhà: các phòng sáng dần ---------- */
  var house = $('.house');
  if (house) {
    var rooms = $$('.room', house);
    var light = function () {
      rooms.forEach(function (r, i) {
        setTimeout(function () { r.classList.add('lit'); }, reduce ? 0 : 260 + i * 190);
      });
    };
    if ('IntersectionObserver' in window && !reduce) {
      var hio = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { light(); hio.disconnect(); } });
      }, { threshold: 0.3 });
      hio.observe(house);
    } else {
      light();
    }
  }

  /* ---------- đếm số ---------- */
  var counters = $$('[data-count]');
  if (counters.length && 'IntersectionObserver' in window) {
    var run = function (el) {
      var target = parseFloat(el.getAttribute('data-count'));
      var suffix = el.getAttribute('data-suffix') || '';
      if (reduce) { el.textContent = target.toLocaleString('en-US') + suffix; return; }
      var dur = 1300, t0 = null;
      var step = function (t) {
        if (!t0) t0 = t;
        var k = Math.min(1, (t - t0) / dur);
        var v = Math.round(target * (1 - Math.pow(1 - k, 3)));
        el.textContent = v.toLocaleString('en-US') + suffix;
        if (k < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };
    var cio = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { run(e.target); cio.unobserve(e.target); }
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* ---------- lọc danh mục ---------- */
  $$('.pfilter[data-target]').forEach(function (bar) {
    var box = $(bar.getAttribute('data-target'));
    if (!box) return;
    var items = $$('[data-cat]', box);
    var buttons = $$('.pf', bar);
    buttons.forEach(function (b) {
      b.addEventListener('click', function () {
        var f = b.getAttribute('data-f');
        buttons.forEach(function (x) { x.classList.toggle('on', x === b); });
        items.forEach(function (c) {
          var show = f === 'all' || (c.getAttribute('data-cat') || '').indexOf(f) > -1;
          c.classList.toggle('out', !show);
          if (show) c.classList.add('in');
        });
      });
    });
  });

  /* làm mờ thẻ khác khi rê chuột */
  $$('.pgrid,.posts').forEach(function (g) {
    g.addEventListener('mouseover', function () { g.classList.add('hov'); });
    g.addEventListener('mouseleave', function () { g.classList.remove('hov'); });
  });

  /* ---------- reveal ---------- */
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });
    $$('.rv').forEach(function (el, i) {
      el.style.transitionDelay = (i % 4) * 65 + 'ms';
      io.observe(el);
    });
  } else {
    $$('.rv').forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------------------------------------------------------------
     FORM LIÊN HỆ
     Mặc định: mở ứng dụng email với nội dung điền sẵn.
     Muốn nhận thẳng vào hộp thư:
       1. Đăng ký https://formspree.io, tạo form, lấy mã dạng xyzabcd
       2. Thêm vào thẻ <form>:  action="https://formspree.io/f/xyzabcd" method="POST"
  --------------------------------------------------------------- */
  $$('form[data-mailto]').forEach(function (frm) {
    frm.addEventListener('submit', function (ev) {
      if (frm.getAttribute('action')) return;
      ev.preventDefault();
      var lines = [];
      new FormData(frm).forEach(function (v, k) { lines.push(k + ': ' + v); });
      location.href = 'mailto:' + frm.getAttribute('data-mailto') +
        '?subject=' + encodeURIComponent('[Website] ' + (frm.getAttribute('data-subject') || 'Liên hệ')) +
        '&body=' + encodeURIComponent(lines.join('\n'));
    });
  });
})();
