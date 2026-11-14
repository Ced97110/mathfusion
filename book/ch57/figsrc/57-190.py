import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, s = 14, 16, 11.0
P = lambda x, y: (ox + x * s, oy + y * s)
for x in range(6):
    for y in range(4):
        r = 'sujet' if x % 2 == 0 else 'varie'
        disc(ax, P(x, y)[0], P(x, y)[1], 1.9, r)
arrow(ax, (P(1, 3)[0], P(1, 3)[1] + 3), (P(5, 3)[0], P(5, 3)[1] + 3), 'resultat', curve=-0.35, both=True)
text(ax, P(3, 3)[0], P(3, 3)[1] + 11, '(1 ; 3) et (5 ; 3) : même classe', 'resultat', 's')
brace(ax, P(0, 0)[0] - 2, P(5, 0)[0] + 2, P(0, 0)[1] - 3, 'fixe', label='reste de x : 0 ou 1  (fini)')
arrow(ax, (6, P(0, 0)[1]), (6, P(0, 3)[1]), 'fixe')
text(ax, 6, P(0, 3)[1] + 4, 'y', 'fixe', 's')
text(ax, 62, 6, 'y : tous les entiers (infini)', 'fixe', 's')
text(ax, 79, 44, 'reste 0', 'sujet', 's')
text(ax, 79, 40, 'reste 1', 'varie', 's')
save(fig, '57-190')
