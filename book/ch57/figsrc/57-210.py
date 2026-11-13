import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, r'si $\frac{1}{6}$ agissait : il faudrait $x=6y$', 'encre', 'm')
ys = [60 - i * 8 for i in range(6)]
for i, y in enumerate(ys):
    disc(ax, 10, y, 3.0, 'sujet', label=str(i), size='s')
    arrow(ax, (13.8, y), (29.5, 40 + (y - 40) * 0.25), 'fixe', lw=0.6)
text(ax, 10, 11, r'$y\in\mathbb{Z}/6\mathbb{Z}$', 'sujet', 's')
box(ax, 30, 32, 24, 16, 'resultat', label=r'$6y=0$' + '\n' + 'pour tout $y$', size='s')
# x = 0 est atteint ; x = 1 à 5 ne l'est jamais
box(ax, 66, 46, 20, 10, 'resultat', label=r'$x=0$', size='m')
arrow(ax, (54.6, 44), (65.4, 50), 'resultat', lw=1.2)
box(ax, 66, 22, 20, 10, 'limite', label=r'$x=1$ à $5$', size='s')
line(ax, [(54.6, 36), (65.4, 28)], 'limite', lw=1.2)
line(ax, [(58.6, 34.2), (61.4, 29.8)], 'limite', lw=1.2)
line(ax, [(58.6, 29.8), (61.4, 34.2)], 'limite', lw=1.2)
text(ax, 76, 17.5, 'jamais atteint', 'limite', 's')
text(ax, 62, 5, 'seul $x=0$ : module nul', 'resultat', 's', weight='bold')
save(fig, '57-210')
