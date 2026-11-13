import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
u = 2.4; X = 5 * u; B = 3 * u; oy = 20
def panel(ox, expr, status, k):
    box(ax, ox, oy, X, X, 'sujet', True, label=r'$x^2$' if k == 0 else None, size='s', r=0.3)
    box(ax, ox + X, oy, B, X, 'fixe', True, label=r'$3x$' if k == 0 else None, size='s', r=0.3)
    box(ax, ox, oy + X, X, B, 'fixe', True, label=r'$3x$' if k == 0 else None, size='s', r=0.3)
    cx, cy = ox + X, oy + X
    if k == 0:
        box(ax, cx, cy, B, B, 'fixe', False, dash=True, r=0.3)
    elif k == 1:
        box(ax, cx, cy, B, B, 'resultat', True, label='9', size='s', r=0.3)
    else:
        h = B * 5 / 9
        box(ax, cx, cy, B, h, 'varie', True, label='5', size='s', r=0.3)
        box(ax, cx, cy + h, B, B - h, 'fixe', False, dash=True, r=0.3)
    text(ax, ox + (X + B) / 2, 13, expr, 'encre', 's')
    text(ax, ox + (X + B) / 2, 7, status, 'resultat' if k == 1 else 'fixe', 's')
panel(3, r'$x^2+6x$', 'il manque 9', 0)
panel(32, r'$x^2+6x+9$', 'carré complet', 1)
panel(61, r'$x^2+6x+5$', 'il manque 4', 2)
save(fig, '23-011')
