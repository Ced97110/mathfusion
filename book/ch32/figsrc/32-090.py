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

fig, ax = canvas(62)
cx, cy, r = 26, 32, 21
circ_axes(ax, cx, cy, r)
arc(ax, cx, cy, 14, 0, 11.54, 'autre', 1.4)
arc(ax, cx, cy, 14, 0, -11.54, 'sujet', 1.6)
pt(ax, cx, cy, r, 11.54, 'autre', 1.4)
pt(ax, cx, cy, r, -11.54, 'sujet', 1.6)
text(ax, 51, cy + 8, '11,54°', 'autre', 'm', ha='left')
text(ax, 51, cy + 4, 'sin = 0,2', 'autre', 's', ha='left')
text(ax, 51, cy - 4, 'sin = −0,2', 'sujet', 's', ha='left')
text(ax, 51, cy - 8, '−11,54°', 'sujet', 'm', ha='left')
text(ax, 44, 6, 'sous l’axe : angle négatif', 'sujet', 'm')
text(ax, cx, 59, 'touche : −90° à 90°', 'fixe', 's')
save(fig, '32-090')
