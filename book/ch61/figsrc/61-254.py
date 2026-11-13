import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 22, 59, 'cos 20°', 'sujet', 'm'); text(ax, 66, 59, r'$\sqrt[3]{2}$', 'autre', 'm')
u = 12
line(ax, [(3, 34), (41, 34)], 'fixe'); line(ax, [(47, 34), (85, 34)], 'fixe')
for v in (-0.77, -0.17, 0.94): disc(ax, 22 + v * u, 34, 1.8, 'resultat')
disc(ax, 62 + 1.26 * u, 34, 1.8, 'resultat')
for sgn in (1, -1): disc(ax, 62 - 0.63 * u, 34 + sgn * 1.09 * u, 1.8, 'limite')
text(ax, 62 - 0.63 * u, 34 + 1.09 * u + 4.5, 'non réelle', 'limite', 's'); text(ax, 62 - 0.63 * u, 34 - 1.09 * u - 4.5, 'non réelle', 'limite', 's')
text(ax, 22, 28, 'droite des réels', 'fixe', 's')
text(ax, 22, 8, 'trois racines réelles', 'resultat', 's'); text(ax, 66, 8, 'une seule racine réelle', 'limite', 's')
save(fig, '61-254')
