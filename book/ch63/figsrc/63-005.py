import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'$a+bi\ \mapsto\ a-bi$', 'varie', 'l')
ox, oy, u = 10, 40, 13
arrow(ax, (2, oy), (50, oy), 'fixe')
text(ax, 49, 44, 'réels', 'fixe', 's', ha='right')
px = ox + 2 * u
text(ax, px + 4, oy - 4, '2', 'fixe', 's')
disc(ax, px, oy + u, 1.7, 'sujet')
disc(ax, px, oy - u, 1.7, 'varie')
text(ax, px + 4, oy + u, r'$2+i$', 'sujet', 'm', ha='left')
text(ax, px + 4, oy - u, r'$2-i$', 'varie', 'm', ha='left')
arrow(ax, (px, oy + u - 3), (px, oy - u + 3), 'varie')
text(ax, 71, 68, 'même carré', 'resultat', 's')
box(ax, 56, 48, 30, 12, 'resultat', label=r'$i^2=-1$')
box(ax, 56, 22, 30, 12, 'resultat', label=r'$(-i)^2=-1$')
save(fig, '63-005')
