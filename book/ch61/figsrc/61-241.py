import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 3, 36, 32, 12, 'fixe', label='tracé à la règle'); 
box(ax, 53, 36, 32, 12, 'sujet', label=r'$3$ divise $2^n$ ?')
arrow(ax, (35, 42), (53, 42), 'varie')
text(ax, 44, 46, 'devient', 'varie', 's')
for i, v in enumerate([2, 4, 8, 16, 32]):
    box(ax, 4 + i * 16.5, 12, 13, 9, 'autre', label=str(v))
text(ax, 44, 27, 'puissances de 2', 'autre', 's')
text(ax, 44, 5, 'aucune n’est un multiple de 3', 'limite', 's')
save(fig, '61-241')
