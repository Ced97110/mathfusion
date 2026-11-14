import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pp(c, R, d): return (c[0] + R * math.cos(math.radians(d)), c[1] + R * math.sin(math.radians(d)))
def axes_xy(ax, c, R, ext=4):
    arrow(ax, (c[0] - R - ext, c[1]), (c[0] + R + ext, c[1]), 'fixe', lw=0.7)
    arrow(ax, (c[0], c[1] - R - ext), (c[0], c[1] + R + ext), 'fixe', lw=0.7)
def ucirc(ax, c, R): ax.add_patch(Circle(c, R, ec=COL['fixe'], fc='none', lw=0.8, zorder=1))
def arcp(ax, c, r0, r1, a0, a1, role, lw=1.0, head=True):
    n = max(8, int(abs(a1 - a0) / 4)); pts = [pp(c, r0 + (r1 - r0) * i / n, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
    if head: arrow(ax, pts[-2], pts[-1], role, lw=lw)
def dot(ax, p, role, r=1.1): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))
TH = r'$\theta$'

fig, ax = canvas(40)
rows = ((28, '30°', 'y = 0,5', 'x = 0,866', 'tan θ ≈ 0,577'), (9, '130°', 'y = 0,766', 'x = −0,643', 'tan θ ≈ −1,19'))
for y, a, ys, xs, ts in rows:
    text(ax, 7, y + 4, a, 'varie', 'm')
    box(ax, 14, y, 19, 8, 'fixe', label=ys, size='s'); text(ax, 36, y + 4, '÷', 'encre', 'm')
    box(ax, 39, y, 20, 8, 'fixe', label=xs, size='s'); text(ax, 62, y + 4, '=', 'encre', 'm')
    box(ax, 65, y, 21, 8, 'sujet', label=ts, size='s')
save(fig, '28-048')
