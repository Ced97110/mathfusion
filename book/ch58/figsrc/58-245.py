import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u = 5.5
def panel(ox, second):
    oy = 20
    P = lambda a, b: (ox + a * u, oy + b * u)
    arrow(ax, P(-2.6, 0), P(4.4, 0), 'sujet', lw=1.1)
    if second == 'vert':
        arrow(ax, P(0, -0.6), P(0, 3.9), 'autre', lw=1.1)
        pa, pb = (1, 0), (0, 3)
    else:
        arrow(ax, P(-0.6, -0.6), P(3.9, 3.9), 'autre', lw=1.1)
        pa, pb = (-2, 0), (3, 3)
    line(ax, [P(*pa), P(1, 3)], 'resultat', dash=True)
    line(ax, [P(*pb), P(1, 3)], 'resultat', dash=True)
    disc(ax, *P(*pa), 1.3, 'sujet'); disc(ax, *P(*pb), 1.3, 'autre'); disc(ax, *P(1, 3), 1.5, 'resultat')
    return P, pa, pb
P1, a1, b1 = panel(15, 'vert')
P2, a2, b2 = panel(62, 'diag')
text(ax, 22, 58, 'coupure 1', 'encre', 'm', weight='bold')
text(ax, 66, 58, 'coupure 2', 'encre', 'm', weight='bold')
text(ax, P1(1, 0)[0], P1(1, 0)[1] - 4.5, '(1, 0)', 'sujet', 's')
text(ax, P1(0, 3)[0] - 7, P1(0, 3)[1] + 1, '(0, 3)', 'autre', 's')
text(ax, P1(1, 3)[0] + 7, P1(1, 3)[1] + 3, '(1, 3)', 'resultat', 's', weight='bold')
text(ax, P2(-2, 0)[0], P2(-2, 0)[1] - 4.5, '(−2, 0)', 'sujet', 's')
text(ax, P2(3, 3)[0] + 3.5, P2(3, 3)[1] - 3.5, '(3, 3)', 'autre', 's')
text(ax, P2(1, 3)[0] - 6, P2(1, 3)[1] + 3, '(1, 3)', 'resultat', 's', weight='bold')
text(ax, 44, 6, 'même couple, deux coupures', 'fixe', 's')
save(fig, '58-245')
