import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
Y0, Y1 = 14, 50

def panel(xa, xb, fn, pts, role, title, formula, npts):
    fx = lambda v: xa + (v + 0.4) / 2.8 * (xb - xa)
    fy = lambda v: Y0 + v / 7.0 * (Y1 - Y0)
    line(ax, [(xa, Y0), (xb, Y0)], 'fixe')
    line(ax, [(xa, Y0), (xa, Y1 + 3)], 'fixe')
    curve = [(fx(-0.4 + 2.8 * i / 60), fy(fn(-0.4 + 2.8 * i / 60))) for i in range(61)]
    line(ax, curve, role, lw=1.5)
    for (px, py) in pts:
        disc(ax, fx(px), fy(py), 1.3, 'resultat')
        text(ax, fx(px), Y0 - 3, f'{px}', 'fixe', 's')
    text(ax, (xa + xb) / 2, 60, title, role, 'm', weight='bold')
    text(ax, (xa + xb) / 2, 7.5, formula, role, 'm')

panel(6, 40, lambda v: 1 + 2 * v, [(0, 1), (1, 3)], 'sujet', r'droite : $n=1$', r'$1+2x$', 2)
panel(50, 84, lambda v: v * v + 1, [(0, 1), (1, 2), (2, 5)], 'autre', r'parabole : $n=2$', r'$x^2+1$', 3)
text(ax, 23, 2.6, r'$n+1=2$ points', 'resultat', 's')
text(ax, 67, 2.6, r'$n+1=3$ points', 'resultat', 's')
save(fig, '55-118')
