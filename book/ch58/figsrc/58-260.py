import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
u = 5.5
def panel(ox, diag):
    oy = 22
    P = lambda a, b: (ox + a * u, oy + b * u)
    arrow(ax, P(-2.6, 0), P(4.4, 0), 'sujet', lw=1.1)
    if diag:
        arrow(ax, P(-0.6, -0.6), P(3.9, 3.9), 'autre', lw=1.1)
        pa, pb = (-2, 0), (3, 3)
        # arc entre les deux droites (45°)
        pts = [(ox + 5 * math.cos(t), oy + 5 * math.sin(t)) for t in [i * math.pi / 4 / 12 for i in range(13)]]
        line(ax, pts, 'encre', lw=0.8)
    else:
        arrow(ax, P(0, -0.6), P(0, 3.9), 'autre', lw=1.1)
        pa, pb = (1, 0), (0, 3)
        line(ax, [(ox + 3, oy), (ox + 3, oy + 3), (ox, oy + 3)], 'encre', lw=0.8)
    line(ax, [P(*pa), P(1, 3)], 'resultat', dash=True)
    line(ax, [P(*pb), P(1, 3)], 'resultat', dash=True)
    disc(ax, *P(*pa), 1.3, 'sujet'); disc(ax, *P(*pb), 1.3, 'autre'); disc(ax, *P(1, 3), 1.5, 'resultat')
    return P
P1 = panel(15, False)
P2 = panel(62, True)
text(ax, 22, 59, 'angle droit', 'encre', 'm', weight='bold')
text(ax, 66, 59, 'angle quelconque', 'encre', 'm', weight='bold')
text(ax, 26, P1(1, 0)[1] - 6.5, '(1, 3) = (1, 0) + (0, 3)', 'resultat', 's')
text(ax, P1(1, 3)[0] + 1, P1(1, 3)[1] + 4, '(1, 3)', 'resultat', 's', weight='bold')
text(ax, 66, P2(-2, 0)[1] - 6.5, '(1, 3) = (−2, 0) + (3, 3)', 'resultat', 's')
text(ax, P2(1, 3)[0] + 1, P2(1, 3)[1] + 4, '(1, 3)', 'resultat', 's', weight='bold')
text(ax, 44, 6, 'deux directions distinctes', 'resultat', 's', weight='bold')
save(fig, '58-260')
