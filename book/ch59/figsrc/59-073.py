import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
mat([['6', '0'], ['0', '4']], [['fixe'] * 2] * 2, 4, 24)
mat([['2', '0'], ['0', '12']], [['resultat', 'fixe'], ['fixe', 'resultat']], 63, 24)
arrow(ax, (28, 34.5), (60, 34.5), 'varie', both=True)
text(ax, 44, 40, 'même module', 'varie', 's')
text(ax, 14.5, 50, 'sans chaîne', 'fixe', 's')
text(ax, 73.5, 50, 'avec la chaîne', 'resultat', 's')
text(ax, 14.5, 17, r'$6\nmid4$', 'limite', 'm')
text(ax, 73.5, 17, r'$2\mid12$', 'resultat', 'm')
text(ax, 44, 6, 'la chaîne en garde une seule', 'resultat', 's')
save(fig, '59-073')
