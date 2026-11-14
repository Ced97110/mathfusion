import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
box(ax, 4, 34, 26, 9, 'sujet', label=r'$u_1 = (1,\ 1)$', size='s')
box(ax, 4, 10, 26, 9, 'autre', label=r'$u_2 = (1,\ -1)$', size='s')
text(ax, 50, 47, 'colonne 1', 'sujet', 's'); text(ax, 72, 47, 'colonne 2', 'autre', 's')
cells = [('1', 'sujet', 50, 33), ('1', 'sujet', 50, 19), ('1', 'autre', 72, 33), ('−1', 'autre', 72, 19)]
for t, r, x, y in cells:
    box(ax, x - 7, y - 5, 14, 10, r, label=t, size='l')
arrow(ax, (30, 38), (43, 33), 'sujet', curve=0.0)
arrow(ax, (30, 12), (72, 14), 'autre')
text(ax, 17, 26, r'$P =$', 'encre', 'l')
text(ax, 61, 4, 'une flèche = une colonne', 'encre', 's')
save(fig, '71-169')
