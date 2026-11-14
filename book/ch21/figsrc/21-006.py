import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0, k = 10, 7
text(ax, 2, 66, 'chacun sa dalle : 6 + 4', 'limite', 's', ha='left')
box(ax, x0, 53, 6 * k, 8, 'sujet', label='6 h', size='s'); box(ax, x0 + 6 * k, 53, 4 * k, 8, 'autre', label='4 h', size='s')
brace(ax, x0, x0 + 10 * k, 51, 'limite', label='6 + 4 = 10 h : trop', size='s')
text(ax, 2, 35, 'le plus rapide, seul', 'autre', 's', ha='left')
box(ax, x0, 24, 4 * k, 8, 'autre', label='4 h', size='s')
line(ax, [(x0 + 4 * k, 36), (x0 + 4 * k, 6)], 'fixe', dash=True)
arrow(ax, (x0 + 4 * k, 12), (x0 + 1.5 * k, 12), 'resultat', lw=1.4)
text(ax, x0 + 4 * k + 2, 12, 'à deux : moins de 4 h', 'resultat', 's', ha='left')
save(fig, '21-006')
