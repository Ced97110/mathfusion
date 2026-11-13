import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'produit direct de Sylow', 'resultat', 'm', weight='bold')
def cross(x, y):
    line(ax, [(x - 1, y - 1), (x + 1, y + 1)], 'fixe', lw=1.0); line(ax, [(x - 1, y + 1), (x + 1, y - 1)], 'fixe', lw=1.0)
def rowof(y, labs):
    x = 22
    for i, l in enumerate(labs):
        box(ax, x, y, 15, 9, 'sujet', label=l, size='s')
        if i < len(labs) - 1: cross(x + 18, y + 4.5)
        x += 21
rowof(40, [r'$\mathbb{Z}/9$', r'$\mathbb{Z}/11$'])
rowof(27, [r'$\mathbb{Z}/3$', r'$\mathbb{Z}/3$', r'$\mathbb{Z}/11$'])
line(ax, [(17, 27), (17, 49)], 'fixe'); text(ax, 8, 38, '99', 'encre', 'm', weight='bold')
text(ax, 8, 14, '1645', 'encre', 'm', weight='bold'); line(ax, [(17, 9), (17, 19)], 'fixe')
rowof(10, [r'$\mathbb{Z}/5$', r'$\mathbb{Z}/7$', r'$\mathbb{Z}/47$'])
text(ax, 50, 3, 'liste complète des groupes', 'resultat', 's')
save(fig, '50-255')
