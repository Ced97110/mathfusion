import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 52, 'Horloge 10, multiplication', 'encre', 's')
vals = ['2', '4', '8', '6']
for k, v in enumerate(vals):
    x = 6 + k*20
    box(ax, x, 28, 14, 11, 'sujet', label=v, size='l')
    text(ax, x + 7, 24, rf'$2^{k+1}$', 'fixe', 's')
    if k < 3: arrow(ax, (x + 14.3, 33.5), (x + 19.7, 33.5), 'fixe')
arrow(ax, (73, 40), (13, 40), 'varie', curve=-0.0)
ax.patches[-1].set_connectionstyle('arc3,rad=0.3')
text(ax, 44, 44.5, 'puis on recommence', 'varie', 's')
box(ax, 26, 4, 36, 10, 'limite', fill=False, dash=True, label=r'jamais $1$ : pas d’ordre'.replace(r'’', '’'), size='s')
save(fig, '47-203')
