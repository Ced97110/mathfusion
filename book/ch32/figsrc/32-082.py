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

fig, ax = canvas(68)
cx, cy, r = 36, 34, 20
circ_axes(ax, cx, cy, r)
line(ax, [(cx, cy - r - 3), (cx, cy + r + 3)], 'varie', 1.2, True)
a = P(cx, cy, r, 30); b = P(cx, cy, r, 150)
line(ax, [a, b], 'fixe', 0.8, True)
arc(ax, cx, cy, 9, 0, 30, 'sujet', 1.2)
arc(ax, cx, cy, 13, 0, 150, 'resultat', 1.2)
disc(ax, a[0], a[1], 1.4, 'sujet'); disc(ax, b[0], b[1], 1.4, 'resultat')
text(ax, 58, a[1] + 2, 'α = 30°', 'sujet', 'm', ha='left')
text(ax, 14, b[1] + 2.5, '180° − α', 'resultat', 's', ha='right')
text(ax, 14, b[1] - 1.5, '= 150°', 'resultat', 's', ha='right')
text(ax, cx, cy + 6.5, 'même hauteur', 'fixe', 's')
text(ax, cx, cy - r - 6, 'axe vertical : reflet', 'varie', 's')
text(ax, 44, 5, 'cos : −α    tan : α + 180°', 'fixe', 's')
save(fig, '32-082')
