import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# left panel: two polynomials of degree <= 2 through 3 points (x = 0, 1, 2)
X0, X1, Y0, Y1 = 8, 40, 12, 52
fx = lambda v: X0 + (v + 0.4) / 3.0 * (X1 - X0)
fy = lambda v: Y0 + v / 6.0 * (Y1 - Y0)
line(ax, [(X0, Y0), (X1, Y0)], 'fixe')
line(ax, [(X0, Y0), (X0, Y1)], 'fixe')
pts = [(fx(-0.4 + 2.6 * i / 60), fy((-0.4 + 2.6 * i / 60) ** 2 + 1)) for i in range(61)]
line(ax, pts, 'sujet', lw=1.6)
line(ax, pts, 'varie', lw=0.8, dash=True)
for v in (0, 1, 2):
    disc(ax, fx(v), fy(v * v + 1), 1.3, 'resultat')
    text(ax, fx(v), Y0 - 3, f'{v}', 'fixe', 's')
text(ax, 24, 58, r'deux polynômes $f$, $g$', 'encre', 'm')
text(ax, 24, 3.5, 'mêmes valeurs en 3 points', 'resultat', 's')
# right panel: the difference f - g has 3 roots, degree <= 2, so it is zero
text(ax, 66, 58, r'$f-g$', 'encre', 'm')
f = numberline(ax, 52, 76, 36, 0, 2, arrow_right=False)
for v in (0, 1, 2):
    disc(ax, f(v), 36, 1.3, 'resultat')
box(ax, 52, 20, 30, 7, 'resultat', label='3 racines', size='m')
box(ax, 52, 8, 30, 7, 'sujet', label=r'degré $\leq 2$ : nulle', size='s')
arrow(ax, (67, 33), (67, 27.8), 'varie')
arrow(ax, (67, 20), (67, 15.8), 'varie')
save(fig, '55-117')
