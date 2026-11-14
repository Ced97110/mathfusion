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
fig, ax = canvas(62); s = 5.5; oy = 16
A = plane(ax, 5, oy, s, 5.4, 6.2); B = plane(ax, 50, oy, s, 5.4, 6.2)
text(ax, 20, 53, 'deux droites différentes', 'encre', 's'); text(ax, 64, 53, 'la même droite', 'limite', 's')
line(ax, [A(0, 5), A(5, 0)], 'sujet', lw=1.4); line(ax, [A(0.9, 6.2), A(4, 0)], 'varie', lw=1.4)
disc(ax, *A(3, 2), 1.6, 'resultat')
text(ax, *A(4.2, 1.8), r'$D_1$', 'sujet', 's'); text(ax, *A(1.3, 6.2), r'$D_2$', 'varie', 's', ha='left')
text(ax, 20, 8, '1 seul point commun', 'resultat', 's')
line(ax, [B(0, 5), B(5, 0)], 'sujet', lw=2.6); line(ax, [B(0, 5), B(5, 0)], 'varie', lw=1.0, dash=True)
for x in (1, 2, 3, 4): disc(ax, *B(x, 5 - x), 0.9, 'limite')
text(ax, *B(2.9, 4.0), r'$x + y = 5$', 'sujet', 's', ha='left'); text(ax, *B(0.3, 1.0), r'$2x + 2y = 10$', 'varie', 's', ha='left')
text(ax, 64, 8, 'tous les points communs', 'limite', 's')
save(fig, '24-014')
