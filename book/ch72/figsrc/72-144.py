import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, 'orange : −1 (impropre)', 'varie', 's')
text(ax, 44, 60, 'vert : 1 (rotation)', 'resultat', 's')
for k in range(1, 5):
    x = 8 + (k - 1) * 20.5
    role = 'varie' if k % 2 else 'resultat'
    for j in range(k):
        box(ax, x, 26 + j * 7, 15, 6, role)
    text(ax, x + 7.5, 20, f'k = {k}', 'encre', 's')
    text(ax, x + 7.5, 12, '−1' if k % 2 else '1', role, 'l', weight='bold')
text(ax, 44, 4, '1 case = 1 réflexion', 'fixe', 's')
save(fig, '72-144')
