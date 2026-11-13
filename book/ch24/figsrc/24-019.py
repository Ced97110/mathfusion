import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def vbrace(ax, xl, xr, yb, yt, role, r=3.0):
    ym = (yb + yt) / 2; xm = xr - r; pts = []
    arc = lambda cx, cy, a0, a1: [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * k / 8)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * k / 8))) for k in range(9)]
    pts += arc(xr, yt - r, 90, 180)
    pts += arc(xl, ym + r, 0, -90)
    pts += arc(xl, ym - r, 90, 0)
    pts += arc(xr, yb + r, 180, 270)
    line(ax, pts, role, lw=1.4)
fig, ax = canvas(66)
vbrace(ax, 3, 9, 28, 62, 'encre')
box(ax, 13, 47, 42, 13, 'sujet', label=r'$x + y = 5$', size='m')
box(ax, 13, 30, 42, 13, 'autre', label=r'$2x + y = 8$', size='m')
text(ax, 72, 62, r'pour $(1, 4)$', 'encre', 's')
text(ax, 72, 53.5, '✓ vrai', 'resultat', 'm')
text(ax, 72, 36.5, '✗ faux', 'limite', 'm')
box(ax, 8, 6, 72, 11, 'encre', label='accolade : les deux à la fois', size='s')
save(fig, '24-019')
