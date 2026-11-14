import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for x, role in [(3, 'sujet'), (59, 'resultat')]:
    box(ax, x, 18, 26, 22, role)
    disc(ax, x+7, 28, 3.6, role, label='1', size='s')
    disc(ax, x+18, 28, 3.6, role, label=r'$z$', size='s')
    text(ax, x+13, 35.5, r'$C$' if x == 3 else r'$gCg^{-1}$', role, 'm')
arrow(ax, (31, 29), (57, 29), 'varie')
text(ax, 44, 35, 'conjuguer', 'varie', 's')
text(ax, 44, 23, r'par $g$', 'varie', 's')
text(ax, 44, 10, r'$gCg^{-1}=C$', 'resultat', 'l')
text(ax, 44, 49, 'chaque z reste en place', 'resultat', 'm')
save(fig, '49-282')
