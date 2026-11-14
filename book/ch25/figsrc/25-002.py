import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

fig, ax = canvas(84)
for (x, y) in [(2, 44), (46, 44), (2, 2)]:
    box(ax, x, y, 40, 38, 'fixe', fill=False)
box(ax, 46, 2, 40, 38, 'sujet')
text(ax, 22, 77, 'segment', 'fixe', 'm', weight='bold')
disc(ax, 8, 63, 1.3, 'fixe'); disc(ax, 36, 63, 1.3, 'fixe'); line(ax, [(8, 63), (36, 63)], 'fixe', lw=1.3)
text(ax, 22, 52, 'a une longueur', 'fixe', 's')
text(ax, 66, 77, 'demi-droite', 'fixe', 'm', weight='bold')
disc(ax, 52, 63, 1.3, 'fixe'); arrow(ax, (52, 63), (82, 63), 'fixe')
text(ax, 66, 52, 'sans fin d’un côté', 'fixe', 's')
text(ax, 22, 35, 'droite', 'fixe', 'm', weight='bold')
arrow(ax, (22, 21), (6, 21), 'fixe'); arrow(ax, (22, 21), (38, 21), 'fixe')
text(ax, 22, 9, 'sans fin des deux côtés', 'fixe', 's')
text(ax, 66, 35, 'angle', 'sujet', 'm', weight='bold')
V = (52, 14)
arrow(ax, V, (82, 14), 'sujet', lw=1.3)
arrow(ax, V, (V[0] + 27 * math.cos(math.radians(40)), V[1] + 27 * math.sin(math.radians(40))), 'sujet', lw=1.3)
arc(ax, V, 8, 0, 40, 'varie'); disc(ax, V[0], V[1], 1.3, 'sujet')
text(ax, 66, 6, 'deux demi-droites, un point', 'sujet', 's')
save(fig, '25-002')
