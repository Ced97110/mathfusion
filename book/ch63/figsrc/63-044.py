import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 3, 22, 38, 22, 'sujet')
text(ax, 22, 40, r'$H$', 'sujet', 'm', weight='bold')
for x, l in zip([14, 30], ['1', r'$\sigma$']):
    disc(ax, x, 30.5, 4.5, 'sujet', label=l)
box(ax, 47, 22, 38, 22, 'autre')
text(ax, 66, 40, '2e bloc', 'autre', 'm')
for x, l in zip([58, 74], [r'$\tau$', r'$\sigma\tau$']):
    disc(ax, x, 30.5, 4.5, 'autre', label=l, size='s')
brace(ax, 3, 85, 46, 'fixe', label=r'$G$ : 4 éléments', down=False)
text(ax, 22, 17, '2 éléments', 'sujet', 's')
text(ax, 66, 17, '2 éléments', 'autre', 's')
text(ax, 44, 7, r'$[G:H]=4\div2=2$', 'resultat', 'l', weight='bold')
save(fig, '63-044')
