import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u1, u2 = 5.5, 2.0
OL, OR = (6, 30), (50, 24)
L = lambda x, y: (OL[0] + x * u1, OL[1] + y * u1)
R = lambda x, y: (OR[0] + (2 * x + y) * u2, OR[1] + (x + 3 * y) * u2)
for i in range(3):
    for j in range(3):
        hi = (i, j) == (1, 1)
        poly(ax, [L(i, j), L(i + 1, j), L(i + 1, j + 1), L(i, j + 1)], 'sujet' if hi else 'fixe', lw=0.5)
        poly(ax, [R(i, j), R(i + 1, j), R(i + 1, j + 1), R(i, j + 1)], 'resultat' if hi else 'fixe', lw=0.5)
arrow(ax, (28, 38), (44, 38), 'varie'); text(ax, 36, 42, r'$T$', 'varie', 'm')
text(ax, 14.5, 25, r'côté $h$ = 0,1 cm', 'sujet', 's'); text(ax, 14.5, 20, r'aire $h^2$ = 0,01', 'sujet', 's')
text(ax, 14.5, 56, 'logo découpé : 12 cm²', 'sujet', 's'); text(ax, 62, 56, 'image : 60 cm²', 'resultat', 's')
text(ax, 62, 19, r'aire $5h^2$ = 0,05', 'resultat', 's')
box(ax, 4, 3, 80, 10, 'varie', label=r'1 200 carrés, chacun $\times5$ : 12 $\to$ 60', size='s')
save(fig, '76-105')
