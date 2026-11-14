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
fig, ax = canvas(78); s = 11; ox, oy = 15, 14
P = plane(ax, ox, oy, s, 4.5, 4.5, xl=(1, 2, 3, 4), yl=(1, 2, 3, 4))
text(ax, ox + 25, oy - 7.5, 'café (€)', 'fixe', 's'); text(ax, ox - 8, oy + 25, 'croissant (€)', 'fixe', 's', rot=90)
line(ax, [P(3, 0), P(3, 2)], 'fixe', dash=True)
arrow(ax, P(2.85, 2), P(0.05, 2), 'sujet', lw=1.4)
disc(ax, *P(3, 2), 1.7, 'resultat'); text(ax, *at(P, 3, 2, 2.5, 3), 'P (3 ; 2)', 'resultat', 'm', ha='left')
text(ax, *P(1.4, 2.45), 'ordonnée : 2', 'sujet', 'm'); text(ax, *P(3.15, 1.0), 'abscisse : 3', 'fixe', 's', ha='left')
text(ax, ox + 3, oy + 4.4 * s, "lue sur l'axe vertical", 'sujet', 's', ha='left')
save(fig, '24-091')
