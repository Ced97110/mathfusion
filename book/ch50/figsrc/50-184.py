import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 71, r'$30 = 2 \times 3 \times 5$', 'sujet', 'l')
def row(y, lab, vals):
    text(ax, 15, y + 6, lab, 'encre', 's')
    for i, (d, r, ok) in enumerate(vals):
        box(ax, 28 + i * 14, y, 12, 12, 'resultat' if ok else 'limite', label=f'{d}\nreste {r}', size='s')
row(48, '$n_5$ divise 6\n(modulo 5)', [(1, 1, 1), (2, 2, 0), (3, 3, 0), (6, 1, 1)])
row(24, '$n_3$ divise 10\n(modulo 3)', [(1, 1, 1), (2, 2, 0), (5, 2, 0), (10, 1, 1)])
text(ax, 44, 42, r'$n_5 \in \{1, 6\}$', 'resultat', 'm')
text(ax, 44, 16, r'$n_3 \in \{1, 10\}$', 'resultat', 'm')
save(fig, '50-184')
