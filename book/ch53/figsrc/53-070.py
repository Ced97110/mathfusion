import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

M = [[3, 3], [2, 5]]
def enc(a, b):
    p = (ord(a) - 65, ord(b) - 65)
    r = [(M[i][0] * p[0] + M[i][1] * p[1]) % 26 for i in range(2)]
    return chr(65 + r[0]) + chr(65 + r[1])
assert enc('E', 'S') == 'OU' and enc('E', 'A') == 'MI'

fig, ax = canvas(66)
rows = [('E', 'S', enc('E', 'S'), 40), ('E', 'A', enc('E', 'A'), 8)]
for a, b, out, y in rows:
    box(ax, 3, y, 12, 12, 'varie', label=a)
    box(ax, 17, y, 12, 12, 'sujet', label=b)
    arrow(ax, (31, y + 6), (50, y + 6), 'fixe')
    text(ax, 40.5, y + 9.5, 'matrice', 'fixe', 's')
    box(ax, 52, y, 12, 12, 'autre', label=out[0])
    box(ax, 66, y, 12, 12, 'resultat', label=out[1])
text(ax, 44, 30, 'même E, deux images : O et M', 'autre', 's')
text(ax, 44, 62, 'matrice de lignes 3, 3 et 2, 5', 'fixe', 's')
save(fig, '53-070')
