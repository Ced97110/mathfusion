import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, r'$uv=2$ sur $\mathbb{F}_3$', 'encre', 'm')
text(ax, 20, 51, r'$u$', 'sujet', 'm'); text(ax, 68, 51, r'$v$', 'resultat', 'm')
Y = {0: 41, 1: 28, 2: 15}
for k in range(3):
    disc(ax, 20, Y[k], 4.2, 'fixe' if k == 0 else 'sujet', label=str(k))
    disc(ax, 68, Y[k], 4.2, 'fixe' if k == 0 else 'resultat', label=str(k))
arrow(ax, (25, Y[1]), (63, Y[2]), 'varie')
arrow(ax, (25, Y[2]), (63, Y[1]), 'varie')
text(ax, 44, Y[0], r'$0\times v=0\neq2$', 'limite', 's')
text(ax, 44, 4, r'$q-1=2$ couples', 'resultat', 'm')
save(fig, '75-133')
