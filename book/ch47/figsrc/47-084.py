import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'6 permutations de 3 objets, $H$ de 2 éléments', 'fixe', 's')
def row(y, role, label):
    text(ax, 44, y + 11, label, role, 'm')
    for k in range(3):
        x = 6 + k * 27.5
        box(ax, x, y, 24, 8, role, fill=False, dash=True)
        for j in range(2): disc(ax, x + 7.5 + j * 9, y + 4, 2.6, role)
row(40, 'sujet', '3 classes à gauche')
row(14, 'autre', 'combien de classes à droite ?')
text(ax, 44, 31.5, r'même nombre : 3 ?', 'varie', 'm')
save(fig, '47-084')
