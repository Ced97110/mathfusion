import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(52)
def fig1(cx, n, ang, fixed, role):
    cy, R = 28, 11
    poly(ax, pg(cx, cy, R, n), 'fixe')
    line(ax, [pol(cx, cy, R + 3, ang), pol(cx, cy, R + 3, ang + 180)], role, lw=1.2)
    for a in fixed:
        x, y = pol(cx, cy, R, a); disc(ax, x, y, 2.0, role)
fig1(15, 5, 90, (90,), 'sujet')
fig1(44, 6, 90, (90, 270), 'varie')
fig1(73, 6, 120, (), 'resultat')
text(ax, 15, 47, r'$n = 5$ impair', 'sujet', 's'); text(ax, 58, 47, r'$n = 6$ pair', 'fixe', 's')
text(ax, 15, 8, '1 sommet fixe', 'sujet', 's'); text(ax, 44, 8, '2 sommets fixes', 'varie', 's'); text(ax, 73, 8, '0 sommet fixe', 'resultat', 's')
save(fig, '44-231')
