import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
box(ax, 3, 14, 10, 24, 'varie', label='P')
mat([['4', '6'], ['6', '4']], [['sujet'] * 2] * 2, 16, 15.5)
box(ax, 40, 14, 10, 24, 'varie', label='Q')
text(ax, 55, 26, '=', 'encre', 'l')
mat([['2', '0'], ['0', '10']], [['resultat', 'fixe'], ['fixe', 'resultat']], 61, 15.5)
text(ax, 8, 9, 'lignes', 'varie', 's')
text(ax, 45, 9, 'colonnes', 'varie', 's')
text(ax, 26.5, 43, 'A', 'sujet', 'l')
save(fig, '59-071')
