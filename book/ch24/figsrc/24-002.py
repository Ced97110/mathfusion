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
fig, ax = canvas(66)
for cx, name, sym, role, cap in [(24, 'café', 'x', 'sujet', "prix d'un café"), (64, 'croissant', 'y', 'autre', "prix d'un croissant")]:
    box(ax, cx - 13, 48, 26, 10, role, label=name)
    arrow(ax, (cx, 47), (cx, 36), role)
    disc(ax, cx, 28, 7, role, label=r'$' + sym + r'$', size='xl')
    text(ax, cx, 15, cap, role, 's'); text(ax, cx, 10.5, 'en euros', role, 's')
save(fig, '24-002')
