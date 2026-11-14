import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 76 / 196; x0 = 6
a, m, c = 25 * u, 90 * u, 81 * u
text(ax, 4, 54, 'gauche : 25 + 90 + 81 = 196', 'encre', 's', ha='left')
box(ax, x0, 38, a, 8, 'fixe', label='25', size='s', dash=True); box(ax, x0 + a, 38, m, 8, 'varie', label='2xy = 90', size='s'); box(ax, x0 + a + m, 38, c, 8, 'fixe', label='81', size='s', dash=True)
text(ax, x0 + a / 2, 49.5, r'$x^2$', 'fixe', 's'); text(ax, x0 + a + m + c / 2, 49.5, r'$y^2$', 'fixe', 's')
text(ax, 44, 30, '=', 'encre', 'l')
box(ax, x0, 12, a, 8, 'fixe', label='25', size='s', dash=True); box(ax, x0 + a, 12, m, 8, 'varie', label='288 − 198', size='s'); box(ax, x0 + a + m, 12, c, 8, 'fixe', label='81', size='s', dash=True)
text(ax, x0 + a + m / 2, 6, r'$2h^2 - 2rp\cos(A+B)$', 'varie', 's')
text(ax, 4, 24, 'droite', 'encre', 's', ha='left')
text(ax, 66, 24, 'retirés des deux côtés', 'fixe', 's')
save(fig, '34-058')
