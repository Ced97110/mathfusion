import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 14, 54, 26, 9, 'autre', label='paquet 0-6', size='s'); box(ax, 48, 54, 26, 9, 'autre', label='paquet 3-9', size='s')
brace(ax, 14, 74, 63, 'autre', label='sous-groupe du quotient : 2', down=False)
arrow(ax, (27, 54), (27, 38), 'varie'); arrow(ax, (61, 54), (61, 38), 'varie')
text(ax, 44, 46, 'remonter', 'varie', 's')
for x, l in [(14, '0'), (27, '6'), (48, '3'), (61, '9')]:
    box(ax, x, 29, 13, 9, 'resultat', label=l)
brace(ax, 14, 40, 28, 'fixe', label=r'$p=2$')
brace(ax, 48, 74, 28, 'fixe', label=r'$p=2$')
box(ax, 9, 6, 70, 10, 'resultat', label=r'$|H|=2\times2=4$ éléments', size='s')
save(fig, '50-128')
