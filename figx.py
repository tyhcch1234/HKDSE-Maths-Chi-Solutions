#!/usr/bin/env python3
"""figx：為題解畫圖的輕量 SVG 工具（數學座標自動縮放）。

用法示例：
    c = Canvas(340, 280)
    A, B, C = (0,0), (10,0), (4,7)
    c.poly([A,B,C], fill="#2563eb", op=0.06)
    c.seg(A,B); c.seg(B,C); c.seg(C,A)
    c.right(A, B, C)          # 在 A 點的直角符號
    c.ang(B, A, C, "60°")     # 在 A 點、由 AB 到 AC 的角弧＋標籤
    c.pt(A,"A",-12,4)         # 點＋標籤
    c.len(A,B,"12 cm")        # 邊長標籤（自動放中點）
    svg = c.svg()
"""
import math

INK = "currentColor"
BLUE = "#2563eb"
RED = "#e11d48"
GREY = "#94a3b8"
TEAL = "#0f766e"
AMBER = "#d97706"
VIOLET = "#7c3aed"
FONT = "Noto Serif CJK TC, Georgia, serif"


def _esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _n(x):
    return ("%.1f" % x).rstrip("0").rstrip(".")


class Canvas:
    def __init__(self, w=340, h=280, pad=34):
        self.w, self.h, self.pad = w, h, pad
        self.items = []
        self.pts = []

    # ---------- 座標 ----------
    def _add(self, *ps):
        for p in ps:
            self.pts.append((float(p[0]), float(p[1])))

    def _map(self):
        xs = [p[0] for p in self.pts] or [0, 1]
        ys = [p[1] for p in self.pts] or [0, 1]
        x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
        if x1 - x0 < 1e-9:
            x0, x1 = x0 - 1, x1 + 1
        if y1 - y0 < 1e-9:
            y0, y1 = y0 - 1, y1 + 1
        s = min((self.w - 2 * self.pad) / (x1 - x0), (self.h - 2 * self.pad) / (y1 - y0))
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        self.s = s
        self.T = lambda p: (self.w / 2 + (p[0] - cx) * s, self.h / 2 - (p[1] - cy) * s)

    # ---------- 圖元 ----------
    def seg(self, p, q, color=INK, w=1.6, dash=None, arrow=False):
        self._add(p, q)
        self.items.append(("seg", p, q, color, w, dash, arrow))

    def poly(self, pts, fill="none", color=INK, w=1.6, op=0.0, dash=None):
        self._add(*pts)
        self.items.append(("poly", pts, fill, color, w, op, dash))

    def circ(self, c, r, color=BLUE, w=1.8, dash=None, fill="none", op=0.0):
        self._add(c, (c[0] + r, c[1]), (c[0], c[1] + r))
        self.items.append(("circ", c, r, color, w, dash, fill, op))

    def ell(self, c, rx, ry, color=INK, w=1.4, dash=None):
        self._add((c[0] - rx, c[1] - ry), (c[0] + rx, c[1] + ry))
        self.items.append(("ell", c, rx, ry, color, w, dash))

    def dot(self, p, color=RED, r=3.2):
        self._add(p)
        self.items.append(("dot", p, color, r))

    def txt(self, p, s, dx=0, dy=0, color=INK, size=12, anchor="start", serif=True):
        self._add(p)
        self.items.append(("txt", p, s, dx, dy, color, size, anchor))

    def pt(self, p, name, dx=8, dy=-6, color=INK):
        self.dot(p, GREY if color == INK else color, 3.0)
        self.txt(p, name, dx, dy, INK, 12)

    def len(self, p, q, text, off=0, color="#334155", size=10.5, anchor="middle"):
        """邊長標籤：放在 p,q 中點，off 為沿法線方向的額外偏移（數學座標）。"""
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        dx, dy = q[0] - p[0], q[1] - p[1]
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L, dx / L
        self.txt((mx + nx * off, my + ny * off), text, 0, 0, color, size, anchor)

    def label_at(self, p, text, dx=0, dy=0, color="#334155", size=10.5, anchor="middle"):
        self.txt(p, text, dx, dy, color, size, anchor)

    def ang(self, a, v, b, text="", r=None, color=TEAL, w=1.3, dashing=None, lr=1.35):
        """在頂點 v 畫由 va 到 vb 的角弧（內角），text 標在角平分線方向。"""
        self._add(a, v, b)
        self.items.append(("ang", a, v, b, text, r, color, w, lr))

    def right(self, v, a, b, s=0.9, color=RED):
        """在 v 點的直角符號（兩方向分別指向 a、b）。"""
        self._add(v, a, b)
        self.items.append(("right", v, a, b, s, color))

    def arc(self, c, r, a0, a1, color=GREY, w=1.2, dash="4 3"):
        self._add(c, (c[0] + r, c[1]))
        self.items.append(("arc", c, r, a0, a1, color, w, dash))

    def sector(self, c, r, a0, a1, fill=TEAL, op=0.10):
        self._add(c)
        self.items.append(("sector", c, r, a0, a1, fill, op))

    def axes(self, xr, yr, xticks=None, yticks=None, xlabel="x", ylabel="y"):
        self._add((xr[0], 0), (xr[1], 0), (0, yr[0]), (0, yr[1]))
        self.items.append(("axes", xr, yr, xticks or [], yticks or [], xlabel, ylabel))

    def fn(self, f, a, b, color=BLUE, w=1.9, steps=160, sx=1.0):
        pts = [(a + (b - a) * i / steps, f(a + (b - a) * i / steps)) for i in range(steps + 1)]
        self._add(*pts)
        self.items.append(("fn", pts, color, w))


    def arcfill(self, c, r, a0, a1, color=BLUE, op=0.10, chord=True, steps=40):
        """以圓弧圍出的區域填色：chord=True 時以弦封口（弓形），否則連到圓心（扇形）。"""
        pts = [circle_pt(c, r, a0 + (a1 - a0) * i / steps) for i in range(steps + 1)]
        if not chord:
            pts = [c] + pts
        self._add(*pts)
        self.items.append(("poly", pts, color, "none", 0, op, None))

    def hidden(self, p, q):
        self.seg(p, q, GREY, 1.1, "4 3")

    # ---------- 輸出 ----------
    def svg(self):
        self._map()
        T, s = self.T, self.s
        o = ['<svg viewBox="0 0 %d %d" width="%d" role="img">' % (self.w, self.h, self.w)]
        for it in self.items:
            k = it[0]
            if k == "seg":
                _, p, q, col, w, dash, arrow = it
                a, b = T(p), T(q)
                d = ' stroke-dasharray="%s"' % dash if dash else ""
                mk = ' marker-end="url(#ah)"' if arrow else ""
                o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s%s/>'
                         % (_n(a[0]), _n(a[1]), _n(b[0]), _n(b[1]), col, w, d, mk))
            elif k == "poly":
                _, ps, fill, col, w, op, dash = it
                pts = " ".join("%s,%s" % (_n(T(p)[0]), _n(T(p)[1])) for p in ps)
                fo = ' fill-opacity="%s"' % op if fill != "none" else ""
                d = ' stroke-dasharray="%s"' % dash if dash else ""
                o.append('<polygon points="%s" fill="%s"%s stroke="%s" stroke-width="%s"%s/>'
                         % (pts, fill, fo, col, w, d))
            elif k == "circ":
                _, c, r, col, w, dash, fill, op = it
                ctr = T(c)
                rr = r * s
                d = ' stroke-dasharray="%s"' % dash if dash else ""
                fo = ' fill-opacity="%s"' % op if fill != "none" else ""
                o.append('<circle cx="%s" cy="%s" r="%s" fill="%s"%s stroke="%s" stroke-width="%s"%s/>'
                         % (_n(ctr[0]), _n(ctr[1]), _n(rr), fill, fo, col, w, d))
            elif k == "ell":
                _, c, rx, ry, col, w, dash = it
                ctr = T(c)
                d = ' stroke-dasharray="%s"' % dash if dash else ""
                o.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="none" stroke="%s" stroke-width="%s"%s/>'
                         % (_n(ctr[0]), _n(ctr[1]), _n(rx * s), _n(ry * s), col, w, d))
            elif k == "dot":
                _, p, col, r = it
                a = T(p)
                o.append('<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (_n(a[0]), _n(a[1]), r, col))
            elif k == "txt":
                _, p, tx, dx, dy, col, size, anchor = it
                a = T(p)
                o.append('<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="%s" '
                         'font-family="%s">%s</text>'
                         % (_n(a[0] + dx), _n(a[1] + dy), size, col, anchor, FONT, _esc(tx)))
            elif k == "ang":
                _, a, v, b, tx, r, col, w, lr = it
                a0 = math.degrees(math.atan2(a[1] - v[1], a[0] - v[0]))
                a1 = math.degrees(math.atan2(b[1] - v[1], b[0] - v[0]))
                d = (a1 - a0) % 360
                if d > 180:
                    a0, a1 = a1, a0
                    d = 360 - d
                rr = (r or min(abs(_dist(a, v)), abs(_dist(b, v))) * 0.28) * s
                ctr = T(v)
                p0 = (ctr[0] + rr * math.cos(math.radians(a0)), ctr[1] - rr * math.sin(math.radians(a0)))
                p1 = (ctr[0] + rr * math.cos(math.radians(a1)), ctr[1] - rr * math.sin(math.radians(a1)))
                large = 1 if d > 180 else 0
                o.append('<path d="M%s %s A%s %s 0 %d 0 %s %s" fill="none" stroke="%s" stroke-width="%s"/>'
                         % (_n(p0[0]), _n(p0[1]), _n(rr), _n(rr), large, _n(p1[0]), _n(p1[1]), col, w))
                if tx:
                    mid = math.radians((a0 + a1) / 2)
                    o.append('<text x="%s" y="%s" font-size="10.5" fill="%s" text-anchor="middle" '
                             'font-family="%s">%s</text>'
                             % (_n(ctr[0] + rr * lr * math.cos(mid)),
                                _n(ctr[1] - rr * lr * math.sin(mid) + 3.5), col, FONT, _esc(tx)))
            elif k == "right":
                _, v, a, b, sz, col = it
                ua = _unit(v, a)
                ub = _unit(v, b)
                p1 = (v[0] + sz * ua[0], v[1] + sz * ua[1])
                p2 = (p1[0] + sz * ub[0], p1[1] + sz * ub[1])
                p3 = (v[0] + sz * ub[0], v[1] + sz * ub[1])
                pts = " ".join("%s,%s" % (_n(T(p)[0]), _n(T(p)[1])) for p in (p1, p2, p3))
                o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.2"/>' % (pts, col))
            elif k == "arc":
                _, c, r, a0, a1, col, w, dash = it
                ctr = T(c)
                rr = r * s
                p0 = (ctr[0] + rr * math.cos(math.radians(a0)), ctr[1] - rr * math.sin(math.radians(a0)))
                p1 = (ctr[0] + rr * math.cos(math.radians(a1)), ctr[1] - rr * math.sin(math.radians(a1)))
                large = 1 if abs(a1 - a0) > 180 else 0
                d = ' stroke-dasharray="%s"' % dash if dash else ""
                o.append('<path d="M%s %s A%s %s 0 %d 0 %s %s" fill="none" stroke="%s" stroke-width="%s"%s/>'
                         % (_n(p0[0]), _n(p0[1]), _n(rr), _n(rr), large, _n(p1[0]), _n(p1[1]), col, w, d))
            elif k == "sector":
                _, c, r, a0, a1, fill, op = it
                ctr = T(c)
                rr = r * s
                p0 = (ctr[0] + rr * math.cos(math.radians(a0)), ctr[1] - rr * math.sin(math.radians(a0)))
                p1 = (ctr[0] + rr * math.cos(math.radians(a1)), ctr[1] - rr * math.sin(math.radians(a1)))
                large = 1 if abs(a1 - a0) > 180 else 0
                o.append('<path d="M%s %s L%s %s A%s %s 0 %d 0 %s %s Z" fill="%s" fill-opacity="%s" '
                         'stroke="none"/>'
                         % (_n(ctr[0]), _n(ctr[1]), _n(p0[0]), _n(p0[1]), _n(rr), _n(rr), large,
                            _n(p1[0]), _n(p1[1]), fill, op))
            elif k == "axes":
                _, xr, yr, xt, yt, xl, yl = it
                a, b = T((xr[0], 0)), T((xr[1], 0))
                o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.1" marker-end="url(#ah)"/>'
                         % (_n(a[0]), _n(a[1]), _n(b[0]), _n(b[1]), GREY))
                a, b = T((0, yr[0])), T((0, yr[1]))
                o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.1" marker-end="url(#ah)"/>'
                         % (_n(a[0]), _n(a[1]), _n(b[0]), _n(b[1]), GREY))
                o.append('<text x="%s" y="%s" font-size="11" fill="#64748b" font-family="%s">%s</text>'
                         % (_n(T((xr[1], 0))[0] + 4), _n(T((xr[1], 0))[1] + 14), FONT, xl))
                o.append('<text x="%s" y="%s" font-size="11" fill="#64748b" font-family="%s">%s</text>'
                         % (_n(T((0, yr[1]))[0] - 12), _n(T((0, yr[1]))[1] - 4), FONT, yl))
                for xv in xt:
                    p = T((xv, 0))
                    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s"/>' % (_n(p[0]), _n(p[1] - 3), _n(p[0]), _n(p[1] + 3), GREY))
                    o.append('<text x="%s" y="%s" font-size="10" fill="#64748b" text-anchor="middle" font-family="%s">%s</text>'
                             % (_n(p[0]), _n(p[1] + 14), FONT, xv))
                for yv in yt:
                    p = T((0, yv))
                    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s"/>' % (_n(p[0] - 3), _n(p[1]), _n(p[0] + 3), _n(p[1]), GREY))
                    o.append('<text x="%s" y="%s" font-size="10" fill="#64748b" text-anchor="end" font-family="%s">%s</text>'
                             % (_n(p[0] - 5), _n(p[1] + 3.5), FONT, yv))
            elif k == "fn":
                _, pts, col, w = it
                d = " ".join("%s,%s" % (_n(T(p)[0]), _n(T(p)[1])) for p in pts)
                o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s"/>' % (d, col, w))
        o.append('<defs><marker id="ah" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto">'
                 '<path d="M0,0 L6,3 L0,6 z" fill="currentColor"/></marker></defs>')
        o.append("</svg>")
        return "\n".join(o)


def _dist(a, b):
    return math.hypot(b[0] - a[0], b[1] - a[1])


def _unit(a, b):
    d = _dist(a, b) or 1
    return ((b[0] - a[0]) / d, (b[1] - a[1]) / d)


def add(P, v, k=1.0):
    return (P[0] + v[0] * k, P[1] + v[1] * k)


def mix(A, B, t):
    return (A[0] + (B[0] - A[0]) * t, A[1] + (B[1] - A[1]) * t)


def rot(P, deg, about=(0, 0)):
    r = math.radians(deg)
    x, y = P[0] - about[0], P[1] - about[1]
    return (about[0] + x * math.cos(r) - y * math.sin(r), about[1] + x * math.sin(r) + y * math.cos(r))


def circle_pt(c, r, deg):
    return (c[0] + r * math.cos(math.radians(deg)), c[1] + r * math.sin(math.radians(deg)))


def tri_from(A, B, ac, bc, up=True):
    """已知 AB 及 AC=ac、BC=bc，求 C。"""
    d = _dist(A, B)
    x = (ac * ac - bc * bc + d * d) / (2 * d)
    y2 = ac * ac - x * x
    y = math.sqrt(max(y2, 0))
    ux, uy = _unit(A, B)
    return (A[0] + ux * x - uy * y * (1 if up else -1), A[1] + uy * x + ux * y * (1 if up else -1))


def tri3(A, B, angleA, angleB, up=True):
    """已知 AB 及兩底角，求第三點。"""
    d = _dist(A, B)
    ux, uy = _unit(A, B)
    a = math.radians(angleA)
    t = d * math.sin(a) / math.sin(math.radians(angleB))
    C = (A[0] + t * (math.cos(a) * ux - math.sin(a) * uy * (1 if up else -1)),
         A[1] + t * (math.cos(a) * uy + math.sin(a) * ux * (1 if up else -1)))
    return C


def oblique(p, kx=0.5, ky=0.3):
    """3D (x,y,z) -> 2D 斜投影。"""
    return (p[0] + kx * p[1], p[2] + ky * p[1])
