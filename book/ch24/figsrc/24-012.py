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
fig, ax = canvas(76); s = 8; ox, oy = 12, 12
P = plane(ax, ox, oy, s, 5.2, 6.5, xl=(3,), yl=(2,))
line(ax, [P(0, 5), P(5, 0)], 'sujet', lw=1.5); line(ax, [P(0.75, 6.5), P(4, 0)], 'varie', lw=1.5)
line(ax, [P(3, 0), P(3, 2)], 'encre', dash=True); line(ax, [P(0, 2), P(3, 2)], 'encre', dash=True)
disc(ax, *P(3, 2), 2.2, 'resultat'); text(ax, *at(P, 3, 2, 3.5, 5), 'P', 'resultat', 16)
text(ax, *P(4.0, 1.6), r'$D_1$', 'sujet', 's', ha='left'); text(ax, *P(1.2, 6.5), r'$D_2$', 'varie', 's', ha='left')
box(ax, 60, 52, 26, 10, 'resultat', label='P (3 ; 2)'); text(ax, 73, 46, 'un seul point', 'encre', 's')
text(ax, 73, 38, r'sur $D_1$ et $D_2$', 'encre', 's')
text(ax, 73, 29, 'café : 3 €', 'sujet', 's'); text(ax, 73, 24, 'croissant : 2 €', 'sujet', 's')
save(fig, '24-012')
