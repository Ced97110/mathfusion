import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
for r in range(2):
    for c in range(3):
        box(ax, 12 + 11 * c, 30 + 11 * r, 9, 9, 'sujet', label='1')
brace(ax, 12, 42, 52, 'varie', label=r'$b$ : 3 termes', down=False)
text(ax, 7, 40, r'$a$ : 2 lignes', 'varie', 's', rot=90)
text(ax, 62, 66, r'$p=a\times b=6$', 'encre', 'm', ha='left')
text(ax, 50, 56, 'somme de 2 : non nulle', 'fixe', 's', ha='left')
text(ax, 50, 49, 'somme de 3 : non nulle', 'fixe', 's', ha='left')
text(ax, 50, 40, 'leur produit : 6 termes', 'encre', 's', ha='left')
text(ax, 50, 33, 'donc égal à 0', 'encre', 's', ha='left')
box(ax, 4, 6, 80, 12, 'limite', label='deux non nuls, produit 0 : faux', size='m')
save(fig, '67-023')
