import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 72, r'$12 = 2^2 \times 3$', 'sujet', 'l')
text(ax, 44, 63, r'$n_3$ divise 4, reste 1 modulo 3', 'encre', 's')
for i, (d, r, ok) in enumerate([(1, 1, True), (2, 2, False), (4, 1, True)]):
    box(ax, 14 + i * 24, 44, 20, 12, 'resultat' if ok else 'limite', label=f'{d}\nreste {r}', size='s')
text(ax, 44, 36, r'$n_3 \in \{1, 4\}$', 'resultat', 'l')
arrow(ax, (30, 33), (20, 22), 'varie'); arrow(ax, (58, 33), (68, 22), 'varie')
box(ax, 4, 8, 32, 12, 'varie', label=r'cas $n_3 = 1$', size='m')
box(ax, 52, 8, 32, 12, 'varie', label=r'cas $n_3 = 4$', size='m')
save(fig, '50-179')
