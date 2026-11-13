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

fig, ax = canvas(60)
cx, cy, r = 21, 30, 17
circ_axes(ax, cx, cy, r)
pt(ax, cx, cy, r, 30, 'sujet', 1.5)
pt(ax, cx, cy, r, 210, 'limite', 1.5)
arc(ax, cx, cy, r + 3, 30, 380, 'resultat', 1.1)
arrow(ax, P(cx, cy, r + 3, 376), P(cx, cy, r + 3, 390), 'resultat')
arc(ax, cx, cy, 10, 30, 205, 'limite', 1.1)
arrow(ax, P(cx, cy, 10, 200), P(cx, cy, 10, 210), 'limite')
text(ax, 30, 36.5, '30°', 'sujet', 'm')
text(ax, 13, 24.5, '210°', 'limite', 'm')
text(ax, 47, 46, '+ 360° : 390°', 'resultat', 'm', ha='left')
text(ax, 47, 41.5, 'sin = 0,5 : vrai', 'resultat', 's', ha='left')
text(ax, 47, 23, '+ 180° : 210°', 'limite', 'm', ha='left')
text(ax, 47, 18.5, 'sin = −0,5 : faux', 'limite', 's', ha='left')
text(ax, 47, 6, 'tangente : pas de 180°', 'fixe', 's', ha='left')
save(fig, '32-084')
