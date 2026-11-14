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
fig, ax = canvas(64)
def row(y, name, items, tot):
    text(ax, 8, y + 14, name, 'encre', 'm'); x = 2
    for lab, w, role in items:
        box(ax, x, y, w, 10, role, label=lab, size='s'); x += w + 1.5
    text(ax, 69, y + 5, '= ' + tot, 'encre', 'm'); text(ax, 82, y + 5, 'juste', 'resultat', 's')
row(40, 'lundi', [('café 1 €', 16, 'sujet'), ('croissant 4 €', 22, 'autre')], '5 €')
row(10, 'mardi', [('café 2 €', 16, 'sujet'), ('café 2 €', 16, 'sujet'), ('croissant 4 €', 22, 'autre')], '8 €')
arrow(ax, (10, 39), (10, 21.5), 'limite', both=True)
text(ax, 13, 30.5, '1 € ≠ 2 € : impossible', 'limite', 's', ha='left')
save(fig, '24-006')
