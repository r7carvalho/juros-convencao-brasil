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

  var DESTAQUE = null;
  function corS(i, nome) {
    if (DESTAQUE && DESTAQUE.indexOf(nome) < 0) return getComputedStyle(root).getPropertyValue("--text-3").trim() || "#888";
    if (DESTAQUE) return cor(DESTAQUE.indexOf(nome));
    return cor(i);
  }
  function legenda(area, series) {
    if (series.length < 2) return;
    var lg = el("div", "g-legenda");
    series.forEach(function (s, i) {
      var sp = el("span"); var sw = el("i"); sw.style.background = corS(i, s.nome);
      if (DESTAQUE && DESTAQUE.indexOf(s.nome) < 0) sp.style.opacity = ".75";
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
    var postos = [];   /* caixas de rótulos já desenhados, para evitar sobreposição */
    (spec.ref || []).forEach(function (r) {
      s.appendChild(svg("line", { x1: mL, x2: W - mR, y1: Y(r.v), y2: Y(r.v), "class": "refl" }));
      if (r.rotulo) {
        s.appendChild(svg("text", { x: W - mR - 2, y: Y(r.v) - 4, "text-anchor": "end", "class": "refl-t" }, r.rotulo));
        postos.push({ x0: W - mR - 2 - r.rotulo.length * 6, x1: W - mR, y0: Y(r.v) - 14, y1: Y(r.v) - 2 });
      }
    });
    series.forEach(function (se, i) {
      var d = "", pen = false;
      se.pts.forEach(function (p) {
        if (p.v == null) { pen = false; return; }
        d += (pen ? "L" : "M") + X(p.x).toFixed(1) + " " + Y(p.v).toFixed(1); pen = true;
      });
      var apagada = DESTAQUE && DESTAQUE.indexOf(se.nome) < 0;
      s.appendChild(svg("path", { d: d, fill: "none", stroke: corS(i, se.nome), "stroke-width": apagada ? 1.2 : 2.4, "stroke-opacity": apagada ? 0.6 : 1, "stroke-linejoin": "round", "stroke-linecap": "round" }));
      var poucos = se.pts.length <= 40 && !apagada;
      se.pts.forEach(function (p) {
        if (p.v == null || !poucos) return;
        s.appendChild(svg("circle", { cx: X(p.x), cy: Y(p.v), r: se.pts.length <= 14 ? 3.5 : 2.2, fill: corS(i, se.nome), stroke: "var(--surface)", "stroke-width": 1.5 }));
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
        html += "<br><i style=\"background:" + corS(l.i, l.nome) + "\"></i>" + (series.length > 1 ? esc(l.nome) + ": " : "") + fmt(l.p.v) + (spec.unidade ? " " + esc(spec.unidade) : "");
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
    var postos = [];   /* caixas de rótulos já desenhados, para evitar sobreposição */
    (spec.ref || []).forEach(function (r) {
      s.appendChild(svg("line", { x1: mL, x2: W - mR, y1: Y(r.v), y2: Y(r.v), "class": "refl" }));
      if (r.rotulo) {
        s.appendChild(svg("text", { x: W - mR - 2, y: Y(r.v) - 4, "text-anchor": "end", "class": "refl-t" }, r.rotulo));
        postos.push({ x0: W - mR - 2 - r.rotulo.length * 6, x1: W - mR, y0: Y(r.v) - 14, y1: Y(r.v) - 2 });
      }
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

  /* dispersão (x, y) com rótulos e destaque -------------------------------- */
  function dispersao(area, spec, W) {
    var pts = [];
    spec.series.forEach(function (se, si) {
      (se.pontos || []).forEach(function (p) { if (p.v != null && p.x != null) pts.push({ x: p.x, v: p.v, t: String(p.t), si: si }); });
    });
    if (!pts.length) return;
    var destaque = spec.destaque || [];
    var xs = pts.map(function (p) { return p.x; }), vs = pts.map(function (p) { return p.v; });
    (spec.ref || []).forEach(function (r) { vs.push(r.v); });
    var nx = nice(Math.min.apply(null, xs), Math.max.apply(null, xs), W < 480 ? 4 : 6);
    var ny = nice(Math.min.apply(null, vs.concat([0])), Math.max.apply(null, vs), W < 480 ? 4 : 6);
    var H = W < 480 ? 280 : 340, mL = spec.eixo_y ? 58 : 44, mR = 14, mT = 12, mB = 40;
    var pw = W - mL - mR, ph = H - mT - mB;
    function X(x) { return mL + (x - nx.lo) / (nx.hi - nx.lo) * pw; }
    function Y(v) { return mT + (1 - (v - ny.lo) / (ny.hi - ny.lo)) * ph; }
    var s = svg("svg", { viewBox: "0 0 " + W + " " + H, width: W, height: H });
    ny.ticks.forEach(function (t) {
      s.appendChild(svg("line", { x1: mL, x2: W - mR, y1: Y(t), y2: Y(t), "class": t === 0 ? "zero" : "gl" }));
      s.appendChild(svg("text", { x: mL - 6, y: Y(t) + 4, "text-anchor": "end", "class": "ax" }, fmt(t)));
    });
    nx.ticks.forEach(function (t) {
      s.appendChild(svg("line", { x1: X(t), x2: X(t), y1: mT + ph, y2: mT + ph + 4, "class": "gl" }));
      s.appendChild(svg("text", { x: X(t), y: mT + ph + 16, "text-anchor": "middle", "class": "ax" }, fmt(t)));
    });
    if (spec.eixo_x) s.appendChild(svg("text", { x: mL + pw / 2, y: H - 4, "text-anchor": "middle", "class": "ax" }, spec.eixo_x.length > 90 ? spec.eixo_x.slice(0, 89) + "…" : spec.eixo_x));
    if (spec.eixo_y) {
      var ey = spec.eixo_y.length > 60 ? spec.eixo_y.slice(0, 59) + "…" : spec.eixo_y;
      s.appendChild(svg("text", { x: 0, y: 0, "text-anchor": "middle", "class": "ax", transform: "translate(11," + (mT + ph / 2) + ") rotate(-90)" }, ey));
    }
    var postos = [];   /* caixas de rótulos já desenhados, para evitar sobreposição */
    (spec.ref || []).forEach(function (r) {
      s.appendChild(svg("line", { x1: mL, x2: W - mR, y1: Y(r.v), y2: Y(r.v), "class": "refl" }));
      if (r.rotulo) {
        s.appendChild(svg("text", { x: W - mR - 2, y: Y(r.v) - 4, "text-anchor": "end", "class": "refl-t" }, r.rotulo));
        postos.push({ x0: W - mR - 2 - r.rotulo.length * 6, x1: W - mR, y0: Y(r.v) - 14, y1: Y(r.v) - 2 });
      }
    });
    if (spec.reta && spec.reta.b != null) {
      var a = spec.reta.a, b = spec.reta.b, xa = nx.lo, xb = nx.hi;
      if (b !== 0) {
        /* corta a reta nos limites do eixo y */
        var x1 = (ny.lo - a) / b, x2 = (ny.hi - a) / b;
        xa = Math.max(xa, Math.min(x1, x2)); xb = Math.min(xb, Math.max(x1, x2));
      }
      s.appendChild(svg("line", { x1: X(xa), x2: X(xb), y1: Y(a + b * xa), y2: Y(a + b * xb), "class": "refl" }));
      if (spec.reta.rotulo) {
        /* rótulo da reta como legenda no canto superior esquerdo, com um traço de amostra */
        var yr = mT + 12, xr = mL + 8;
        s.appendChild(svg("line", { x1: xr, x2: xr + 22, y1: yr - 4, y2: yr - 4, "class": "refl" }));
        s.appendChild(svg("text", { x: xr + 28, y: yr, "text-anchor": "start", "class": "refl-t" }, spec.reta.rotulo));
        postos.push({ x0: xr, x1: xr + 28 + spec.reta.rotulo.length * 6, y0: yr - 10, y1: yr + 2 });
      }
    }
    var tip = tooltip(area);
    var cinza = getComputedStyle(root).getPropertyValue("--text-3").trim() || "#888";
    /* os próprios pontos também são obstáculos para os rótulos */
    pts.forEach(function (p) { postos.push({ x0: X(p.x) - 6, x1: X(p.x) + 6, y0: Y(p.v) - 6, y1: Y(p.v) + 6 }); });
    pts.forEach(function (p) {
      var hi = destaque.indexOf(p.t) >= 0;
      var c = svg("circle", { cx: X(p.x), cy: Y(p.v), r: hi ? 6 : 4.5, fill: hi ? cor(1) : cor(0), stroke: "var(--surface)", "stroke-width": 1.5 });
      function dica(ev) {
        var rr = s.getBoundingClientRect();
        var cx = (ev.touches ? ev.touches[0].clientX : ev.clientX) - rr.left, cy = (ev.touches ? ev.touches[0].clientY : ev.clientY) - rr.top;
        tip.show("<b>" + esc(p.t) + "</b><br>" + esc(spec.eixo_x || "x") + ": " + fmt(p.x) + "<br>" + esc(spec.eixo_y || "y") + ": " + fmt(p.v), cx, cy);
      }
      c.addEventListener("mousemove", dica);
      c.addEventListener("touchstart", dica, { passive: true });
      c.addEventListener("mouseleave", tip.hide);
      s.appendChild(c);
      if (W >= 420 || hi) {
        /* tenta posições ao redor do ponto e fica com a primeira que não bate em outro rótulo
           nem sai da área do gráfico */
        var px = X(p.x), py = Y(p.v), larg = p.t.length * 6.5 + (hi ? 6 : 0);
        var direita = px < mL + pw * 0.8;
        var lados = direita ? [1, -1] : [-1, 1];
        var cands = [];
        lados.forEach(function (ld) { [0, -13, 13, -26, 26].forEach(function (dy) { cands.push({ ld: ld, dy: dy }); }); });
        var esc0 = null;
        for (var k = 0; k < cands.length; k++) {
          var cd = cands[k];
          var lx = px + cd.ld * 8, ly = py + 4 + cd.dy;
          var x0 = cd.ld > 0 ? lx : lx - larg, x1r = cd.ld > 0 ? lx + larg : lx;
          var fora = x0 < mL || x1r > W - mR || ly < mT + 9 || ly > mT + ph;
          var bate = postos.some(function (q) { return ly - 10 < q.y1 && ly + 2 > q.y0 && x0 < q.x1 && x1r > q.x0; });
          if (!fora && !bate) { esc0 = { lx: lx, ly: ly, x0: x0, x1: x1r, ld: cd.ld }; break; }
          if (!esc0 && k === cands.length - 1) esc0 = { lx: px + lados[0] * 8, ly: py + 4, x0: x0, x1: x1r, ld: lados[0] };
        }
        postos.push({ x0: esc0.x0, x1: esc0.x1, y0: esc0.ly - 10, y1: esc0.ly + 2 });
        s.appendChild(svg("text", { x: esc0.lx, y: esc0.ly, "text-anchor": esc0.ld > 0 ? "start" : "end", "class": "ax", fill: hi ? "var(--text)" : cinza, "font-weight": hi ? 700 : 400 }, p.t));
      }
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
    DESTAQUE = null;
    if (tipo === "linha") {
      if (Array.isArray(spec.destaque) && spec.destaque.length) DESTAQUE = spec.destaque;
      else if (spec.series.length > 5 && spec.series.some(function (x) { return x.nome === "Brasil"; })) DESTAQUE = ["Brasil"];
    }
    try {
      if (tipo === "linha") linha(area, spec, W);
      else if (tipo === "barras") barras(area, spec, W, false);
      else if (tipo === "empilhadas") barras(area, spec, W, true);
      else if (tipo === "barrash") barrash(area, spec, W);
      else if (tipo === "dispersao") dispersao(area, spec, W);
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
