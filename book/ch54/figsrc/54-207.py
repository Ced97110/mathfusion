import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def panel(x0, xmin, xmax, f, role, xs, ys, y0):
    # axis, then the curve of f over [xmin, xmax]
    line(ax, [(x0 + xmin * xs - 1, y0), (x0 + xmax * xs + 1, y0)], 'fixe', lw=1.0)
    n = 60
    pts = [(x0 + (xmin + (xmax - xmin) * i / n) * xs, y0 + f(xmin + (xmax - xmin) * i / n) * ys) for i in range(n + 1)]
    line(ax, pts, role, lw=1.4)
# left: x^2 + x + 1, axis at y=34, 9 mm per unit in x, 5 mm per unit in y
panel(20, -2, 1.5, lambda x: x * x + x + 1, 'sujet', 9, 4.5, 34)
# right: x^2 - 3x + 2, roots 1 and 2
panel(48, 0, 3, lambda x: x * x - 3 * x + 2, 'autre', 9, 4.5, 34)
for r in (1, 2):
    disc(ax, 48 + r * 9, 34, 1.3, 'resultat')
    text(ax, 48 + r * 9, 29.5, str(r), 'resultat', 's')
text(ax, 22, 58, r'$x^2+x+1$', 'sujet', 'l')
text(ax, 66, 58, r'$x^2-3x+2$', 'autre', 'l')
text(ax, 22, 21, r'$1-4=-3<0$', 'sujet', 'm')
text(ax, 66, 21, r'$9-8=1>0$', 'autre', 'm')
box(ax, 4, 4, 38, 9, 'sujet', label='irréductible sur ' + r'$\mathbb{R}$', size='s')
box(ax, 46, 4, 38, 9, 'autre', label='réductible sur ' + r'$\mathbb{R}$', size='s')
save(fig, '54-207')
