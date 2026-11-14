import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(108)
steps = [r'$\alpha(\alpha+1)$', r'$\alpha^2+\alpha$', r'$(\alpha+1)+\alpha$', r'$1$']
notes = ['on développe', r'règle 2 : $\alpha^2=\alpha+1$', r'$\alpha+\alpha=0$, reste 1']
roles = ['sujet', 'varie', 'varie', 'resultat']
for i in range(4):
    y = 94 - 18 * i
    box(ax, 4, y, 38, 11, roles[i], label=steps[i], size='m')
    if i < 3:
        arrow(ax, (23, y), (23, y - 7), 'varie')
        text(ax, 28, y - 3.5, notes[i], 'varie', 's', ha='left')
box(ax, 8, 14, 22, 12, 'sujet', label=r'$\alpha$', size='l')
box(ax, 58, 14, 24, 12, 'autre', label=r'$\alpha+1$', size='l')
arrow(ax, (30, 20), (58, 20), 'resultat', both=True)
text(ax, 44, 25, 'produit 1', 'resultat', 's')
text(ax, 44, 6, 'inverses l’un de l’autre', 'resultat', 'm')
save(fig, '67-017')
