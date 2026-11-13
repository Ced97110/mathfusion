import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 8; ox, oy = 8, 14
for i in range(3):
    for j in range(3):
        poly(ax, [(ox + i * u, oy + j * u), (ox + (i + 1) * u, oy + j * u), (ox + (i + 1) * u, oy + (j + 1) * u), (ox + i * u, oy + (j + 1) * u)], 'varie')
poly(ax, [(ox, oy), (ox + u, oy), (ox + u, oy + u), (ox, oy + u)], 'sujet')
brace(ax, ox, ox + u, oy, 'sujet', label='1', down=True, depth=1.4)
brace(ax, ox, ox + 3 * u, oy - 8, 'varie', label='3', down=True, depth=1.4)
text(ax, 56, 40, 'carré unité : aire 1', 'sujet', 's', ha='left')
text(ax, 56, 34, r'chaque côté $\times3$', 'varie', 's', ha='left')
text(ax, 56, 28, r'aire $=3\times3=9$', 'varie', 's', ha='left')
text(ax, 56, 20, r'$T(3)=3+3=6$', 'resultat', 's', ha='left')
text(ax, 56, 14, r'$N(3)=3^2=9$', 'resultat', 's', ha='left')
text(ax, 56, 7, r'$\mathbb{C}$ sur $\mathbb{R}$ : $n=2$', 'autre', 's', ha='left')
save(fig, '77-096')
