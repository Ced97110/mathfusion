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
text(ax, 44, 70, 'système de deux équations', 'encre', 'l')
text(ax, 28, 56, r'$x + y = 5$', 'sujet', 'l'); text(ax, 28, 41, r'$2x + y = 8$', 'varie', 'l')
line(ax, [(47, 62), (51, 60), (51, 50), (54, 48.5), (51, 47), (51, 37), (47, 35)], 'fixe', lw=1.0)
arrow(ax, (55, 48.5), (60, 48.5), 'fixe')
box(ax, 61, 40, 25, 17, 'resultat'); text(ax, 73.5, 51, 'les deux', 'resultat', 's'); text(ax, 73.5, 46, 'vraies', 'resultat', 's'); text(ax, 73.5, 42.5, 'à la fois', 'resultat', 's')
text(ax, 44, 24, r'$ax + by = c$', 'encre', 'l')
text(ax, 44, 17, r'$x$ et $y$ : les deux inconnues', 'sujet', 's'); text(ax, 44, 12, r'$a$, $b$, $c$ : nombres connus', 'fixe', 's')
save(fig, '24-015')
