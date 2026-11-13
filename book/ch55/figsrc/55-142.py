import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
U = 8.0   # mm per unit on y
def panel(xa, xb, xmin, xmax, fn, role, title, delta, note, roots):
    fx = lambda v: xa + (v - xmin) / (xmax - xmin) * (xb - xa)
    y0 = 30
    arrow(ax, (xa - 1, y0), (xb + 3, y0), 'fixe', lw=0.8)
    pts = [(fx(xmin + (xmax - xmin) * i / 60), y0 + U * fn(xmin + (xmax - xmin) * i / 60)) for i in range(61)]
    line(ax, pts, role, lw=1.5)
    for r in roots:
        disc(ax, fx(r), y0, 1.4, 'resultat')
    text(ax, (xa + xb) / 2, 68, title, role, 'm', weight='bold')
    text(ax, (xa + xb) / 2, 14, delta, role, 'm')
    text(ax, (xa + xb) / 2, 7, note, 'resultat' if roots else 'fixe', 's')
panel(4, 38, 1, 4, lambda v: v * v - 5 * v + 6, 'sujet', r'$x^2-5x+6$', r'$\Delta=1>0$', '2 racines réelles', (2, 3))
panel(50, 84, -1.5, 1.5, lambda v: v * v + 1, 'autre', r'$x^2+1$', r'$\Delta=-4<0$', 'aucune racine réelle', ())
assert 25 - 24 == 1 and 0 - 4 * 1 * 1 == -4
save(fig, '55-142')
