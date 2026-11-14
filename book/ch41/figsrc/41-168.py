import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
rows = {'u': ('sujet', '1  1  3'), 'v': ('autre', '2  0  0'), 'w': ('varie', '1  2  0')}
def matrix(x, order):
    for i, k in enumerate(order):
        role, nums = rows[k]
        box(ax, x, 50 - i * 12, 36, 10, role, label=rf'${k}$ :   ' + nums.replace('  ', r'   '), size='s')
text(ax, 22, 70, 'lignes u, v, w', 'encre', 's')
text(ax, 66, 70, 'lignes u, w, v', 'encre', 's')
matrix(4, 'uvw')
matrix(48, 'uwv')
box(ax, 4, 6, 36, 10, 'resultat', label='produit mixte = 12', size='s')
box(ax, 48, 6, 36, 10, 'resultat', label='produit mixte = −12', size='s')
save(fig, '41-168')
