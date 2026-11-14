import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for y, n, cap in ((30, 5, '5 éléments : 1 et 5 seulement'), (8, 6, '6 éléments : 1, 2, 3, 6')):
    text(ax, 5, y + 13.5, cap, 'encre', 's', ha='left')
    for t in range(1, n + 1):
        ok = n % t == 0
        box(ax, 5 + (t - 1) * 14, y, 12, 9, 'resultat' if ok else 'limite', label=str(t), size='l', dash=not ok)
text(ax, 44, 1.5, 'vert : taille possible ; rouge : impossible', 'fixe', 's')
save(fig, '64-101')
