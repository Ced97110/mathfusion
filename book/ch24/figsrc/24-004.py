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
fig, ax = canvas(80)
P = plane(ax, 14, 12, 11, 5.4, 5.4, xl=(1, 2, 3, 4, 5))
text(ax, 14 + 5.4 * 11 + 6, 12, r'$x$', 'fixe', 'm'); text(ax, 14, 12 + 5.4 * 11 + 6.5, r'$y$', 'fixe', 'm')
arrow(ax, P(0, 5), P(5, 0), 'sujet', lw=1.4, both=True)
for x, y, lab in [(1, 4, '(1 ; 4)'), (2, 3, '(2 ; 3)'), (4.5, 0.5, '(4,5 ; 0,5)')]:
    disc(ax, *P(x, y), 1.4, 'resultat')
    text(ax, *at(P, x, y, 1.8, 2.8), lab, 'resultat', 's', ha='left')
text(ax, *P(3.8, 4.4), r'$x + y = 5$', 'sujet', 'm')
text(ax, 62, 48.5, 'infinité de couples', 'resultat', 's')
save(fig, '24-004')
