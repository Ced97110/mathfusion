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
fig, ax = canvas(94)
box(ax, 6, 78, 76, 11, 'sujet', label=r'$P$ est sur $D_1$ et sur $D_2$')
arrow(ax, (44, 77), (44, 69.5), 'fixe')
box(ax, 6, 48, 76, 20, 'varie')
text(ax, 44, 63, 'étape clé', 'varie', 'm', weight='bold'); text(ax, 44, 58.5, 'être sur une droite', 'varie', 'm'); text(ax, 44, 54, '= vérifier son équation', 'varie', 'm')
arrow(ax, (24, 47), (24, 41.5), 'fixe'); arrow(ax, (64, 47), (64, 41.5), 'fixe')
box(ax, 6, 29, 36, 11, 'resultat', label='3 + 2 = 5  (lundi)', size='s'); box(ax, 46, 29, 36, 11, 'resultat', label=r'2 × 3 + 2 = 8  (mardi)', size='s')
arrow(ax, (24, 28), (40, 21), 'fixe'); arrow(ax, (64, 28), (48, 21), 'fixe')
box(ax, 6, 8, 76, 12, 'resultat', label=r'$x=3$ et $y=2$ : les prix')
save(fig, '24-013')
