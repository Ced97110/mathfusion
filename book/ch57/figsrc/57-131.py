import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 2, 14, 84, 42, 'fixe')
text(ax, 8, 51, r'$\mathbb{R}^2$', 'fixe', 'm')
u = 13.0; ox, oy = 18.0, 36.0
P = lambda x, y: (ox + x * u, oy + y * u)
for i in range(-1, 5):
    disc(ax, *P(i, 0), 1.2, 'sujet')
text(ax, 52, 51, r'$\mathbb{Z}^2$ : les points $(n\,;\,0)$', 'sujet', 's')
a = P(1, 0)
arrow(ax, (a[0] + 1.5, oy + 2), (P(3, 0)[0] - 1.5, oy + 2), 'varie', curve=-0.5)
text(ax, P(2, 0)[0], oy + 9.5, r'$\times 3$', 'varie', 's')
disc(ax, *P(0.5, 0), 1.2, 'limite', fill=False)
arrow(ax, (a[0] - 1.5, oy - 2), (P(0.5, 0)[0] + 1.5, oy - 2), 'varie', curve=-0.6)
text(ax, P(0.75, 0)[0], oy - 8.5, r'$\times\frac{1}{2}$', 'varie', 's')
text(ax, P(0.5, 0)[0] + 8, oy - 13, r'$(\frac{1}{2}\,;\,0)\notin\mathbb{Z}^2$', 'limite', 's')
text(ax, 44, 9, r'coefficients $\mathbb{Z}$ : $\mathbb{Z}^2$ est stable', 'resultat', 's')
text(ax, 44, 3.5, r'coefficients $\mathbb{R}$ : $\mathbb{Z}^2$ sort', 'limite', 's')
save(fig, '57-131')
