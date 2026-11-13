import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy = 30, 35
arrow(ax, (6, oy), (54, oy), 'fixe', lw=0.8); arrow(ax, (ox, 10), (ox, 62), 'fixe', lw=0.8)
line(ax, [(ox - 24, oy - 24), (ox + 24, oy + 24)], 'limite', lw=1.4)
line(ax, [(ox - 24, oy + 24), (ox + 24, oy - 24)], 'limite', lw=1.4)
arrow(ax, (44, 49), (44, 21), 'varie', curve=-0.5, lw=1.2)
text(ax, 58, 62, r'$(1,1)$', 'limite', 's'); text(ax, 58, 8, r'$(1,-1)$', 'limite', 's')
text(ax, 74, 36, 'isométrie', 'varie', 's')
text(ax, 74, 30, 'carré 0', 'resultat', 's'); text(ax, 74, 26, 'des deux côtés', 'resultat', 's')
save(fig, '72-123')
