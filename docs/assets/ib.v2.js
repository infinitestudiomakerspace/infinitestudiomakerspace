/* Infinite Maker Space — script dùng chung cho toàn site */
(function () {
  'use strict';

  /* ---------- header dính ---------- */
  var hd = document.querySelector('header');
  if (hd) addEventListener('scroll', function () {
    hd.classList.toggle('stuck', scrollY > 20);
  }, { passive: true });

  /* ---------- menu mobile ---------- */
  var burger = document.getElementById('burger');
  var mobmenu = document.getElementById('mobmenu');
  if (burger && mobmenu) {
    burger.addEventListener('click', function () { mobmenu.classList.toggle('open'); });
    mobmenu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') mobmenu.classList.remove('open');
    });
  }

  /* ---------- reveal khi cuộn ---------- */
  var rv = document.querySelectorAll('.rv');
  if (rv.length) {
    if (!('IntersectionObserver' in window)) {
      rv.forEach(function (el) { el.classList.add('in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e, k) {
          if (!e.isIntersecting) return;
          setTimeout(function () { e.target.classList.add('in'); }, k * 70);
          io.unobserve(e.target);
        });
      }, { threshold: .12, rootMargin: '0px 0px -40px' });
      rv.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---------- đếm số ---------- */
  var nums = document.querySelectorAll('.num[data-count]');
  if (nums.length && 'IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, to = +el.dataset.count, t0 = performance.now(), dur = 1400;
        (function tick(now) {
          var p = Math.min(1, (now - t0) / dur);
          el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3))).toLocaleString('vi-VN');
          if (p < 1) requestAnimationFrame(tick);
        })(t0);
        cio.unobserve(el);
      });
    }, { threshold: .5 });
    nums.forEach(function (el) { cio.observe(el); });
  }

  /* ---------- bộ lọc thẻ ---------- */
  document.querySelectorAll('[data-filterset]').forEach(function (set) {
    var btns = set.querySelectorAll('.pf');
    var grid = document.getElementById(set.dataset.filterset);
    if (!grid) return;
    var cards = grid.querySelectorAll('[data-cat]');
    btns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        btns.forEach(function (b) { b.classList.remove('on'); });
        btn.classList.add('on');
        var f = btn.dataset.f;
        cards.forEach(function (c) {
          var show = f === 'all' || (c.dataset.cat || '').split(' ').indexOf(f) > -1;
          c.classList.toggle('hide', !show);
        });
      });
    });
  });

  /* ---------- form liên hệ (demo, chưa nối backend) ---------- */
  var form = document.getElementById('contactForm');
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    var ok = document.getElementById('formOk');
    if (ok) ok.classList.add('show');
    form.reset();
  });

  /* ---------- năm hiện tại ---------- */
  document.querySelectorAll('.js-year').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
