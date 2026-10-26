"""極簡 SVG 繪圖輔助：把數學坐标自動縮放成 360×280 的圖。"""
import math


class Fig:
    def __init__(self, w=360, h=280, pad=34):
        self.w, self.h, self.pad = w, h, pad
        self.items = []
        self.pts = []

    # ---- 坐标收集 ----
    def _add(self, *pts):
        self.pts.extend(pts)

    def _map(self):
        xs = [p[0] for p in self.pts] or [0, 1]
        ys = [p[1] for p in self.pts] or [0, 1]
        x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
        if x1 - x0 < 1e-9:
            x0, x1 = x0 - 1, x1 + 1
        if y1 - y0 < 1e-9:
            y0, y1 = y0 - 1, y1 + 1
        sx = (self.w - 2 * self.pad) / (x1 - x0)
        sy = (self.h - 2 * self.pad) / (y1 - y0)
        s = min(sx, sy)
        cx = (x0 + x1) / 2
        cy = (y0 + y1) / 2
        self.T = lambda p: (self.w / 2 + (p[0] - cx) * s, self.h / 2 - (p[1] - cy) * s)

    # ---- 圖元 ----
    def seg(self, p, q, dash=None, color="currentColor", w=1.6, arrow=False):
        self._add(p, q)
        self.items.append(("seg", p, q, dash, color, w, arrow))

    def poly(self, pts, fill="none", color="currentColor", w=1.6, opacity=0.07):
        self._add(*pts)
        self.items.append(("poly", pts, fill, color, w, opacity))

    def circ(self, c, r, color="currentColor", w=1.6, dash=None):
        self._add(c, (c[0] + r, c[1]), (c[0], c[1] + r))
        self.items.append(("circ", c, r, color, w, dash))

    def dot(self, p, color="#e11d48", r=3.2):
        self._add(p)
        self.items.append(("dot", p, color, r))

    def label(self, p, text, dx=6, dy=-6, color="currentColor", size=12, anchor="start"):
        self._add(p)
        self.items.append(("label", p, text, dx, dy, color, size, anchor))

    def note(self, p, text, dx=6, dy=16, color="#64748b", size=10.5):
        self._add(p)
        self.items.append(("label", p, text, dx, dy, color, size, "start"))

    def arc(self, c, r, a0, a1, color="#94a3b8", w=1.2, dash="4 3"):
        self.items.append(("arc", c, r, a0, a1, color, w, dash))

    def axes(self, xr=None, yr=None, grid=False):
        xs = [p[0] for p in self.pts]
        ys = [p[1] for p in self.pts]
        x0, x1 = xr or (min(xs + [0]) - 0.5, max(xs + [0]) + 0.5)
        y0, y1 = yr or (min(ys + [0]) - 0.5, max(ys + [0]) + 0.5)
        self._add((x0, 0), (x1, 0), (0, y0), (0, y1))
        self.items.append(("axis", (x0, x1, y0, y1), grid))

    # ---- 輸出 ----
    def svg(self, cap_pad=0):
        self._map()
        T = self.T
        out = [f'<svg viewBox="0 0 {self.w} {self.h}" width="100%" role="img" '
               f'style="max-width:{self.w}px">']
        out.append('<rect width="100%" height="100%" fill="none"/>')
        for it in self.items:
            kind = it[0]
            if kind == "axis":
                (x0, x1, y0, y1), _grid = it[1], it[2]
                if _grid:
                    gx = math.floor(x0)
                    while gx <= x1:
                        a, b = T((gx, y0)), T((gx, y1))
                        out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#e2e8f0" stroke-width="0.7"/>')
                        gx += 1
                a, b = T((x0, 0)), T((x1, 0))
                out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#94a3b8" stroke-width="1"/>')
                a, b = T((0, y0)), T((0, y1))
                out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#94a3b8" stroke-width="1"/>')
            elif kind == "seg":
                _, p, q, dash, color, w, arrow = it
                a, b = T(p), T(q)
                d = f' stroke-dasharray="{dash}"' if dash else ""
                mk = ' marker-end="url(#ah)"' if arrow else ""
                out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{color}" stroke-width="{w}"{d}{mk}/>')
            elif kind == "poly":
                _, pts, fill, color, w, op = it
                s = " ".join(f"{T(p)[0]:.1f},{T(p)[1]:.1f}" for p in pts)
                out.append(f'<polygon points="{s}" fill="{fill}" fill-opacity="{op}" stroke="{color}" stroke-width="{w}"/>')
            elif kind == "circ":
                _, c, r, color, w, dash = it
                o = T(c)
                d = f' stroke-dasharray="{dash}"' if dash else ""
                out.append(f'<circle cx="{o[0]:.1f}" cy="{o[1]:.1f}" r="{abs(T((c[0]+r,c[1]))[0]-o[0]):.1f}" fill="none" stroke="{color}" stroke-width="{w}"{d}/>')
            elif kind == "dot":
                _, p, color, r = it
                o = T(p)
                out.append(f'<circle cx="{o[0]:.1f}" cy="{o[1]:.1f}" r="{r}" fill="{color}"/>')
            elif kind == "arc":
                _, c, r, a0, a1, color, w, dash = it
                o = T(c)
                rr = abs(T((c[0] + r, c[1]))[0] - o[0])
                p0 = (o[0] + rr * math.cos(math.radians(a0)), o[1] - rr * math.sin(math.radians(a0)))
                p1 = (o[0] + rr * math.cos(math.radians(a1)), o[1] - rr * math.sin(math.radians(a1)))
                large = 1 if abs(a1 - a0) > 180 else 0
                out.append(f'<path d="M{p0[0]:.1f} {p0[1]:.1f} A{rr:.1f} {rr:.1f} 0 {large} 0 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="{color}" stroke-width="{w}" stroke-dasharray="{dash}"/>')
            elif kind == "label":
                _, p, text, dx, dy, color, size, anchor = it
                o = T(p)
                out.append(f'<text x="{o[0]+dx:.1f}" y="{o[1]+dy:.1f}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-family="Noto Serif CJK TC, Georgia, serif">{text}</text>')
        out.append('<defs><marker id="ah" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto">'
                   '<path d="M0,0 L6,3 L0,6 z" fill="currentColor"/></marker></defs>')
        out.append("</svg>")
        return "\n".join(out)


def insert(page, svg, caption):
    """把圖插入題解卡片最上方（若尚未有圖）。"""
    s = open(page, encoding="utf8").read()
    if "<svg" in s or "<img" in s:
        return False
    block = ('<figure class="fig">\n' + svg +
             f'\n<figcaption>{caption}</figcaption></figure>\n    ')
    if "<h2>題解</h2>" not in s:
        return False
    s = s.replace("<h2>題解</h2>", "<h2>題解</h2>\n    " + block, 1)
    open(page, "w", encoding="utf8").write(s)
    return True
