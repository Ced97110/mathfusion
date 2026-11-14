import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
PAD = '  '; SEP = ' ' * 3
def ent(v): return str(v).replace('-', '−') if v < 0 else PAD + str(v)
def mat(x0, M, role, title):
    pitch = 8.95
    for r in range(3):
        y = 36 - 9 * r
        box(ax, x0 + r * pitch + 3.05 - 4.3 + 2.2, y - 4, 8.6, 8, role)
        text(ax, x0 + 2.2, y, SEP.join(ent(v) for v in M[r]), 'encre', 'm', ha='left')
    for sx in (x0 - 1, x0 + 27):
        line(ax, [(sx, 12), (sx, 42)], 'fixe', lw=0.8)
    text(ax, x0 + 13, 51, title, role, 's')
mat(9, [[1, 0, 0], [1, 1, 0], [1, 1, 1]], 'sujet', r'$\zeta$ : points → totaux')
mat(54, [[1, 0, 0], [-1, 1, 0], [0, -1, 1]], 'resultat', r'$\mu$ : totaux → points')
arrow(ax, (38, 26), (49, 26), 'varie')
text(ax, 43.5, 31, 'défait', 'varie', 's')
text(ax, 44, 3, 'des 1 sur la diagonale, 0 d’un côté', 'encre', 's')
save(fig, '80-271')
