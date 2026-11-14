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
fig, ax = canvas(76)
text(ax, 44, 66, r'$D_1$', 'sujet', 22)
arrow(ax, (40, 58), (24, 47.5), 'sujet'); arrow(ax, (48, 58), (64, 47.5), 'varie')
box(ax, 9, 32, 30, 14, 'sujet', label='D', size='xl'); box(ax, 49, 32, 30, 14, 'varie', label='1', size='xl')
text(ax, 24, 26, 'lettre de « droite »', 'sujet', 's'); text(ax, 64, 26, 'numéro de la droite', 'varie', 's'); text(ax, 64, 22, 'pas une puissance', 'varie', 's')
text(ax, 44, 13, r'droite des points où $x+y=5$', 'encre', 'm')
text(ax, 44, 6, r'$(0,5)\in D_1$ : 0 + 5 = 5', 'resultat', 's')
save(fig, '24-009')
