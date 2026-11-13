import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 36, 38, 24, 'resultat'); text(ax, 21, 55, r'$S_4$ : 24', 'resultat', 'm'); box(ax, 8, 39, 26, 10, 'sujet', label='4 éléments')
box(ax, 2, 6, 38, 24, 'resultat'); text(ax, 21, 25, r'$S_6$ : 720', 'resultat', 'm'); box(ax, 8, 9, 26, 10, 'sujet', label='6 éléments')
line(ax, [(44, 4), (44, 60)], 'fixe', dash=True)
box(ax, 48, 32, 20, 22, 'fixe'); text(ax, 58, 49, r'$S_n$ : fini', 'fixe', 's')
for i in range(8): disc(ax, 52 + i * 4.8, 38, 1.7, 'limite')
text(ax, 62, 26, r'$\mathbb{Z}$ : infini', 'limite', 'm'); text(ax, 62, 20, 'ne rentre pas', 'limite', 's')
save(fig, '45-093')
