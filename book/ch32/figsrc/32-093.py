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

fig, ax = canvas(66)
cx, cy, r = 44, 33, 21
circ_axes(ax, cx, cy, r)
line(ax, [P(cx, cy, r + 5, 149.04), P(cx, cy, r + 5, -30.96)], 'varie', 1.1)
arc(ax, cx, cy, 12, 0, -30.96, 'sujet', 1.3)
arc(ax, cx, cy, 14, 0, 149.04, 'autre', 1.3)
pt(ax, cx, cy, r, -30.96, 'sujet', 1.5); pt(ax, cx, cy, r, 149.04, 'autre', 1.5)
text(ax, 66, 17, '−30,96°', 'sujet', 'm', ha='left')
text(ax, 22, 48, '149,04°', 'autre', 'm', ha='right')
text(ax, 76, 44, 'pente −0,6', 'varie', 'm')
text(ax, 44, 5, 'deux angles : 180° d’écart', 'fixe', 's')
save(fig, '32-093')
