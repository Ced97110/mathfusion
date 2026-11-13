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
fig, ax = canvas(70)
box(ax, 6, 48, 76, 16, 'fixe'); text(ax, 44, 58, 'la droite où deux cafés', 'fixe', 'm'); text(ax, 44, 53, 'plus un croissant font 8 €', 'fixe', 'm')
arrow(ax, (44, 47), (44, 38.5), 'varie'); text(ax, 62, 42.5, "s'écrit", 'varie', 's')
box(ax, 28, 22, 32, 15, 'varie', label=r'$D_2$', size=16)
text(ax, 44, 17.5, 'deux caractères : D et 2', 'varie', 's')
text(ax, 44, 10, r'$(4,0)\in D_2$ : $2\times4+0=8$', 'resultat', 'm'); text(ax, 44, 4.5, '∈ : appartient à', 'fixe', 's')
save(fig, '24-011')
