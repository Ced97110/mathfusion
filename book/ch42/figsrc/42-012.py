import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
rows = [('la gourde seule', r'$\{a\}$'), ('la gourde et la carte', r'$\{a,b\}$'), ('les trois objets', r'$\{a,b,c\}$')]
for i, (ph, no) in enumerate(rows):
    y = 50 - i * 15
    box(ax, 2, y - 5, 40, 10, 'fixe', label=ph, size='s')
    arrow(ax, (43, y), (52, y), 'varie')
    box(ax, 53, y - 5, 33, 10, 'sujet', label=no, size='l', weight='bold')
text(ax, 44, 7, r'$\{\ \}$ : « l’ensemble formé de »', 'varie', 's', weight='bold')
save(fig, '42-012')
