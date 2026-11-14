import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
ox, oy, u = 24, 30, 20
arrow(ax, (ox - 14, oy), (ox + 54, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 9), (ox, oy + 36), 'fixe', lw=0.8)
arrow(ax, (ox, oy), (ox, oy + u), 'sujet', lw=1.8)
arrow(ax, (ox, oy), (ox + u, oy), 'varie', lw=1.8)
arrow(ax, (ox + 2, oy + u - 1), (ox + u - 1, oy + 2), 'varie', curve=-0.35)
text(ax, ox + 3, oy + u + 8, r'$w=(0,1)$', 'sujet', 's', ha='left')
text(ax, ox + u + 4, oy - 4, r'$(\lambda-2)w=(1,0)$', 'varie', 's', ha='left')
text(ax, ox + 26, oy + 16, r'$\times(\lambda-2)$', 'varie', 's')
box(ax, 8, 4, 72, 11, 'resultat', label=r'$e=2$ vecteurs : une base du plan', size='s')
text(ax, 44, 21, r'$A$ de lignes (2, 1) et (0, 2)', 'encre', 's')
save(fig, '60-180')
