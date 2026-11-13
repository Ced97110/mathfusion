import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def plane(ax, ox, oy, s, xm, ym, xl=(), yl=(), size='s'):
    arrow(ax, (ox, oy), (ox + xm * s + 3, oy), 'fixe', lw=0.9)
    arrow(ax, (ox, oy), (ox, oy + ym * s + 3), 'fixe', lw=0.9)
    for v in range(1, int(xm) + 1):
        ax.plot([ox + v * s] * 2, [oy - 1, oy + 1], color=COL['fixe'], lw=0.7, zorder=1.5)
        if v in xl: text(ax, ox + v * s, oy - 3.2, str(v), 'fixe', size)
    for v in range(1, int(ym) + 1):
        ax.plot([ox - 1, ox + 1], [oy + v * s] * 2, color=COL['fixe'], lw=0.7, zorder=1.5)
        if v in yl: text(ax, ox - 3, oy + v * s, str(v), 'fixe', size)
    return lambda x, y: (ox + x * s, oy + y * s)

def at(P, x, y, dx=0.0, dy=0.0):
    p = P(x, y); return (p[0] + dx, p[1] + dy)
fig, ax = canvas(84); s = 9; ox, oy = 15, 18
P = plane(ax, ox, oy, s, 5.6, 5.6, xl=(3, 5), yl=(3, 5))
line(ax, [P(0, 5), P(5, 0)], 'sujet', lw=1.6)
for x, y, lab, role in [(0, 5, '0 + 5 = 5', 'resultat'), (5, 0, '5 + 0 = 5', 'resultat'), (3, 3, '3 + 3 = 6 ≠ 5', 'limite')]:
    disc(ax, *P(x, y), 1.5, role)
    text(ax, *at(P, x, y, 2.6, 2.6 if x == 0 else 0.8), lab, role, 's', ha='left')
text(ax, *P(1.0, 1.4), r'$D_1$ : $x+y=5$', 'sujet', 's', ha='left')
text(ax, 44, 9, 'sur la droite : vrai', 'resultat', 's'); text(ax, 44, 4.5, 'hors de la droite : faux', 'limite', 's')
save(fig, '24-010')
