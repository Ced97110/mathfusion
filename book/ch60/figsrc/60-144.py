import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 80, r'$\lambda^2 - 2\lambda + 1$ dans $\mathbb{Q}[\lambda]$', 'sujet', 'm', weight='bold')
pw = [r'$\lambda^2$', r'$\lambda^1$', r'$\lambda^0$']
co = ['1', '−2', '1']
for k in range(3):
    x = 21 + k * 18
    text(ax, x + 7, 72, pw[k], 'fixe', 's')
    box(ax, x, 58, 14, 10, 'sujet', label=co[k], size='m')
text(ax, 44, 52, 'coefficients pris dans le corps F', 'fixe', 's')
# comparison
box(ax, 2, 36, 38, 9, 'autre', label='entiers ℤ', size='s')
box(ax, 48, 36, 38, 9, 'sujet', label=r'polynômes $F[\lambda]$', size='s')
arrow(ax, (40.6, 40.5), (47.4, 40.5), 'varie', both=True)
box(ax, 2, 22, 38, 9, 'autre', label='nombre premier', size='s')
box(ax, 48, 22, 38, 9, 'sujet', label='polynôme irréductible', size='s')
arrow(ax, (40.6, 26.5), (47.4, 26.5), 'varie', both=True)
box(ax, 2, 8, 38, 9, 'autre', label='multiple', size='s')
box(ax, 48, 8, 38, 9, 'sujet', label='multiple d’un polynôme', size='s')
arrow(ax, (40.6, 12.5), (47.4, 12.5), 'varie', both=True)
save(fig, '60-144')
