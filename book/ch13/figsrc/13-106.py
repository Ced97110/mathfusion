import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def G(ax, x0, y0, n, c, xl="j'ai", yl='je dois'):
    for i in range(n + 1):
        for p, q in (((x0 + i*c, y0), (x0 + i*c, y0 + n*c)), ((x0, y0 + i*c), (x0 + n*c, y0 + i*c))):
            ax.plot([p[0], q[0]], [p[1], q[1]], color=COL['fixe'], lw=0.35, alpha=0.45, zorder=1)
    arrow(ax, (x0, y0), (x0 + n*c + 4, y0), 'fixe', lw=0.8)
    arrow(ax, (x0, y0), (x0, y0 + n*c + 4), 'fixe', lw=0.8)
    if xl: text(ax, x0 + n*c + 2, y0 - 3.5, xl, 'fixe', 's')
    if yl: text(ax, x0 + 2, y0 + n*c + 7, yl, 'fixe', 's')
    return lambda a, b: (x0 + a*c, y0 + b*c)
def dpt(ax, p, role, r=1.5):
    disc(ax, p[0], p[1], r, role)
def trim_arrow(ax, p, q, role='varie', t=2.0, curve=0.0, both=False):
    d = math.hypot(q[0]-p[0], q[1]-p[1]); ux, uy = (q[0]-p[0])/d, (q[1]-p[1])/d
    arrow(ax, (p[0]+ux*t, p[1]+uy*t), (q[0]-ux*t, q[1]-uy*t), role, curve=curve, both=both)
fig, ax = canvas(64)
f = numberline(ax, 8, 72, 30, -4, 4, arrow_right=True, every=2, role='fixe')
for v in range(-4, 5): dpt(ax, (f(v), 30), 'sujet' if v < 0 else 'autre', 1.5)
brace(ax, f(-4), f(4), 36, 'sujet', label='ℤ : tous les entiers relatifs', down=False)
brace(ax, f(0), f(4), 24, 'autre', label='ℕ : 0, 1, 2…', down=True)
text(ax, f(-2), 41.5+6, '', 'sujet', 's') if False else None
text(ax, f(-2), 17, '−2 est dans ℤ,', 'sujet', 's')
text(ax, f(-2), 13, 'pas dans ℕ', 'sujet', 's')
save(fig, '13-106')
