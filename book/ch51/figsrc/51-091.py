import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'A : lignes (1, 2) et (0, 3)', 'sujet', 's')
text(ax, 44, 54, 'B : lignes (4, 5) et (0, 6)', 'autre', 's')
c = 9
def mat(x0, y0, vals, roles):
    for i in range(2):
        for j in range(2):
            box(ax, x0 + j * c, y0 + (1 - i) * c, c, c, roles[2 * i + j], label=vals[2 * i + j], size='m')
text(ax, 14, 41, 'A B =', 'sujet', 'l')
mat(30, 32, ['4', '17', '0', '18'], ['fixe', 'limite', 'resultat', 'fixe'])
text(ax, 14, 18, 'B A =', 'autre', 'l')
mat(30, 9, ['4', '23', '0', '18'], ['fixe', 'limite', 'resultat', 'fixe'])
text(ax, 66, 41, '17 ≠ 23', 'limite', 'm', ha='left')
text(ax, 66, 18, 'les deux 0', 'resultat', 's', ha='left')
text(ax, 66, 13, 'restent', 'resultat', 's', ha='left')
save(fig, '51-091')
