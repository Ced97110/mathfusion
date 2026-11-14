import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 4, 56, 'chemin long : modules et matrices', 'fixe', 's', ha='left')
xs = [4, 24, 44, 64]
labs = ['groupe', 'module', 'matrices', 'décomposition']
for i, (x, v) in enumerate(zip(xs, labs)):
    w = 20 if i < 3 else 22
    box(ax, x, 40, w, 10, 'fixe', label=v, size='s')
    if i < 3:
        arrow(ax, (x + w, 45), (xs[i + 1], 45), 'fixe')
text(ax, 4, 28, 'chemin de Judson : dans le groupe', 'resultat', 's', ha='left')
box(ax, 4, 10, 20, 10, 'sujet', label='groupe', size='s')
box(ax, 64, 10, 22, 10, 'resultat', label='décomposition', size='s')
arrow(ax, (24, 15), (64, 15), 'varie', lw=1.4)
text(ax, 44, 19, 'sans module', 'varie', 's')
text(ax, 44, 11, 'ni matrice', 'varie', 's')
save(fig, '60-109')
