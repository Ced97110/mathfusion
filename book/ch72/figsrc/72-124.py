import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
ox, oy = 44, 44
line(ax, [(ox - 22, oy - 22), (ox + 22, oy + 22)], 'limite', lw=1.4)
line(ax, [(ox - 22, oy + 22), (ox + 22, oy - 22)], 'limite', lw=1.4)
arrow(ax, (ox, oy), (ox + 20, oy), 'varie', lw=1.6)
text(ax, ox + 27, oy + 4, r'$(1,0)$', 'varie', 's'); text(ax, ox + 28, oy - 4, 'carré 1', 'varie', 's')
box(ax, 68, 63, 16, 7, 'limite', label='dim 1', size='s'); box(ax, 68, 19, 16, 7, 'limite', label='dim 1', size='s')
text(ax, 44, 8, 'même dimension : 1', 'resultat', 'm', weight='bold')
save(fig, '72-124')
