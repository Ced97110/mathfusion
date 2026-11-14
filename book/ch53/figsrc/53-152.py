import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
# colonne Alice
text(ax, 15, 76, 'Alice', 'autre', 'm', weight='bold')
box(ax, 2, 58, 26, 12, 'autre', label=r'$d = 27$', size='l')
text(ax, 15, 52, 'privé', 'autre', 's')
# colonne Bob
text(ax, 61, 76, 'Bob', 'sujet', 'm', weight='bold')
box(ax, 43, 58, 36, 12, 'sujet', label=r"$d' = 29$", size='l')
text(ax, 61, 52, 'privé', 'sujet', 's')
text(ax, 61, 44, r"$e' \times d' = 5 \times 29 = 145$", 'encre', 's')
arrow(ax, (61, 41), (61, 36), 'varie')
box(ax, 36, 27, 50, 8, 'resultat', label=r'$145 = 2 \times 72 + 1$', size='s')
arrow(ax, (61, 26), (61, 21), 'varie')
box(ax, 36, 11, 50, 9, 'fixe', label=r'$72 = 6 \times 12$', size='s')
text(ax, 61, 5.5, r'$6 = 7 - 1$ et $12 = 13 - 1$', 'fixe', 's')
save(fig, '53-152')
