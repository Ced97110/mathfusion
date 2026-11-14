import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# rangée 1 : condition nécessaire, cas qui casse
text(ax, 44, 70, 'On sait déjà : un corps est intègre', 'fixe', 'm')
box(ax, 2, 50, 22, 12, 'fixe', label=r'$\mathbb{Z}/6$')
arrow(ax, (24, 56), (60, 56), 'limite')
text(ax, 42, 60, r'$2\times3=0$', 'limite', 's')
text(ax, 42, 52, 'impossible dans un corps', 'limite', 's')
box(ax, 62, 50, 24, 12, 'fixe', dash=True, label='corps')
# rangée 2 : cas qui marche
box(ax, 2, 30, 22, 12, 'sujet', label=r'$\mathbb{Z}$')
arrow(ax, (24, 36), (60, 36), 'resultat')
text(ax, 42, 40, 'se plonge', 'resultat', 's')
box(ax, 62, 30, 24, 12, 'resultat', label=r'$\mathbb{Q}$')
# la question
box(ax, 8, 4, 72, 14, 'varie', label='Tout anneau intègre se plonge-t-il\ndans un corps ?')
save(fig, '54-031')
