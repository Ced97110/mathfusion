import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(66)
c1, c2, cy, R = 22, 66, 36, 14
poly(ax, pg(c1, cy, R, 5), 'fixe')
for k in range(5):
    a = 90 + 72 * k; line(ax, [pol(c1, cy, R + 3, a), pol(c1, cy, -(R * math.cos(math.radians(36)) + 3), a)] if False else [pol(c1, cy, R + 3, a), pol(c1, cy, R * math.cos(math.radians(36)) + 3, a + 180)], 'sujet', lw=1.2)
poly(ax, pg(c2, cy, R, 6), 'fixe')
for k in range(3):
    a = 90 + 60 * k; line(ax, [pol(c2, cy, R + 3, a), pol(c2, cy, R + 3, a + 180)], 'varie', lw=1.2)
    a = 120 + 60 * k; m = R * math.cos(math.radians(30)) + 3
    line(ax, [pol(c2, cy, m, a), pol(c2, cy, m, a + 180)], 'resultat', lw=1.2)
text(ax, c1, 8, r'$n = 5$', 'encre', 'l'); text(ax, c1, 2.5, '5 axes, 1 sorte', 'sujet', 's')
text(ax, c2, 8, r'$n = 6$', 'encre', 'l'); text(ax, c2, 2.5, '3 + 3 axes, 2 sortes', 'fixe', 's')
text(ax, c1, 62, 'sommet – côté', 'sujet', 's')
text(ax, c2, 63.5, 'sommet – sommet', 'varie', 's'); text(ax, c2, 59.5, 'côté – côté', 'resultat', 's')
save(fig, '44-230')
