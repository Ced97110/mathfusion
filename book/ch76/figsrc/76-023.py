import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
ox, oy, u = 14, 12, 12
arrow(ax, (ox, oy), (ox + u, oy), 'sujet', lw=1.6); arrow(ax, (ox, oy), (ox, oy + u), 'sujet', lw=1.6)
line(ax, [(ox + u, oy), (ox + 5.5 * u, oy)], 'fixe', lw=0.5, dash=True)
line(ax, [(ox, oy + u), (ox, oy + 5 * u)], 'fixe', lw=0.5, dash=True)
text(ax, ox + u, oy - 3, '1', 'sujet', 'm'); text(ax, ox - 3.5, oy + u, r'$i$', 'sujet', 'm')
px, py = ox + 2 * u, oy + 3 * u
line(ax, [(px, oy), (px, py)], 'varie', dash=True); line(ax, [(ox, py), (px, py)], 'varie', dash=True)
disc(ax, px, py, 1.4, 'resultat')
text(ax, px + 3, py + 4, r'$2 + 3i$', 'resultat', 'm', ha='left', weight='bold')
text(ax, px, oy - 3, '2 devant 1', 'varie', 's'); text(ax, ox + 2, py + 3, '3 devant $i$', 'varie', 's', ha='left')
text(ax, 62, 62, r'base $(1,\ i)$', 'sujet', 'm', weight='bold')
text(ax, 62, 22, '2 nombres réels', 'varie', 'm'); text(ax, 62, 17, 'fixent un complexe', 'varie', 's')
save(fig, '76-023')
