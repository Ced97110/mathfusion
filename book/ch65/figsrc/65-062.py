import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
text(ax, 44, 62, r'$x^3-x$ : les 3 racines sont dans $\mathbb{Q}$', 'sujet', 's', weight='bold')
vals = ['0', '1', '−1']
xs = [16, 44, 72]
for x, v in zip(xs, vals):
    box(ax, x - 12, 30, 24, 22, 'autre', dash=True, fill=False)
    disc(ax, x, 44, 4.4, 'sujet', label=v, size='m')
    arrow(ax, (x, 39), (x, 34.5), 'fixe', lw=0.8)
    text(ax, x, 32, v + ' reste ' + v if False else 'reste en place', 'fixe', 's')
text(ax, 44, 22, '3 orbites d’un seul point', 'autre', 's', weight='bold')
box(ax, 22, 6, 44, 11, 'resultat', label='groupe = {identité}', size='s', weight='bold')
save(fig, '65-062')
