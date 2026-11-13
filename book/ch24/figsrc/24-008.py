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
fig, ax = canvas(78); s = 9; ox, oy = 15, 13
P = plane(ax, ox, oy, s, 5.4, 6.5, xl=(1, 2, 3, 4, 5), yl=(2, 4, 6))
text(ax, ox + 27, oy - 7.5, 'prix du café (€)', 'fixe', 's'); text(ax, ox - 8, oy + 30, 'prix du croissant (€)', 'fixe', 's', rot=90)
line(ax, [P(0, 5), P(5, 0)], 'sujet', lw=1.6); line(ax, [P(0.75, 6.5), P(4, 0)], 'varie', lw=1.6)
line(ax, [P(3, 0), P(3, 2)], 'encre', dash=True); line(ax, [P(0, 2), P(3, 2)], 'encre', dash=True)
disc(ax, *P(3, 2), 1.7, 'resultat')
text(ax, *at(P, 3, 2, 2.5, 3), 'P (3 ; 2)', 'resultat', 'm', ha='left')
text(ax, *P(1.3, 6.2), r'$D_2$ : $2x+y=8$', 'varie', 's', ha='left'); text(ax, 54, 27, r'$D_1$ : $x+y=5$', 'sujet', 's', ha='left')
save(fig, '24-008')
