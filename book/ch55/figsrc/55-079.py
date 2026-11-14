import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(80)
text(ax, 44, 74, r'$e_r$ = produit de tous', 'sujet', 'm', weight='bold')
rows = [((2, 3, 4), 56), ((1, 2, 3, 4), 36), ((2, 5, 7), 16)]
for vals, y in rows:
    xs = [10 + 11.5 * i for i in range(len(vals))]
    for x, v in zip(xs, vals):
        disc(ax, x, y, 4.5, 'sujet', label=str(v), size='l')
    brace(ax, xs[0] - 4.5, xs[-1] + 4.5, y - 6, 'resultat', depth=1.8)
    text(ax, 58, y, rf'$r={len(vals)}$ : {math.prod(vals)}', 'resultat', 'l', ha='left', weight='bold')
save(fig, '55-079')
