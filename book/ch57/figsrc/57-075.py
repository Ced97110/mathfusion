import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
ox, oy, u = 6, 8, 7
for i in range(7):
    for j in range(4):
        disc(ax, ox + u * i, oy + u * j, 0.55, 'fixe')
X = (ox + 2 * u, oy + 1 * u); A = (ox + 6 * u, oy + 3 * u)
arrow(ax, (ox, oy), A, 'resultat', lw=1.2)
arrow(ax, (ox, oy), X, 'sujet', lw=1.4)
arrow(ax, (X[0] + 1, X[1] + 1.5), (A[0] - 1.5, A[1] + 0.5), 'varie', curve=-0.35)
text(ax, 27, 38, '×3', 'varie', 's')
text(ax, X[0] + 3, X[1] - 4, 'x', 'sujet', 'm')
text(ax, A[0] + 2, A[1] - 5, 'ax', 'resultat', 'm')
box(ax, 62, 38, 24, 9, 'varie', label='coefficient 3', size='s')
box(ax, 62, 25, 24, 9, 'sujet', label='objet (2 ; 1)', size='s')
box(ax, 62, 12, 24, 9, 'resultat', label='ax = (6 ; 3)', size='s')
save(fig, '57-075')
