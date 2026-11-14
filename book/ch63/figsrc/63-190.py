import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# colonne de gauche : les étapes de la dérivée
text(ax, 4, 74, r'$x^4 - x$', 'sujet', 'l', ha='left')
text(ax, 4, 62, r'dérivée : $4x^3 - 1$', 'varie', 'm', ha='left')
text(ax, 4, 50, r'$4 = 0$ donc $0\cdot x^3 - 1$', 'varie', 'm', ha='left')
box(ax, 4, 31, 38, 10, 'resultat', label=r'reste $-1$ : jamais nul', size='m')
# corps à 2 éléments : quatre sauts de 1 reviennent à 0
text(ax, 67, 74, 'corps à 2 éléments', 'autre', 's')
xs = [49 + 8.5 * i for i in range(5)]
for i, x in enumerate(xs):
    disc(ax, x, 56, 3.3, 'autre' if i % 2 == 0 else 'fixe', label='0' if i % 2 == 0 else '1', size='s')
    if i:
        arrow(ax, (xs[i - 1] + 3.6, 56), (x - 3.6, 56), 'varie', lw=0.9)
text(ax, 67, 46, '1 + 1 + 1 + 1 = 0', 'resultat', 'm')
# second cas : p = 3
text(ax, 4, 18, r'$x^3 - x$ : dérivée $3x^2 - 1$', 'sujet', 's', ha='left')
text(ax, 4, 10, r'$3 = 0$ : reste $-1$ aussi', 'resultat', 's', ha='left')
save(fig, '63-190')
