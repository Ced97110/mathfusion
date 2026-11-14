import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'base : $u_1 = (1, 0)$, $u_2 = (0, 1)$', 'fixe', 's')
rels = [r'$T u_1 = 0\,u_1 + 1\,u_2$', r'$T u_2 = 1\,u_1 + 0\,u_2$']
rows = [[0, 1], [1, 0]]
roles = ['sujet', 'varie']
mx, cw = 60, 12
ys = [34, 20]
for k in range(2):
    text(ax, 24, ys[k] + 6, rels[k], roles[k], 's')
    arrow(ax, (47, ys[k] + 6), (mx - 1.5, ys[k] + 6), roles[k])
    for j in range(2):
        box(ax, mx + j * cw, ys[k], cw, 12, roles[k], label=str(rows[k][j]), size='m', r=0.6)
text(ax, mx + cw, 52, r'$A$', 'resultat', 'l', weight='bold')
text(ax, 44, 8, r'ligne $i$ de $A$ : image de $u_i$', 'resultat', 's')
save(fig, '60-150')
