import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
ox, oy, R = 44, 52, 17
line(ax, [(ox - 24, oy), (ox + 24, oy)], 'fixe', lw=0.6)
line(ax, [(ox, oy - 22), (ox, oy + 22)], 'fixe', lw=0.6)
th = [math.radians(a) for a in range(0, 361, 6)]
line(ax, [(ox + R * math.cos(t), oy + R * math.sin(t)) for t in th], 'fixe', lw=0.5, dash=True)
arrow(ax, (ox, oy), (ox + R, oy), 'sujet', lw=1.3)
arrow(ax, (ox, oy), (ox, oy + R), 'varie', lw=1.3)
arrow(ax, (ox, oy), (ox - R, oy), 'varie', lw=1.3)
text(ax, ox + R + 4, oy - 3, r'$v$', 'sujet', 'm')
text(ax, ox + 7, oy + R + 2, r'$T(v)$', 'varie', 'm')
text(ax, ox - R - 2, oy + 4, r'$T(T(v))$', 'varie', 's', ha='right') if False else text(ax, 14, oy + 3.5, r'$T(T(v))$', 'varie', 's', ha='center')
arrow(ax, (ox + 11, oy + 4), (ox + 3.5, oy + 11), 'varie', curve=0.3, lw=0.8)
arrow(ax, (ox - 3.5, oy + 11), (ox - 11, oy + 4), 'varie', curve=0.3, lw=0.8)
text(ax, 72, 62, 'quart de tour', 'varie', 's')
box(ax, 8, 8, 72, 12, 'resultat', label=r'$T(T(v))+v=0$', size='m')
text(ax, 44, 26, r'$x^2+1$ annule $T$', 'resultat', 's')
save(fig, '54-277')
