import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
o = (14, 14); s = 22
G = lambda x, y: (o[0] + x * s, o[1] + y * s)
arrow(ax, G(-0.4, 0), G(1.9, 0), 'fixe', lw=0.6); arrow(ax, G(0, -0.4), G(0, 1.8), 'fixe', lw=0.6)
arrow(ax, G(1, 0), G(1, 1), 'varie', lw=1.3)
disc(ax, *G(1, 0), 1.1, 'sujet'); disc(ax, *G(1, 1), 1.1, 'limite')
text(ax, G(1, 0)[0] + 2, G(1, 0)[1] - 3, r'$x=(1,0)$ : $Q=0$', 'sujet', 's', ha='left')
text(ax, G(1, 1)[0] + 2, G(1, 1)[1] + 3, r'$x+z=(1,1)$ : $Q=1$', 'limite', 's', ha='left')
text(ax, G(1, 0.5)[0] + 2, G(1, 0.5)[1], r'$z=(0,1)$', 'varie', 's', ha='left')
text(ax, 44, 59, r'$Q(x,y)=xy$', 'sujet', 'm')
text(ax, 62, 30, r'$2B(x,z)=1\neq 0$', 'limite', 's', ha='center'); text(ax, 62, 25, r'$z$ hors du radical', 'limite', 's')
save(fig, '71-198')
