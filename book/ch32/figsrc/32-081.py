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
cx, cy, r = 24, 31, 21
circ_axes(ax, cx, cy, r)
arc(ax, cx, cy, r, -90, 90, 'sujet', 1.8)
for a, lab, sv, dy in ((30, 'α = 30°', 'sin = 0,5', 1), (-11.54, 'α = −11,54°', 'sin = −0,2', -1)):
    x, y = P(cx, cy, r, a)
    line(ax, [(cx, cy), (x, y)], 'resultat', 0.8, True)
    arc(ax, cx, cy, 9, 0, a, 'resultat', 1.0)
    disc(ax, x, y, 1.4, 'resultat')
    text(ax, 52, y + (3 if dy > 0 else -1) * 1.0 + (0 if dy > 0 else -0.0), lab, 'resultat', 'm', ha='left')
    text(ax, 52, y + (-1.5 if dy > 0 else -5.5), sv, 'fixe', 's', ha='left')
text(ax, cx + 6, cy + r + 3.5, '90°', 'sujet', 's')
text(ax, cx + 7, cy - r - 3.5, '−90°', 'sujet', 's')
text(ax, cx - 11, cy + 7, 'hors touche', 'fixe', 's')
text(ax, 66, 57, 'un seul angle', 'sujet', 'm')
save(fig, '32-081')
