/* Juros, convenção e dívida no Brasil: navegação, tema, fórmulas e gráficos SVG.
   Gráficos desenhados a partir do JSON embutido em cada <figure>; tabela de dados fica
   como alternativa sem JavaScript. Motor inspirado no painel Alarmismo × Fatos. */
(function () {
  "use strict";

  /* tema e menu --------------------------------------------------------- */
  var root = document.documentElement;
  var bt = document.querySelector(".btn-tema");
  if (bt) bt.addEventListener("click", function () {
    var atual = root.getAttribute("data-theme");
    if (!atual) atual = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    var novo = atual === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", novo);
    try { localStorage.setItem("tema", novo); } catch (e) {}
    redesenhar();
  });
  var bm = document.querySelector(".btn-menu");
  if (bm) bm.addEventListener("click", function () {
    var ab = document.body.classList.toggle("menu-aberto");
    bm.setAttribute("aria-expanded", ab ? "true" : "false");
  });
  document.addEventListener("click", function (ev) {
    if (!document.body.classList.contains("menu-aberto")) return;
    if (ev.target.closest(".lateral") || ev.target.closest(".btn-menu")) return;
    document.body.classList.remove("menu-aberto");
    if (bm) bm.setAttribute("aria-expanded", "false");
  });
  var at = document.querySelector(".arvore a.atual");
  if (at && at.scrollIntoView) { try { at.scrollIntoView({ block: "center" }); } catch (e) {} }

  /* fórmulas -------------------------------------------------------------- */
  function renderMath() {
    if (!window.katex) return;
    document.querySelectorAll(".math").forEach(function (el) {
      if (el.classList.contains("katex-ok")) return;
      var tex = el.textContent;
      try {
        window.katex.render(tex, el, { displayMode: el.getAttribute("data-display") === "1", throwOnError: false });
        el.classList.add("katex-ok");
      } catch (e) { /* mantém o TeX legível */ }
    });
  }

  /* utilidades ------------------------------------------------------------ */
  var NS = "http://www.w3.org/2000/svg";
  function svg(tag, attrs, txt) {
    var n = document.createElementNS(NS, tag);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (txt != null) n.textContent = txt;
    return n;
  }
  function el(tag, cls, txt) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (txt != null) n.textContent = txt;
    return n;
  }
  function cor(i) {
    return getComputedStyle(root).getPropertyValue("--s" + ((i % 8) + 1)).trim() || "#2a78d6";
  }
  function fmt(v) {
    if (v == null || isNaN(v)) return "–";
    var a = Math.abs(v);
    var dec = a >= 1000 ? 0 : a >= 100 ? 1 : a >= 10 ? 1 : 2;
    return v.toLocaleString("pt-BR", { maximumFractionDigits: dec });
  }
  function toX(t) {
    var s = String(t);
    var m = s.match(/^(\d{4})-?(?:T|Q)([1-4])/);
    if (m) return +m[1] + (+m[2] - 0.5) / 4;
    m = s.match(/^(\d{4})(?:-(\d{1,2}))?(?:-(\d{1,2}))?/);
    if (!m) return NaN;
    var y = +m[1];
    if (!m[2]) return y + 0.5;
    var mo = +m[2];
    if (!m[3]) return y + (mo - 0.5) / 12;
    return y + (mo - 1) / 12 + (+m[3] - 1) / 365;
  }
  function nice(min, max, n) {
    if (min === max) { min -= 1; max += 1; }
    var span = max - min, step = Math.pow(10, Math.floor(Math.log10(span / n)));
    var err = span / n / step;
    if (err >= 7.5) step *= 10; else if (err >= 3.5) step *= 5; else if (err >= 1.5) step *= 2;
    var lo = Math.floor(min / step) * step, hi = Math.ceil(max / step) * step;
    var ticks = [];
    for (var v = lo; v <= hi + step / 2; v += step) ticks.push(Math.round(v / step) * step);
    return { lo: lo, hi: hi, ticks: ticks };
  }
  var GOVERNOS = [
    { de: 1985.2, ate: 1990.2, nome: "Sarney" },
    { de: 1990.2, ate: 1992.75, nome: "Collor" },
    { de: 1992.75, ate: 1995, nome: "Itamar" },
    { de: 1995, ate: 2003, nome: "FHC" },
    { de: 2003, ate: 2011, nome: "Lula 1–2" },
    { de: 2011, ate: 2016.37, nome: "Dilma" },
    { de: 2016.37, ate: 2019, nome: "Temer" },
    { de: 2019, ate: 2023, nome: "Bolsonaro" },
    { de: 2023, ate: 2027, nome: "Lula 3" }
  ];

  /* tooltip --------------------------------------------------------------- */
  function tooltip(area) {
    var tip = area.querySelector(".g-tip");
    if (!tip) { tip = el("div", "g-tip"); area.appendChild(tip); }
    return {
      show: function (html, x, y) {
        tip.innerHTML = html; tip.style.display = "block";
        var w = area.clientWidth, tw = tip.offsetWidth;
        var left = x + 12; if (left + tw > w) left = Math.max(0, x - tw - 12);
        tip.style.left = left + "px"; tip.style.top = Math.max(0, y - 10) + "px";
      },
      hide: function () { tip.style.display = "none"; }
    };
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function legenda(area, series) {
    if (series.length < 2) return;
    var lg = el("div", "g-legenda");
    series.forEach(function (s, i) {
      var sp = el("span"); var sw = el("i"); sw.style.background = cor(i);
      sp.appendChild(sw); sp.appendChild(document.createTextNode(s.nome)); lg.appendChild(sp);
    });
    area.appendChild(lg);
  }

  /* gráfico de linha ------------------------------------------------------- */
  function linha(area, spec, W) {
    var series = spec.series.map(function (s) {
      return { nome: s.nome, pts: (s.pontos || []).map(function (p) { return { x: toX(p.t), v: p.v, t: p.t }; })
        .filter(function (p) { return !isNaN(p.x); }).sort(function (a, b) { return a.x - b.x; }) };
    });
    var xs = [], vs = [];
    series.forEach(function (s) { s.pts.forEach(function (p) { xs.push(p.x); if (p.v != null) vs.push(p.v); }); });
    (spec.ref || []).forEach(function (r) { vs.push(r.v); });
    if (!xs.length) return;
    var x0 = Math.min.apply(null, xs), x1 = Math.max.apply(null, xs);
    if (x1 - x0 < 0.5) { x0 -= 0.5; x1 += 0.5; }
    var vmin = Math.min.apply(null, vs), vmax = Math.max.apply(null, vs);
    if (vmin > 0 && vmin < (vmax - vmin) * 0.6) vmin = 0;
    var ny = nice(vmin, vmax, W < 480 ? 4 : 6);
    var H = W < 480 ? 240 : 300, mL = 44, mR = 14, mT = spec.governos ? 22 : 10, mB = 28;
    var pw = W - mL - mR, ph = H - mT - mB;
    function X(x) { return mL + (x - x0) / (x1 - x0) * pw; }
    function Y(v) { return mT + (1 - (v - ny.lo) / (ny.hi - ny.lo)) * ph; }
    var s = svg("svg", { viewBox: "0 0 " + W + " " + H, width: W, height: H });
    if (spec.governos) {
      GOVERNOS.forEach(function (g, i) {
        var a = Math.max(g.de, x0), b = Math.min(g.ate, x1);
        if (b <= a) return;
        s.appendChild(svg("rect", { x: X(a), y: mT, width: X(b) - X(a), height: ph, "class": i % 2 ? "band-a" : "band-b" }));
        if (X(b) - X(a) > g.nome.length * 6 + 4)
          s.appendChild(svg("text", { x: (X(a) + X(b)) / 2, y: mT - 6, "text-anchor": "middle", "class": "band-t" }, g.nome));
      });
    }
    ny.ticks.forEach(function (t) {
      s.appendChild(svg("line", { x1: mL, x2: W - mR, y1: Y(t), y2: Y(t), "class": t === 0 ? "zero" : "gl" }));
      s.appendChild(svg("text", { x: mL - 6, y: Y(t) + 4, "text-anchor": "end", "class": "ax" }, fmt(t)));
    });
    var span = x1 - x0, passo = span <= 3 ? 0.5 : span <= 8 ? 1 : span <= 16 ? 2 : span <= 40 ? 5 : 10;
    if (W < 480 && span > 8) passo *= 2;
    var mostraMes = passo < 1;
    for (var xt = Math.ceil(x0 / passo) * passo; xt <= x1 + 1e-9; xt += passo) {
      var lab = mostraMes ? (Math.floor(xt) + (xt % 1 ? "/07" : "")) : String(Math.floor(xt));
      s.appendChild(svg("line", { x1: X(xt), x2: X(xt), y1: mT + ph, y2: mT + ph + 4, "class": "gl" }));
      s.appendChild(svg("text", { x: X(xt), y: H - 8, "text-anchor": "middle", "class": "ax" }, lab));
    }
    (spec.ref || []).forEach(function (r) {
      s.appendChild(svg("line", { x1: mL, x2: W - mR, y1: Y(r.v), y2: Y(r.v), "class": "refl" }));
      if (r.rotulo) s.appendChild(svg("text", { x: W - mR - 2, y: Y(r.v) - 4, "text-anchor": "end", "class": "refl-t" }, r.rotulo));
    });
    series.forEach(function (se, i) {
      var d = "", pen = false;
      se.pts.forEach(function (p) {
        if (p.v == null) { pen = false; return; }
        d += (pen ? "L" : "M") + X(p.x).toFixed(1) + " " + Y(p.v).toFixed(1); pen = true;
      });
      s.appendChild(svg("path", { d: d, fill: "none", stroke: cor(i), "stroke-width": 2, "stroke-linejoin": "round", "stroke-linecap": "round" }));
      var poucos = se.pts.length <= 40;
      se.pts.forEach(function (p) {
        if (p.v == null || !poucos) return;
        s.appendChild(svg("circle", { cx: X(p.x), cy: Y(p.v), r: se.pts.length <= 14 ? 3.5 : 2.2, fill: cor(i), stroke: "var(--surface)", "stroke-width": 1.5 }));
      });
    });
    var cross = svg("line", { x1: 0, x2: 0, y1: mT, y2: mT + ph, "class": "cross", visibility: "hidden" });
    s.appendChild(cross);
    var hit = svg("rect", { x: mL, y: mT, width: pw, height: ph, fill: "transparent" });
    s.appendChild(hit);
    legenda(area, series);
    area.appendChild(s);
    var tip = tooltip(area);
    function mover(ev) {
      var r = s.getBoundingClientRect(), esc_ = W / r.width;
      var px = ((ev.touches ? ev.touches[0].clientX : ev.clientX) - r.left) * esc_;
      var xv = x0 + (px - mL) / pw * (x1 - x0);
      var linhas = [], melhorX = null, tlab = null;
      series.forEach(function (se, i) {
        var best = null;
        se.pts.forEach(function (p) { if (p.v != null && (best === null || Math.abs(p.x - xv) < Math.abs(best.x - xv))) best = p; });
        if (!best) return;
        if (melhorX === null || Math.abs(best.x - xv) < Math.abs(melhorX - xv)) { melhorX = best.x; tlab = best.t; }
        linhas.push({ i: i, p: best, nome: se.nome });
      });
      if (melhorX === null) return;
      var html = "<b>" + esc(tlab) + "</b>";
      linhas.forEach(function (l) {
        if (Math.abs(l.p.x - melhorX) > (x1 - x0) / 25) return;
        html += "<br><i style=\"background:" + cor(l.i) + "\"></i>" + (series.length > 1 ? esc(l.nome) + ": " : "") + fmt(l.p.v) + (spec.unidade ? " " + esc(spec.unidade) : "");
      });
      cross.setAttribute("x1", X(melhorX)); cross.setAttribute("x2", X(melhorX)); cross.setAttribute("visibility", "visible");
      tip.show(html, X(melhorX) / esc_, mT / esc_ + 20);
    }
    hit.addEventListener("mousemove", mover);
    hit.addEventListener("touchstart", mover, { passive: true });
    hit.addEventListener("mouseleave", function () { tip.hide(); cross.setAttribute("visibility", "hidden"); });
  }

  /* barras verticais (agrupadas ou empilhadas) ---------------------------- */
  function barras(area, spec, W, empilhar) {
    var series = spec.series;
    var cats = [];
    series.forEach(function (s) { (s.pontos || []).forEach(function (p) { if (cats.indexOf(String(p.t)) < 0) cats.push(String(p.t)); }); });
    var val = series.map(function (s) { var m = {}; (s.pontos || []).forEach(function (p) { m[String(p.t)] = p.v; }); return m; });
    var vs = [0];
    if (empilhar) {
      cats.forEach(function (c) {
        var pos = 0, neg = 0;
        val.forEach(function (m) { var v = m[c]; if (v == null) return; if (v >= 0) pos += v; else neg += v; });
        vs.push(pos, neg);
      });
      if (spec.total !== false) cats.forEach(function (c) { var t = 0; val.forEach(function (m) { if (m[c] != null) t += m[c]; }); vs.push(t); });
    } else val.forEach(function (m) { cats.forEach(function (c) { if (m[c] != null) vs.push(m[c]); }); });
    (spec.ref || []).forEach(function (r) { vs.push(r.v); });
    var ny = nice(Math.min.apply(null, vs), Math.max.apply(null, vs), W < 480 ? 4 : 6);
    var rot = cats.some(function (c) { return c.length > 6; }) && cats.length * 60 > W;
    var H = (W < 480 ? 250 : 300) + (rot ? 40 : 0), mL = 44, mR = 10, mT = 10, mB = rot ? 70 : 28;
    var pw = W - mL - mR, ph = H - mT - mB;
    function Y(v) { return mT + (1 - (v - ny.lo) / (ny.hi - ny.lo)) * ph; }
    var s = svg("svg", { viewBox: "0 0 " + W + " " + H, width: W, height: H });
    ny.ticks.forEach(function (t) {
      s.appendChild(svg("line", { x1: mL, x2: W - mR, y1: Y(t), y2: Y(t), "class": t === 0 ? "zero" : "gl" }));
      s.appendChild(svg("text", { x: mL - 6, y: Y(t) + 4, "text-anchor": "end", "class": "ax" }, fmt(t)));
    });
    var bw = pw / cats.length, gap = Math.min(8, bw * 0.2);
    var tip = tooltip(area);
    var esc_ = 1;
    var salto = Math.max(1, Math.ceil(cats.length / Math.floor(pw / (rot ? 18 : 44))));
    cats.forEach(function (c, ci) {
      var xb = mL + ci * bw + gap / 2, larg = bw - gap;
      if (empilhar) {
        var pos = 0, neg = 0;
        series.forEach(function (se, si) {
          var v = val[si][c]; if (v == null || v === 0) return;
          var a = v >= 0 ? pos : neg, b = a + v;
          if (v >= 0) pos = b; else neg = b;
          var y1 = Y(Math.max(a, b)), y2 = Y(Math.min(a, b));
          var r = svg("rect", { x: xb, y: y1, width: larg, height: Math.max(0.5, y2 - y1 - 1), fill: cor(si), rx: 1.5 });
          r.addEventListener("mousemove", function (ev) { dica(ev, c); });
          r.addEventListener("touchstart", function (ev) { dica(ev, c); }, { passive: true });
          r.addEventListener("mouseleave", tip.hide);
          s.appendChild(r);
        });
        if (spec.total !== false && series.length > 1) {
          var tot = 0, tem = false; val.forEach(function (m) { if (m[c] != null) { tot += m[c]; tem = true; } });
          if (tem) s.appendChild(svg("line", { x1: xb - 1, x2: xb + larg + 1, y1: Y(tot), y2: Y(tot), stroke: "var(--text)", "stroke-width": 2.5 }));
        }
      } else {
        var sub = larg / series.length;
        series.forEach(function (se, si) {
          var v = val[si][c]; if (v == null) return;
          var y1 = Y(Math.max(0, v)), y2 = Y(Math.min(0, v));
          var r = svg("rect", { x: xb + si * sub + (series.length > 1 ? 1 : 0), y: y1, width: Math.max(1, sub - (series.length > 1 ? 2 : 0)), height: Math.max(0.5, y2 - y1), fill: cor(si), rx: 2 });
          r.addEventListener("mousemove", function (ev) { dica(ev, c); });
          r.addEventListener("touchstart", function (ev) { dica(ev, c); }, { passive: true });
          r.addEventListener("mouseleave", tip.hide);
          s.appendChild(r);
        });
      }
      if (ci % salto === 0) {
        var tx = xb + larg / 2, ty = mT + ph + 16;
        var t = svg("text", rot ? { x: tx, y: ty - 4, "text-anchor": "end", "class": "ax", transform: "rotate(-40 " + tx + " " + (ty - 4) + ")" } : { x: tx, y: ty, "text-anchor": "middle", "class": "ax" }, c.length > 22 ? c.slice(0, 21) + "…" : c);
        s.appendChild(t);
      }
    });
    (spec.ref || []).forEach(function (r) {
      s.appendChild(svg("line", { x1: mL, x2: W - mR, y1: Y(r.v), y2: Y(r.v), "class": "refl" }));
      if (r.rotulo) s.appendChild(svg("text", { x: W - mR - 2, y: Y(r.v) - 4, "text-anchor": "end", "class": "refl-t" }, r.rotulo));
    });
    function dica(ev, c) {
      var r = s.getBoundingClientRect(); esc_ = W / r.width;
      var cx = (ev.touches ? ev.touches[0].clientX : ev.clientX) - r.left, cy = (ev.touches ? ev.touches[0].clientY : ev.clientY) - r.top;
      var html = "<b>" + esc(c) + "</b>", tot = 0;
      series.forEach(function (se, si) {
        var v = val[si][c]; if (v == null) return; tot += v;
        html += "<br><i style=\"background:" + cor(si) + "\"></i>" + (series.length > 1 ? esc(se.nome) + ": " : "") + fmt(v) + (spec.unidade ? " " + esc(spec.unidade) : "");
      });
      if (empilhar && series.length > 1 && spec.total !== false) html += "<br>Soma: " + fmt(tot);
      tip.show(html, cx, cy);
    }
    legenda(area, series);
    if (empilhar && series.length > 1 && spec.total !== false) {
      var lg = area.querySelector(".g-legenda");
      if (lg) { var sp = el("span"); var sw = el("i"); sw.style.background = "var(--text)"; sw.style.height = "3px"; sp.appendChild(sw); sp.appendChild(document.createTextNode(spec.rotulo_total || "Soma")); lg.appendChild(sp); }
    }
    area.appendChild(s);
  }

  /* barras horizontais ---------------------------------------------------- */
  function barrash(area, spec, W) {
    var pts = (spec.series[0].pontos || []).filter(function (p) { return p.v != null; });
    var vs = pts.map(function (p) { return p.v; }).concat([0]);
    var ny = nice(Math.min.apply(null, vs), Math.max.apply(null, vs), W < 480 ? 4 : 6);
    var labW = Math.min(W * 0.42, 12 + 6.6 * Math.max.apply(null, pts.map(function (p) { return String(p.t).length; })));
    var lin = 24, mT = 6, mB = 24, H = mT + mB + lin * pts.length, mL = labW + 8, mR = 44, pw = W - mL - mR;
    function X(v) { return mL + (v - ny.lo) / (ny.hi - ny.lo) * pw; }
    var s = svg("svg", { viewBox: "0 0 " + W + " " + H, width: W, height: H });
    ny.ticks.forEach(function (t) {
      s.appendChild(svg("line", { x1: X(t), x2: X(t), y1: mT, y2: H - mB, "class": t === 0 ? "zero" : "gl" }));
      s.appendChild(svg("text", { x: X(t), y: H - 6, "text-anchor": "middle", "class": "ax" }, fmt(t)));
    });
    var destaque = spec.destaque || [];
    pts.forEach(function (p, i) {
      var y = mT + i * lin + 4, h = lin - 8;
      var a = X(Math.min(0, p.v)), b = X(Math.max(0, p.v));
      var lab = String(p.t);
      var hi = destaque.indexOf(lab) >= 0 || /brasil/i.test(lab);
      s.appendChild(svg("rect", { x: a, y: y, width: Math.max(1, b - a), height: h, rx: 2, fill: hi ? cor(1) : cor(0) }));
      s.appendChild(svg("text", { x: mL - 6, y: y + h / 2 + 4, "text-anchor": "end", "class": "ax-l", "font-weight": hi ? 700 : 400 }, lab.length > 40 ? lab.slice(0, 39) + "…" : lab));
      s.appendChild(svg("text", { x: b + 4, y: y + h / 2 + 4, "text-anchor": "start", "class": "ax" }, fmt(p.v)));
    });
    area.appendChild(s);
  }

  /* desenho -------------------------------------------------------------- */
  function desenhar(area) {
    var id = area.getAttribute("data-grafico");
    var srcEl = document.getElementById(id + "-dados");
    if (!srcEl) return;
    var spec;
    try { spec = JSON.parse(srcEl.textContent); } catch (e) { return; }
    area.innerHTML = "";
    var W = Math.max(280, Math.floor(area.clientWidth || 600));
    var tipo = spec.tipo || "linha";
    try {
      if (tipo === "linha") linha(area, spec, W);
      else if (tipo === "barras") barras(area, spec, W, false);
      else if (tipo === "empilhadas") barras(area, spec, W, true);
      else if (tipo === "barrash") barrash(area, spec, W);
    } catch (e) { area.textContent = "Não foi possível desenhar o gráfico; veja os dados na tabela abaixo."; }
  }
  function redesenhar() { document.querySelectorAll(".g-area").forEach(desenhar); }
  var larguraAnterior = window.innerWidth, timer;
  window.addEventListener("resize", function () {
    if (Math.abs(window.innerWidth - larguraAnterior) < 20) return;
    larguraAnterior = window.innerWidth;
    clearTimeout(timer); timer = setTimeout(redesenhar, 150);
  });
  function iniciar() { redesenhar(); renderMath(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", iniciar); else iniciar();
  window.addEventListener("load", renderMath);
})();
