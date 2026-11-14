import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    n = max(8, int(abs(a1 - a0) / 4))
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts[:-1], role, lw)
    arrow(ax, pts[-2], pts[-1], role, lw)

fig, ax = canvas(66)
# left: rotation, one fixed point
cx, cy = 22, 38
box(ax, 2, 14, 40, 50, 'fixe', fill=False, dash=True)
arc(ax, cx, cy, 11, 0, 270, 'varie', 1.1)
disc(ax, cx, cy, 1.8, 'resultat')
text(ax, cx, cy - 6, r'$c$ fixe', 'resultat', 'm')
text(ax, cx, 58, r'$\theta\neq 0$', 'sujet', 'l')
text(ax, cx, 8, 'un seul point fixe', 'resultat', 's')
# right: translation, no fixed point
box(ax, 46, 14, 40, 50, 'fixe', fill=False, dash=True)
for (x, y) in [(52, 26), (52, 44), (66, 35)]:
    disc(ax, x, y, 1.2, 'limite')
    arrow(ax, (x + 1.5, y + 0.4), (x + 15, y + 5), 'limite')
text(ax, 66, 58, r'$\theta=0,\ b\neq 0$', 'limite', 'l')
text(ax, 66, 8, 'tous les points avancent', 'limite', 's')
save(fig, '74-051')
