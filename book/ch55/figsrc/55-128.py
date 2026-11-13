import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
e1, e2 = 5, 3      # x^2 - 5x + 3 : sum 5, product 3
assert e1 ** 3 - 3 * e1 * e2 == 80 and 3 * e1 * e2 == 45
box(ax, 4, 66, 40, 9, 'sujet', label=r'$x^2-5x+3$', size='m')
# main path: coefficients only
arrow(ax, (16, 66), (14, 59.5), 'varie')
arrow(ax, (32, 66), (34, 59.5), 'varie')
box(ax, 2, 50, 22, 9, 'varie', label=r'$e_1=5$', size='m')
box(ax, 26, 50, 22, 9, 'varie', label=r'$e_2=3$', size='m')
arrow(ax, (13, 50), (22, 43.5), 'varie')
arrow(ax, (37, 50), (28, 43.5), 'varie')
box(ax, 2, 34, 46, 9, 'resultat', label=r'$125-3\times5\times3$', size='s')
arrow(ax, (25, 34), (25, 27.5), 'resultat')
box(ax, 10, 17, 30, 10, 'resultat', label='80', size='xl', weight='bold')
text(ax, 25, 11, r'sans racine carrée', 'resultat', 's')
# bypassed path: the roots themselves
arrow(ax, (44, 70), (58, 70), 'fixe')
box(ax, 58, 58, 28, 18, 'fixe', dash=True, label='')
text(ax, 72, 70, 'les racines', 'fixe', 's')
text(ax, 72, 63, r'$\frac{5\pm\sqrt{13}}{2}$', 'fixe', 'm')
text(ax, 72, 50, 'inutiles ici', 'fixe', 's')
text(ax, 72, 44, r'$r_1^3+r_2^3$', 'sujet', 'm')
text(ax, 72, 38, 'se calcule sans elles', 'fixe', 's')
save(fig, '55-128')
