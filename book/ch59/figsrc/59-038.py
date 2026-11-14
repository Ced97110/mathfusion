import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def tb(ax, x, y, s, role, size='s'):
    ax.text(x, y, s, color=COL[role], fontsize=SIZE[size], ha='center', va='center', zorder=5, bbox=dict(fc='white', ec='none', pad=0.6))
ox, oy, u = 9, 9, 7.2
P = lambda a, b: (ox + a * u, oy + b * u)
for a in range(7):
    for b in range(7):
        disc(ax, *P(a, b), 0.5, 'fixe')
# base e1, e2
arrow(ax, P(0, 0), P(1, 0), 'fixe', lw=1.4); arrow(ax, P(0, 0), P(0, 1), 'fixe', lw=1.4)
text(ax, *P(1.0, -0.75), r'$e_1$', 'fixe', 'm'); text(ax, *P(-0.7, 1.0), r'$e_2$', 'fixe', 'm')
# f1 = 4e1 + 6e2 : droite puis haut
line(ax, [P(0, 0), P(4, 0), P(4, 6)], 'sujet', lw=1.3)
disc(ax, *P(4, 6), 1.5, 'sujet')
tb(ax, *P(2.4, -0.75), r'$4e_1$', 'sujet', 's')
tb(ax, *P(4.5, 2.0), r'$6e_2$', 'sujet', 's')
text(ax, *P(3.4, 6.7), r'$f_1$ (4, 6)', 'sujet', 'm')
# f2 = 6e1 + 4e2 : haut puis droite
line(ax, [P(0, 0), P(0, 4), P(6, 4)], 'autre', lw=1.3)
disc(ax, *P(6, 4), 1.5, 'autre')
tb(ax, *P(-0.7, 3.0), r'$4e_2$', 'autre', 's')
tb(ax, *P(1.8, 4.7), r'$6e_1$', 'autre', 's')
text(ax, P(6, 4)[0] + 2, P(6, 4)[1] + 0.2, r'$f_2$ (6, 4)', 'autre', 'm', ha='left')
text(ax, 86, 18, r'$f_1=4e_1+6e_2$', 'sujet', 'm', ha='right')
text(ax, 86, 10.5, r'$f_2=6e_1+4e_2$', 'autre', 'm', ha='right')
save(fig, '59-038')
