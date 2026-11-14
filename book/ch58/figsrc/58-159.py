import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
s = 7.0; ox, oy = 8.0, 28.0
P = lambda x, y: (ox + s * x, oy + s * y)
line(ax, [P(-0.5, 0), P(4.2, 0)], 'fixe', lw=0.5)
line(ax, [P(0, -2.5), P(0, 3.2)], 'fixe', lw=0.5)
arrow(ax, P(0, 0), P(3, 1), 'sujet', lw=1.5)
disc(ax, *P(0, 0), 1.3, 'varie')
text(ax, P(3, 1)[0] + 1, P(3, 1)[1] + 4, '(3, 1)', 'sujet', 's')
text(ax, P(0, 0)[0] + 10, P(0, 0)[1] - 7, '(0, 0) : un point', 'varie', 's')
text(ax, 22, 56, 'la famille', 'fixe', 's')
# la relation
box(ax, 46, 38, 40, 10, 'varie', label=r'$1\times(0,\,0)=(0,\,0)$')
box(ax, 46, 24, 40, 10, 'sujet', label=r'$0\times(3,\,1)=(0,\,0)$')
text(ax, 66, 52, 'nombres 1 et 0', 'fixe', 's')
line(ax, [(48, 19), (84, 19)], 'fixe')
box(ax, 46, 6, 40, 10, 'resultat', label='somme : (0, 0)', weight='bold')
text(ax, 25, 10, r'$1\neq 0$ : liée', 'resultat', 's')
save(fig, '58-159')
