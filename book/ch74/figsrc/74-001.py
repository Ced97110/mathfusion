import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 68, 'rouleaux de papier peint', 'sujet', 'l')
roles = ['sujet', 'varie', 'autre', 'fixe']
def mark(kind, x, y, role):
    if kind == 0: disc(ax, x, y, 1.7, role)
    elif kind == 1: box(ax, x - 1.6, y - 1.6, 3.2, 3.2, role, r=0.2)
    elif kind == 2: poly(ax, [(x, y - 2), (x + 2, y), (x, y + 2), (x - 2, y)], role)
    else: poly(ax, [(x - 2, y - 1.6), (x + 2, y - 1.6), (x, y + 1.9)], role)
for i in range(4):
    x0 = 4 + i * 21
    box(ax, x0, 38, 17, 17, 'encre')
    for a in range(3):
        for b in range(3): mark(i, x0 + 3.5 + a * 5, 41.5 + b * 5, roles[i])
brace(ax, 4, 84, 57, 'fixe', '500 aspects différents', down=False)
for i in range(4): arrow(ax, (12.5 + i * 21, 36), (44 + (i - 1.5) * 8, 25), 'fixe', lw=0.8)
box(ax, 19, 13, 50, 11, 'resultat', label='mêmes mouvements', size='m')
text(ax, 44, 6, 'combien de familles ?', 'varie', 'l')
save(fig, '74-001')
