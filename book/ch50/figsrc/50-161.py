import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'$n_3\in\{1,\ 4\}$', 'encre', 'l')
text(ax, 44, 54, '4 sous-groupes de 3 éléments', 'sujet', 'm')
for g in range(4):
    x = 3.5 + g * 21
    box(ax, x, 34, 18, 14, 'sujet')
    disc(ax, x + 3.5, 41, 2.3, 'fixe', label=r'$e$', size='s')
    disc(ax, x + 9, 41, 2.3, 'sujet')
    disc(ax, x + 14.5, 41, 2.3, 'sujet')
brace(ax, 3.5, 84.5, 32, 'sujet', label='8 éléments, 2 par groupe')
arrow(ax, (44, 25.5), (44, 20), 'resultat')
box(ax, 24, 9, 40, 10, 'resultat', label=r'$n_3=8/2=4$')
save(fig, '50-161')
