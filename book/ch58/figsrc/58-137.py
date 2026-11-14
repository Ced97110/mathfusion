import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
n = lambda v: str(v).replace('-', '−')
t2 = lambda t: '(' + ', '.join(n(v) for v in t) + ')'
vs = [(1, 2), (0, 1), (3, 0)]
cs = [2, 3, -1]
prods = [(c * v[0], c * v[1]) for c, v in zip(cs, vs)]
tot = (sum(p[0] for p in prods), sum(p[1] for p in prods))
assert prods == [(2, 4), (0, 3), (-3, 0)] and tot == (-1, 7)
text(ax, 22, 73, '1. multiplier chacun', 'varie', 'm')
text(ax, 68, 73, 'produits', 'sujet', 'm')
for c, v, pr, y in zip(cs, vs, prods, [57, 45, 33]):
    box(ax, 2, y, 40, 9, 'varie', label=rf'${n(c)}\times{t2(v)}$')
    arrow(ax, (44, y + 4.5), (56, y + 4.5), 'varie')
    box(ax, 58, y, 28, 9, 'sujet', label=t2(pr))
brace(ax, 58, 86, 31, 'encre', depth=2.0)
text(ax, 22, 21, '2. additionner', 'resultat', 'm')
arrow(ax, (44, 21), (56, 21), 'resultat')
box(ax, 58, 15.5, 28, 9, 'resultat', label=t2(tot), weight='bold')
save(fig, '58-137')
