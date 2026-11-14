import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'cadran à 7 heures', 'fixe', 'm')
xs = [10, 38, 68]
for x, lab in zip(xs, ['3', '2', '6']):
    box(ax, x, 40, 14, 11, 'sujet', label=lab, size='l')
text(ax, 31, 45.5, r'$\times$', 'encre', 'l'); text(ax, 59, 45.5, '=', 'encre', 'l')
for x, lab in zip(xs, ['5', '4', '6']):
    arrow(ax, (x + 7, 39), (x + 7, 32), 'varie')
    box(ax, x, 20, 14, 11, 'autre', label=lab, size='l')
text(ax, 3, 57.5, 'unités', 'sujet', 's', ha='left')
text(ax, 3, 15.5, 'leurs inverses', 'autre', 's', ha='left')
text(ax, 44, 8, r'$4\times5=20$, soit 6', 'resultat', 'm')
text(ax, 44, 3, 'inverse de 6 = 6 ; ordre inversé', 'resultat', 's')
save(fig, '51-059')
