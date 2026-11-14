import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, 'A : 3 × 3, coefficients dans ℚ', 'encre', 'm')
x0, ytop, cw, ch = 28, 61, 12, 9
rows = [[-1, -2, 6], [-1, 0, 3], [-1, -1, 4]]
for r in range(3):
    for c in range(3):
        box(ax, x0 + c * cw, ytop - (r + 1) * ch, cw, ch, 'sujet', label=str(rows[r][c]).replace('-', '−'), size='m')
for sgn, xx in ((-1, x0 - 1.5), (1, x0 + 3 * cw + 1.5)):
    line(ax, [(xx - sgn * 1.5, ytop + 0.5), (xx, ytop + 0.5), (xx, ytop - 3 * ch - 0.5), (xx - sgn * 1.5, ytop - 3 * ch - 0.5)], 'encre', lw=0.9)
names = [r'on forme $\lambda1-A$', 'la réduire', 'facteurs\ninvariants']
xs = [2, 32, 62]
for x, nm, role in zip(xs, names, ['varie', 'varie', 'resultat']):
    box(ax, x, 15, 24, 14, role, label=nm, size='s')
for i in range(2):
    arrow(ax, (xs[i] + 24.3, 22), (xs[i + 1] - 0.3, 22), 'varie')
text(ax, 72, 8, r'$1,\ \lambda-1,\ (\lambda-1)^2$', 'resultat', 's')
save(fig, '60-203')
