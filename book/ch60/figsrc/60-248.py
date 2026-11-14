import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
labs = ['1', r'$\lambda$', r'$\lambda^2$', r'$\lambda^3$']
for i, s in enumerate(labs):
    box(ax, 3 + 17 * i, 48, 13, 10, 'sujet', label=s)
    if i < 3: arrow(ax, (16.3 + 17 * i, 53), (19.7 + 17 * i, 53), 'varie')
text(ax, 18, 63, r'$\times\lambda$', 'varie', 's')
text(ax, 75, 53, r'$\cdots$', 'sujet', 'l')
text(ax, 44, 40, r'$F[\lambda]$ : libre, sans torsion', 'sujet', 's')
arrow(ax, (3, 32), (82, 32), 'fixe')
text(ax, 44, 27.5, 'dimension infinie sur F', 'fixe', 's')
box(ax, 4, 5, 80, 13, 'limite', dash=True, label='dimension finie\nsans torsion : impossible', size='s')
save(fig, '60-248')
