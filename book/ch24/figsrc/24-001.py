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
fig, ax = canvas(62)
rows = [(46, 'lundi', ['croissant', 'café'], '5 €'), (26, 'mardi', ['croissant', 'café', 'café'], '8 €')]
for y, name, items, tot in rows:
    text(ax, 7, y + 5, name, 'encre', 'm')
    x = 14
    for i, it in enumerate(items):
        w = 22 if it == 'croissant' else 14
        role = 'fixe' if it == 'croissant' else 'sujet'
        if name == 'mardi' and i == 2: role = 'varie'
        box(ax, x, y, w, 10, role, label=it, size='s'); x += w + 1.5
    text(ax, 80, y + 5, '= ' + tot, 'encre', 'l')
text(ax, 60, 21, 'un café de plus', 'varie', 's')
text(ax, 44, 8, '2 prix inconnus, 2 totaux', 'encre', 'm')
save(fig, '24-001')
