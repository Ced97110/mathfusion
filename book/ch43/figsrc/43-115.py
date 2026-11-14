import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 4, 56, 'numéros : 0, 1, 2, 3, …', 'varie', 'm', ha='left')
for i in range(4):
    x = 12 + 17 * i
    box(ax, x - 6, 34, 12, 9, 'sujet', label=r'$a_%d$' % i)
    text(ax, x, 48, str(i), 'varie', 'm')
    arrow(ax, (x, 47), (x, 44.5), 'varie')
text(ax, 80, 38.5, '…', 'sujet', 'l')
text(ax, 4, 28, 'ℕ : chaque élément a un numéro', 'sujet', 's', ha='left')
box(ax, 4, 4, 80, 14, 'limite', label='réels entre 0 et 1 : pas de liste', size='s')
save(fig, '43-115')
