import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Fig. 40.2 : M (2 ; 60°) = (1 ; 1,73) et ses trois symétriques : rectangle centré en O
fig, ax = canvas(86)
o = (44, 46); u = 14
X, Y = u * 1.0, u * math.sqrt(3)
M = (o[0] + X, o[1] + Y); M1 = (o[0] + X, o[1] - Y); M2 = (o[0] - X, o[1] + Y); M3 = (o[0] - X, o[1] - Y)
arrow(ax, (o[0] - 36, o[1]), (o[0] + 38, o[1]), 'fixe', lw=0.9)
arrow(ax, (o[0], o[1] - 36), (o[0], o[1] + 36), 'fixe', lw=0.9)
text(ax, o[0] + 40, o[1] - 3, r'$x$', 'fixe', 's')
text(ax, o[0] + 3, o[1] + 37, r'$y$', 'fixe', 's')
# rectangle (côtés parallèles aux axes)
line(ax, [M, M1, M3, M2, M], 'fixe', lw=0.6, dash=True)
# trois pointillés partant de M
line(ax, [M, M1], 'varie', lw=0.9, dash=True)
line(ax, [M, M2], 'varie', lw=0.9, dash=True)
line(ax, [M, M3], 'varie', lw=0.9, dash=True)
disc(ax, M[0], M[1], 1.5, 'sujet')
for q in (M1, M2, M3):
    disc(ax, q[0], q[1], 1.5, 'varie')
disc(ax, o[0], o[1], 0.8, 'encre')
text(ax, o[0] + 3, o[1] - 3, 'O', 'encre', 's')
text(ax, M[0] + 14, M[1] + 3, r'$M$ (2 ; 60°)', 'sujet', 's')
text(ax, M1[0] + 15, M1[1] - 3, r'$M_1$ (2 ; $-$60°)', 'varie', 's')
text(ax, M2[0] - 14, M2[1] + 3, r'$M_2$ (2 ; 120°)', 'varie', 's')
text(ax, M3[0] - 14, M3[1] - 3, r'$M_3$ ($-$2 ; 60°)', 'varie', 's')
text(ax, 44, 5, 'quatre points, quatre coins d’un rectangle', 'encre', 'm')
save(fig, '40-035')
