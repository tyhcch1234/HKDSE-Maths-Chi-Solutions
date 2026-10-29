(function () {
  var sols = Array.prototype.slice.call(document.querySelectorAll('.q__sol'));
  var total = sols.length;
  var fill = document.getElementById('pfill');
  var label = document.getElementById('ptext');

  function opened() { return sols.filter(function (s) { return !s.hasAttribute('hidden'); }).length; }

  function refresh() {
    var n = opened();
    if (fill) fill.style.width = (total ? (n / total * 100) : 0) + '%';
    if (label) label.textContent = '已展開 ' + n + ' / ' + total + ' 題';
  }

  function typeset(el, done) {
    if (window.MathJax && window.MathJax.typesetPromise) {
      el.classList.remove('tex2jax_ignore');
      window.MathJax.typesetPromise([el]).then(done).catch(done);
    } else if (done) { done(); }
  }

  document.querySelectorAll('.q__toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var sol = document.getElementById(btn.dataset.target);
      var open = btn.getAttribute('aria-expanded') === 'true';
      if (open) {
        sol.setAttribute('hidden', '');
        btn.setAttribute('aria-expanded', 'false');
        btn.textContent = '顯示答案及詳解';
        refresh();
      } else {
        sol.removeAttribute('hidden');
        btn.setAttribute('aria-expanded', 'true');
        btn.textContent = '收起詳解';
        typeset(sol, refresh);
      }
    });
  });

  var allBtn = document.getElementById('expandAll');
  var closeBtn = document.getElementById('collapseAll');
  if (allBtn) allBtn.addEventListener('click', function () {
    var pending = [];
    sols.forEach(function (sol) {
      if (sol.hasAttribute('hidden')) {
        sol.removeAttribute('hidden');
        var b = document.querySelector('.q__toggle[data-target="' + sol.id + '"]');
        if (b) { b.setAttribute('aria-expanded', 'true'); b.textContent = '收起詳解'; }
        sol.classList.remove('tex2jax_ignore');
        pending.push(sol);
      }
    });
    if (window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise(pending).then(refresh).catch(refresh);
    } else { refresh(); }
  });
  if (closeBtn) closeBtn.addEventListener('click', function () {
    sols.forEach(function (sol) {
      sol.setAttribute('hidden', '');
      var b = document.querySelector('.q__toggle[data-target="' + sol.id + '"]');
      if (b) { b.setAttribute('aria-expanded', 'false'); b.textContent = '顯示答案及詳解'; }
    });
    refresh();
  });

  window.addEventListener('beforeprint', function () {
    if (allBtn) allBtn.click();
  });

  refresh();

  var links = Array.prototype.slice.call(document.querySelectorAll('.typebar a[data-t]'));
  var secs = links.map(function (a) { return document.getElementById(a.dataset.t); });
  function sync() {
    var y = window.scrollY + 140, idx = 0;
    secs.forEach(function (s, i) { if (s && s.offsetTop <= y) idx = i; });
    links.forEach(function (a, i) { a.classList.toggle('active', i === idx); });
  }
  window.addEventListener('scroll', sync, { passive: true });
  sync();
})();
