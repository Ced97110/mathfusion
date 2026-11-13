import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 5
def plane(ox, oy, pt, n, role):
    arrow(ax, (ox, oy), (ox + 7*u, oy), 'fixe', lw=1.0); arrow(ax, (ox, oy), (ox, oy + 5*u), 'fixe', lw=1.0)
    for v in range(1, 7): ax.plot([ox + v*u]*2, [oy - .8, oy + .8], color=COL['fixe'], lw=0.6)
    line(ax, [(ox + pt[0]*u, oy), (ox + pt[0]*u, oy + pt[1]*u), (ox, oy + pt[1]*u)], 'varie', dash=True)
    disc(ax, ox + pt[0]*u, oy + pt[1]*u, 1.6, role)
    text(ax, ox + pt[0]*u + 1, oy + pt[1]*u + 4.5, f'{pt[0]} ; {pt[1]}', role, 's')
    text(ax, ox + 3.5*u, oy - 5, r'$e_%d$ : position' % n, 'sujet', 's')
    text(ax, ox + 3.5*u, oy + 5*u + 5, r'plan $P_%d$' % n, role, 'm')
    text(ax, ox - 3.5, oy + 3.2*u + 4, r'$f_%d$' % n, 'sujet', 's')
plane(8, 14, (3, 2), 1, 'sujet')
plane(52, 14, (5, 2), 2, 'autre')
text(ax, 44, 3, r'$f_i$ : vitesse $\times$ masse', 'sujet', 's')
save(fig, '75-040')
