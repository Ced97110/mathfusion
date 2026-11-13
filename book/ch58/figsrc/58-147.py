import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
n = lambda v: str(v).replace('-', '−')
t2 = lambda t: '(' + ', '.join(n(v) for v in t) + ')'
vs = [(3, 1), (1, 2), (-1, 3)]
cs = [-1, 2, -1]
prods = [(c * v[0], c * v[1]) for c, v in zip(cs, vs)]
tot = (sum(p[0] for p in prods), sum(p[1] for p in prods))
assert prods == [(-3, -1), (2, 4), (1, -3)] and tot == (0, 0)
text(ax, 22, 79, '1. multiplier', 'varie', 'm')
for c, v, pr, y in zip(cs, vs, prods, [62, 50, 38]):
    box(ax, 2, y, 40, 9, 'varie', label=rf'${n(c)}\times{t2(v)}$')
    arrow(ax, (44, y + 4.5), (56, y + 4.5), 'varie')
    box(ax, 58, y, 28, 9, 'sujet', label=t2(pr))
text(ax, 22, 29, '2. additionner', 'resultat', 'm')
text(ax, 72, 29.5, r'$-3+2+1=0$', 'resultat', 's')
text(ax, 72, 25, r'$-1+4-3=0$', 'resultat', 's')
text(ax, 22, 14.5, '3. comparer au vecteur nul', 'resultat', 'm')
box(ax, 58, 8, 28, 9, 'resultat', label=r'$(0,0)=\mathbf{0}$', weight='bold')
brace(ax, 58, 86, 36.5, 'encre', depth=2.0)
save(fig, '58-147')
