import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
O, u = (34, 26), 9
x0, x1, y0, y1 = 6, 72, 4, 58
for a, b, c, d in ((x0, y0, O[0], O[1]), (O[0], y0, x1, O[1]), (x0, O[1], O[0], y1), (O[0], O[1], x1, y1)):
    poly(ax, [(a, b), (c, b), (c, d), (a, d)], 'resultat')
line(ax, [(x0, O[1]), (x1, O[1])], 'limite', lw=2); line(ax, [(O[0], y0), (O[0], y1)], 'limite', lw=2)
disc(ax, O[0] + 2 * u, O[1] + 3 * u, 1.5, 'sujet')
text(ax, O[0] + 2 * u, O[1] + 3 * u - 4, '2 × 3 = 6', 'sujet', 's')
disc(ax, O[0] + 2 * u, O[1], 1.5, 'limite')
text(ax, O[0] + 2 * u, O[1] - 4.5, '2 × 0 = 0', 'limite', 's')
text(ax, 20, 14, 'produit ≠ 0', 'resultat', 's')
text(ax, 20, 40, 'produit ≠ 0', 'resultat', 's')
text(ax, 44, 62, 'x·y = 0 sur les axes', 'limite', 's')
save(fig, '70-173')
