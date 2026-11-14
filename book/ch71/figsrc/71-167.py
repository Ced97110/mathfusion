import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$B$ symétrique, $\det = 1$', 'sujet', 'm')
box(ax, 4, 38, 20, 14, 'sujet', label='0  1\n1  0', size='m')
text(ax, 15, 56, 'matrice', 'sujet', 's')
text(ax, 56, 45, r'sur $(\mathbb{Z}/2)^2$ : 4 flèches', 'encre', 's')
vs = ['(0, 0)', '(1, 0)', '(0, 1)', '(1, 1)']
for i, v in enumerate(vs):
    x = 4 + i * 21
    box(ax, x, 22, 19, 7, 'fixe', label=v, size='s')
    arrow(ax, (x + 9.5, 22), (x + 9.5, 15), 'limite')
    box(ax, x + 4, 7, 11, 8, 'limite', label='0')
text(ax, 44, 2.5, r'$B(u, u) = 0$ pour toute flèche $u$', 'limite', 's')
save(fig, '71-167')
