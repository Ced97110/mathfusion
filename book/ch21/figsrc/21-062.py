import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 4, 68, 'chapitre 6', 'autre', 'm', ha='left')
box(ax, 4, 50, 80, 14, 'autre', label=r'$\frac{2}{3}\times\frac{5}{7}=\frac{10}{21}$', size='l')
arrow(ax, (44, 48), (44, 36), 'varie', both=True)
text(ax, 47, 42, 'même règle', 'varie', 's', ha='left')
text(ax, 4, 32, 'polynômes', 'sujet', 'm', ha='left')
box(ax, 4, 6, 80, 20, 'sujet', label=r'$\frac{x+1}{3}\times\frac{5}{x+2}=\frac{5(x+1)}{3(x+2)}$', size='m')
save(fig, '21-062')
