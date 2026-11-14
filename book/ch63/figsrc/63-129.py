import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
xs = [2, 32, 62]

def row(y, boxes, labs, head):
    for x, (t, r) in zip(xs, boxes):
        box(ax, x, y, 24, 11, role=r, label=t)
    for i, l in enumerate(labs):
        arrow(ax, (xs[i] + 24.8, y + 5.5), (xs[i + 1] - 0.8, y + 5.5), 'varie')
        text(ax, xs[i] + 27.5, y + 9.2, l, 'varie', 's')
    text(ax, 44, y + 16.5, head, 'encre', 's')

row(30, [('H = {1, σ}', 'sujet'), ('K = ℚ(√3)', 'autre'), ('Gal(E/K) = H', 'resultat')],
    ['Inv', 'Gal'], '(2) + théorème 4.7 : H = Gal(E/K)')
row(4, [('K = ℚ(√3)', 'autre'), ('Gal(E/K)', 'sujet'), ('Inv(Gal) = K', 'resultat')],
    ['Gal', 'Inv'], '(1) + théorème 4.7 : K = Inv(Gal)')
save(fig, '63-129')
