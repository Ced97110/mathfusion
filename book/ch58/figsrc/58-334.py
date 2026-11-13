import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
# B de colonnes (2,1),(1,3) ; P de colonnes (2,1),(1,1)
# P^-1 B P : colonnes (0,5),(-1,5) ; P^t B P : colonnes (15,10),(10,7)
def mat(x, y, cols, role, c=9.0):
    """tableau 2x2 donné par colonnes ; coin bas-gauche (x, y)"""
    for j in range(2):
        for i in range(2):
            v = str(cols[j][i]).replace('-', '−')
            box(ax, x + c * j, y + c * (1 - i), c, c, role, label=v, size='m')
mat(34, 64, [(2, 1), (1, 3)], 'sujet')
text(ax, 30, 73, r'$B$', 'sujet', 'l')
mat(60, 64, [(2, 1), (1, 1)], 'fixe')
text(ax, 55.5, 73, r'$P$', 'fixe', 'l')
# deux chemins
arrow(ax, (40, 62), (22, 44), 'varie', lw=1.2)
arrow(ax, (48, 62), (66, 44), 'autre', lw=1.2)
text(ax, 10, 53, 'homomorphisme', 'varie', 's', ha='left')
text(ax, 78, 53, 'forme bilinéaire', 'autre', 's', ha='right')
text(ax, 22, 40, r'$P^{-1}BP$', 'varie', 'l')
text(ax, 66, 40, r'$P^{t}BP$', 'autre', 'l')
mat(13, 20, [(0, 5), (-1, 5)], 'varie')
mat(57, 20, [(15, 10), (10, 7)], 'autre')
text(ax, 22, 10, 'inverse de $P$', 'varie', 's')
text(ax, 66, 10, 'transposée de $P$', 'autre', 's')
save(fig, '58-334')
