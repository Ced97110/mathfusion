import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
arrow(ax, (4, 30), (84, 30), 'fixe', lw=0.9)
xs = [12, 27, 42, 57, 71]
for x in xs:
    disc(ax, x, 30, 1.8, 'autre')
text(ax, 12, 24, '561', 'autre', 'm', weight='bold')
text(ax, 12, 19.5, 'le plus petit', 'autre', 's')
brace(ax, 9, 45, 36, 'limite', 'une liste finie', down=False, size='s')
text(ax, 62, 42, 'toujours un', 'varie', 's')
text(ax, 62, 38, 'de plus', 'varie', 's')
arrow(ax, (57, 36), (57, 32.5), 'varie')
arrow(ax, (71, 36), (71, 32.5), 'varie')
text(ax, 44, 6, 'une infinité (preuve de 1994)', 'encre', 'm')
save(fig, '53-186')
