import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
text(ax, 44, 71, 'étape 5 : faire entrer le 3 dans la ligne 1', 'encre', 's')
mat([['2', '0'], ['0', '3']], [['sujet', 'fixe'], ['fixe', 'varie']], 4, 42)
mat([['2', '3'], ['0', '3']], [['sujet', 'varie'], ['fixe', 'fixe']], 63, 42)
arrow(ax, (28, 52.5), (60, 52.5), 'varie')
text(ax, 44, 58, 'ligne 1 + ligne 2', 'varie', 's')
text(ax, 14.5, 37, r'$2\nmid3$ : pas un multiple', 'encre', 's')
text(ax, 71, 37, '3 dans la ligne 1', 'varie', 's')
arrow(ax, (71, 34), (71, 27), 'varie')
text(ax, 66, 30.5, 'puis division', 'varie', 's', ha='right')
box(ax, 48, 9, 38, 17, 'resultat', label=r'$3=1\times2+1$' + '\n' + r'reste $1<2$', size='s')
text(ax, 22, 17.5, r'le pivot baisse', 'resultat', 's')
text(ax, 22, 11.5, r'$2\ \to\ 1$', 'resultat', 's')
save(fig, '59-082')
