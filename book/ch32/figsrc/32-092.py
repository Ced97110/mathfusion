import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def P(cx, cy, r, d):
    return (cx + r * math.cos(math.radians(d)), cy + r * math.sin(math.radians(d)))
def arc(ax, cx, cy, r, a0, a1, role, lw=0.9, dash=False, n=90):
    line(ax, [P(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def circ_axes(ax, cx, cy, r, ext=3):
    line(ax, [(cx - r - ext, cy), (cx + r + ext, cy)], "fixe", 0.5)
    line(ax, [(cx, cy - r - ext), (cx, cy + r + ext)], "fixe", 0.5)
    arc(ax, cx, cy, r, 0, 360, "fixe", 0.8)
def pt(ax, cx, cy, r, d, role, rr=1.3):
    x, y = P(cx, cy, r, d); disc(ax, x, y, rr, role)

fig, ax = canvas(74)
cx, cy, r = 44, 37, 22
circ_axes(ax, cx, cy, r)
xl = cx - 2.2
line(ax, [(xl, cy - r), (xl, cy + r)], 'varie', 1.1, True)
arc(ax, cx, cy, 10, 0, 95.74, 'sujet', 1.3)
arc(ax, cx, cy, 13, 0, -95.74, 'autre', 1.3)
pt(ax, cx, cy, r, 95.74, 'sujet', 1.5); pt(ax, cx, cy, r, -95.74, 'autre', 1.5)
text(ax, 28, 60, '95,74°', 'sujet', 'm')
text(ax, 28, 14, '−95,74°', 'autre', 'm')
text(ax, 76, 43, 'cos = −0,1', 'varie', 'm')
text(ax, 44, 5, 'angles de −180° à 180°', 'fixe', 's')
save(fig, '32-092')
