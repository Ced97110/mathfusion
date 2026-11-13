import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def tiles(x, y, roles):
    for i, (l, r) in enumerate(zip('xyx', roles)): box(ax, x + i * 9, y, 8.5, 9, r, label=f'${l}$')
tiles(8, 52, ['sujet', 'sujet', 'fixe'])
brace(ax, 8, 25.5, 52, 'sujet', label='d’abord ces deux', depth=1.4)
tiles(52, 52, ['fixe', 'autre', 'autre'])
brace(ax, 61, 78.5, 52, 'autre', label='d’abord ces deux', depth=1.4)
arrow(ax, (17, 37), (36, 27), 'varie'); arrow(ax, (70, 37), (52, 27), 'varie')
tiles(34, 14, ['resultat'] * 3)
text(ax, 44, 7, 'même mot : $xyx$', 'resultat', 's')
save(fig, '49-028')
