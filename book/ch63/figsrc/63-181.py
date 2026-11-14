import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
# gauche : corps où 2 = 0, x^2 - a = (x - u)^2, une seule racine comptée deux fois
# droite : x^2 - 2 sur les fractions, deux racines distinctes
text(ax, 21, 76, r'$2 = 0$ : $x^2 - a$', 'limite', 'm', weight='bold')
text(ax, 67, 76, r'fractions : $x^2 - 2$', 'fixe', 'm', weight='bold')
line(ax, [(44, 8), (44, 72)], 'fixe', dash=True)
y = 56
arrow(ax, (4, y), (40, y), 'fixe', lw=0.7)
disc(ax, 22, y, 2.2, 'limite'); disc(ax, 22, y, 4.0, 'limite', fill=False, lw=0.8)
text(ax, 22, y + 8, r'$u$ compté 2 fois', 'limite', 's')
text(ax, 21, 42, r'$(x - u)(x - u)$', 'limite', 'm')
text(ax, 21, 32, r'$\eta(u) = u$ : groupe $\{1\}$', 'limite', 's')
box(ax, 4, 14, 34, 11, 'limite', label='groupe 1 < degré 2', size='s')
arrow(ax, (48, y), (84, y), 'fixe', lw=0.7)
disc(ax, 56, y, 2.2, 'resultat'); disc(ax, 76, y, 2.2, 'resultat')
text(ax, 56, y + 6, r'$-\sqrt{2}$', 'resultat', 's'); text(ax, 76, y + 6, r'$\sqrt{2}$', 'resultat', 's')
arrow(ax, (58.5, y - 4), (73.5, y - 4), 'varie', both=True, curve=0.0)
text(ax, 67, 42, '2 racines distinctes', 'resultat', 's')
text(ax, 67, 32, 'groupe à 2 éléments', 'resultat', 's')
box(ax, 50, 14, 34, 11, 'resultat', label='groupe 2 = degré 2', size='s')
save(fig, '63-181')
