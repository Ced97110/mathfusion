import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
s = 11
def panel(ox, oy, u, v, name, b, c, lp):
    P = lambda x, y: (ox + x * s, oy + y * s)
    line(ax, [P(-0.2, 0), P(2.5, 0)], 'fixe', lw=0.6); line(ax, [P(0, -0.2), P(0, 3.3)], 'fixe', lw=0.6)
    arrow(ax, P(0, 0), P(*u), 'sujet', lw=1.2); arrow(ax, P(0, 0), P(*v), 'resultat', lw=1.2)
    arrow(ax, P(u[0], u[1]), P(*v), 'varie', lw=1.0)
    text(ax, *P(u[0] + 0.3, u[1] - 0.35), r'$u$', 'sujet', 'm'); text(ax, *P(v[0] + 0.3, v[1] + 0.1), r"$u'$", 'resultat', 'm')
    mid = ((u[0] + v[0]) / 2, (u[1] + v[1]) / 2); dx = (v[0] - u[0]); dy = (v[1] - u[1])
    text(ax, *P(mid[0] + lp[0], mid[1] + lp[1]), r"$u'-u$", 'varie', 's', ha=lp[2])
    text(ax, ox + 18, 15, b, 'encre', 's'); text(ax, ox + 18, 9, r'$c\,B(u,w)=-1$', 'encre', 's'); text(ax, ox + 18, 68, name, 'encre', 's')
panel(6, 28, (1, 0), (2, 1), 'essai 1', r'$B(u,u^{\prime})=1,\ c=1$', 0, (0.55, -0.05, 'left'))
panel(50, 24, (1, 1), (1, 3), 'essai 2', r'$B(u,u^{\prime})=2,\ c=1/2$', 0, (0.12, 0, 'left'))
text(ax, 44, 2.5, r'$w=u-u^{\prime}$ : on arrive en $u^{\prime}$', 'varie', 's')
save(fig, '75-082')
