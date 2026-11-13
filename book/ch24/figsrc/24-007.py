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
fig, ax = canvas(80); u = 8; x0 = 14; yM, yL, h = 50, 28, 10
text(ax, 7, yM + 5, 'mardi', 'encre', 'm'); text(ax, 7, yL + 5, 'lundi', 'encre', 'm')
for y in (yM, yL):
    box(ax, x0, y, 2 * u, h, 'fixe', label='croissant', size='s')
    box(ax, x0 + 2 * u, y, 3 * u, h, 'sujet', label='café', size='s')
box(ax, x0 + 5 * u, yM, 3 * u, h, 'varie', label='café', size='s')
brace(ax, x0, x0 + 8 * u, yM + h, 'encre', label='8 €', down=False)
brace(ax, x0, x0 + 5 * u, yL, 'encre', label='5 €')
brace(ax, x0 + 5 * u, x0 + 8 * u, yM, 'varie', label='8 € − 5 € = 3 €')
arrow(ax, (22, yM - 0.5), (22, yL + h + 0.5), 'fixe', both=True); text(ax, 25, 44, 'même croissant', 'fixe', 's', ha='left')
box(ax, 14, 8, 30, 9, 'resultat', label='café = 3 €'); box(ax, 48, 8, 36, 9, 'resultat', label='croissant = 5 − 3 = 2 €', size='s')
save(fig, '24-007')
