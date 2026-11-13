import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
x0, y0, d = 22, 16, 14
line(ax, [(x0 - 6, y0), (x0 + 2 * d + 6, y0)], 'limite', lw=1.2, dash=True)
for i in range(3):
    for j in range(3):
        role = 'limite' if j == 0 else 'resultat'
        if (i, j) == (1, 0): role = 'sujet'
        disc(ax, x0 + i * d, y0 + j * d, 3.0, role)
text(ax, x0 + d, y0 - 7, r'$u_1=(1,\,0)$', 'sujet', 's')
text(ax, x0 + d, 66, 'droite de $u_1$ : 3 points', 'limite', 's')
text(ax, 72, y0 + 2 * d + 2, '6 restent', 'resultat', 's')
text(ax, 72, y0 + d, r'$q^n-q=6$', 'resultat', 'l')
save(fig, '75-107')
