import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
ox, oy, u = 14, 8, 18
P = lambda x, y: (ox + x*u, oy + y*u)
arrow(ax, (ox-5, oy), (ox+60, oy), 'fixe', lw=0.8)
line(ax, [(ox, oy-3), (ox, oy+2.3*u)], 'fixe', lw=0.6)
n = 40
line(ax, [P(math.cos(k*math.pi/2/n), math.sin(k*math.pi/2/n)) for k in range(n+1)], 'sujet', lw=1.0, dash=True)
line(ax, [(ox, oy), P(1, 0)], 'fixe', lw=1.1); line(ax, [(ox, oy), P(0, 1)], 'resultat', lw=1.1); line(ax, [P(0, 1), P(0, 2)], 'limite', lw=1.1)
arrow(ax, P(.55, .1), P(.1, .55), 'varie', curve=0.35)
for q, r in ((P(1, 0), 'fixe'), (P(0, 1), 'resultat'), (P(0, 2), 'limite')):
    disc(ax, q[0], q[1], 1.3, r)
text(ax, P(1, 0)[0], oy-4, '1', 'fixe', 'm')
text(ax, ox-3, P(0, 1)[1], '$i$', 'resultat', 'm')
text(ax, ox-4, P(0, 2)[1], '$2i$', 'limite', 'm')
text(ax, 64, 54, r'$\times\,i$ : rotation', 'resultat', 'm', weight='bold')
text(ax, 64, 47, 'module 1 : même distance', 'resultat', 's')
text(ax, 64, 31, r'$\times\,2i$ : pas une rotation', 'limite', 'm', weight='bold')
text(ax, 64, 24, 'module 2 : 2 fois plus loin', 'limite', 's')
text(ax, ox+26, oy+9, 'cercle de rayon 1', 'sujet', 's')
save(fig, '75-167')
