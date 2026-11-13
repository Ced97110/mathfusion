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
fig, ax = canvas(76); u = 8; x0 = 14
def bar(y, parts, tot, eq, name):
    text(ax, x0 + sum(w for w, _ in parts) * u / 2, y + 17, eq, 'encre', 'l')
    text(ax, 7, y + 5, name, 'encre', 'm')
    x = x0
    for w, sym in parts:
        box(ax, x, y, w * u, 10, 'sujet' if sym == 'x' else 'autre', label=r'$' + sym + r'$')
        x += w * u
    brace(ax, x0, x, y, 'encre', label=tot)
bar(52, [(3, 'x'), (2, 'y')], '5 €', r'$x + y = 5$', 'lundi')
bar(20, [(3, 'x'), (3, 'x'), (2, 'y')], '8 €', r'$2x + y = 8$', 'mardi')
save(fig, '24-003')
