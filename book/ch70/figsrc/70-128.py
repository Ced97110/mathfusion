import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, u = 22, 36, 14
arrow(ax, (ox - 14, oy), (ox + 18, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy - 22), (ox, oy + 22), 'fixe', lw=0.7)
text(ax, ox + 14, oy - 3, 'réel', 'fixe', 's')
text(ax, ox + 2, oy + 25, 'imaginaire', 'fixe', 's', ha='left')
arrow(ax, (ox + 5, oy + u - 2), (ox + 5, oy - u + 2), 'varie', lw=0.9, both=True)
text(ax, ox + 7, oy + 6, 'conjugués', 'varie', 's', ha='left')
for s, nm, yb in ((1, r'$i$', 50), (-1, r'$-i$', 22)):
    disc(ax, ox, oy + s * u, 1.4, 'sujet')
    text(ax, ox - 3, oy + s * u + 2.3, nm, 'sujet', 's', ha='right')
box(ax, 62, 44, 24, 11, 'sujet', label=r'$(1,\ i)$')
box(ax, 62, 17, 24, 11, 'sujet', label=r'$(1,\ -i)$')
arrow(ax, (ox + 2, oy + u + 0.5), (62, 49.5), 'fixe', lw=0.7, curve=-0.15)
arrow(ax, (ox + 2, oy - u - 0.5), (62, 22.5), 'fixe', lw=0.7, curve=0.15)
text(ax, 74, 36, 'même\nabscisse : 1', 'resultat', 's')
save(fig, '70-128')
