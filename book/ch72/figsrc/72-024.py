import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ox, oy, u = 22, 32, 9
P = lambda x, y: (ox + x*u, oy + y*u)
arrow(ax, P(-2.3, 0), P(2.3, 0), 'fixe', lw=0.6); arrow(ax, P(0, -2.3), P(0, 2.3), 'fixe', lw=0.6)
line(ax, [P(-2.1, -2.1), P(2.1, 2.1)], 'limite', lw=1.1); line(ax, [P(-2.1, 2.1), P(2.1, -2.1)], 'limite', lw=1.1)
arrow(ax, P(0, 0), P(1, 1), 'sujet', lw=1.6)
text(ax, *P(1.9, 0.6), r'$u=(1,1)$', 'sujet', 's')
text(ax, 68, 57, 'carré de $u$', 'sujet', 's')
box(ax, 53, 44, 30, 9, 'limite', label=r'$1-1=0$', size='m')
arrow(ax, (68, 43), (68, 38), 'varie', lw=0.9)
text(ax, 68, 33, r'$\frac{B(y,u)}{B(u,u)}=\frac{B(y,u)}{0}$', 'encre', 'm')
text(ax, 68, 17, 'division par 0', 'limite', 'm'); text(ax, 68, 11, 'impossible', 'limite', 'm')
save(fig, '72-024')
