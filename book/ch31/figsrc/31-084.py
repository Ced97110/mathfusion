import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$\cos^2 x = 1 - \sin x$', 'sujet', 'l')
box(ax, 3, 6, 82, 42, 'fixe', dash=True)
text(ax, 44, 43, 'toutes les valeurs de l’angle', 'fixe', 's')
box(ax, 8, 8, 44, 30, 'resultat', dash=True)
text(ax, 30, 33, 'solutions : vrai', 'resultat', 's')
for i, v in enumerate(['0°', '90°', '180°', '360°']):
    x = 16 + (i % 2) * 20; y = 25 - (i // 2) * 10
    disc(ax, x, y, 4.2, 'resultat', label=v, size='s')
disc(ax, 70, 22, 4.2, 'limite', label='45°', size='s')
text(ax, 70, 31, 'faux', 'limite', 's')
text(ax, 70, 14, '0,5 ≠ 0,2929', 'limite', 's')
save(fig, '31-084')
