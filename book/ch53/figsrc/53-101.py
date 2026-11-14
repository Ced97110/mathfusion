import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'Clé publiée par Alice', 'encre', 'm')
box(ax, 14, 40, 26, 11, 'fixe', label=r'$n$ = 55', size='m')
box(ax, 48, 40, 26, 11, 'sujet', label=r'$e$ = 3', size='m')
arrow(ax, (61, 39), (61, 29), 'varie')
for i, x in enumerate((20, 38, 56)):
    box(ax, x, 14, 14, 12, 'varie', label='8', size='l')
text(ax, 17, 20, '', 'encre', 's')
text(ax, 36, 20, r'$\times$', 'encre', 'm')
text(ax, 54, 20, r'$\times$', 'encre', 'm')
brace(ax, 20, 70, 13, 'sujet', label=r'$e$ = 3 facteurs égaux', down=True)
save(fig, '53-101')
