import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
panels = [(2, 'sujet', r'$F$ infini : $\mathbb{R}$', 'resultat', 'vaut 6 en 2 :\nfonction non nulle', 'isomorphisme'),
          (46, 'autre', r'$F$ fini : $\mathbb{Z}/3\mathbb{Z}$', 'limite', 'vaut 0 partout :\nfonction nulle', 'pas isomorphisme')]
for x, role, head, r2, f, v in panels:
    box(ax, x, 3, 40, 70, 'fixe', fill=False, dash=True)
    text(ax, x + 20, 67, head, role, 'm', weight='bold')
    box(ax, x + 2, 44, 36, 14, role, label=r'$x^3 - x$ :' + '\npolynôme non nul', size='s')
    arrow(ax, (x + 20, 43), (x + 20, 36), 'varie')
    box(ax, x + 2, 22, 36, 13, r2, label=f, size='s')
    arrow(ax, (x + 20, 21), (x + 20, 15), 'varie')
    box(ax, x + 2, 5, 36, 9, r2, label=v, size='s')
save(fig, '55-039')
