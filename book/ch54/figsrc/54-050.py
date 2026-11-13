import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
assert 1 * 4 == 2 * 2 and 2 * 6 == 4 * 3 and 4 * (6 - 6) == 0 and 1 * 6 == 2 * 3
text(ax, 44, 91, r'but : $1\times6=2\times3$ ?', 'varie', 'm')
y = 68
box(ax, 2, y, 22, 11, 'sujet', label='(1, 2)', size='m')
box(ax, 33, y, 22, 11, 'sujet', label='(2, 4)', size='m')
box(ax, 64, y, 22, 11, 'sujet', label='(3, 6)', size='m')
arrow(ax, (24, y + 5.5), (33, y + 5.5), 'resultat')
arrow(ax, (55, y + 5.5), (64, y + 5.5), 'resultat')
text(ax, 20, y - 5, r'① $1\times4=2\times2$', 'resultat', 's')
text(ax, 68, y - 5, r'② $2\times6=4\times3$', 'resultat', 's')
arrow(ax, (20, y - 9), (34, 52), 'resultat')
arrow(ax, (68, y - 9), (54, 52), 'resultat')
box(ax, 8, 38, 72, 13, 'fixe', label=r'③ $4\times(6-6)=0$', size='m')
arrow(ax, (44, 37), (44, 26), 'varie')
text(ax, 48, 31.5, r'④ $4\neq0$, anneau intègre', 'varie', 's', ha='left')
box(ax, 8, 12, 72, 13, 'resultat', label=r'$6-6=0$ donc $1\times6=2\times3$', size='m')
save(fig, '54-050')
