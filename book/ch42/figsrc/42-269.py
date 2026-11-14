import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
for y, n, p, s in ((42, '10 objets', r'$2^{10}$', '1 024 sacs'), (26, '20 objets', r'$2^{20}$', '1 048 576 sacs')):
    box(ax, 2, y, 24, 10, 'sujet', label=n); arrow(ax, (26, y + 5), (46, y + 5), 'varie'); text(ax, 36, y + 9, p, 'varie')
    box(ax, 46, y, 40, 10, 'resultat', label=s)
box(ax, 2, 6, 40, 9, 'limite', label='liste : impossible', size='s'); box(ax, 46, 6, 40, 9, 'resultat', label='règle : un seul calcul', size='s')
save(fig, '42-269')
