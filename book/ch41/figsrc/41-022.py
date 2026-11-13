import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Échelle 7 mm par unité. A (1 ; 2), B (4 ; 6) : déplacement (3 ; 4), longueur 5.
fig, ax = canvas(62)
u = 7.0
O = (8, 6)
P = lambda x, y: (O[0] + x * u, O[1] + y * u)
arrow(ax, O, (O[0] + 38, O[1]), 'fixe', lw=0.8)
arrow(ax, O, (O[0], O[1] + 52), 'fixe', lw=0.8)
for i in range(1, 6):
    line(ax, [(O[0] + i * u, O[1] - 0.8), (O[0] + i * u, O[1] + 0.8)], 'fixe', lw=0.7)
for j in range(1, 7):
    line(ax, [(O[0] - 0.8, O[1] + j * u), (O[0] + 0.8, O[1] + j * u)], 'fixe', lw=0.7)
A, B, C = P(1, 2), P(4, 6), P(4, 2)
line(ax, [A, C, B], 'fixe', lw=0.8, dash=True)
arrow(ax, A, B, 'sujet', lw=1.8)
disc(ax, A[0], A[1], 1.5, 'sujet')
disc(ax, B[0], B[1], 1.5, 'sujet')
text(ax, A[0] - 2.5, A[1] + 1, r'$A$ (1 ; 2)', 'sujet', 's', ha='right')
text(ax, B[0] - 2.5, B[1] + 2, r'$B$ (4 ; 6)', 'sujet', 's', ha='right')
text(ax, (A[0] + C[0]) / 2, A[1] - 3.5, '3 vers l’est', 'fixe', 's')
text(ax, C[0] + 2.5, (C[1] + B[1]) / 2, '4 vers le nord', 'fixe', 's', ha='left')
box(ax, 56, 44, 28, 12, 'sujet', label=r'$\overrightarrow{AB}$', size='xl')
text(ax, 70, 38, 'de $A$ vers $B$', 'sujet', 's')
text(ax, 21.5, 36, 'longueur 5', 'sujet', 's', rot=53.1)
save(fig, '41-022')
