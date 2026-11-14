import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
u = 7.5; oy = 14
v = (2, 0.8); a0 = math.atan2(v[1], v[0])
def panel(ox, mid):
    P = lambda x, y: (ox + x * u, oy + y * u)
    arrow(ax, P(-2.5, 0), P(2.7, 0), 'fixe', lw=0.6); arrow(ax, P(0, -1.3), P(0, 2.8), 'fixe', lw=0.6)
    return P
P1 = panel(22, 0)
arrow(ax, P1(2, 0.8), P1(-2, -0.8), 'varie', lw=1.6)
disc(ax, *P1(2, 0.8), 1.1, 'sujet'); disc(ax, *P1(-2, -0.8), 1.1, 'resultat')
text(ax, *P1(2.1, 1.5), 'v', 'sujet', 'm'); text(ax, *P1(-2.1, -1.55), '−v', 'resultat', 'm')
text(ax, 22, 40, '× (−1)', 'varie', 'l', weight='bold')
P2 = panel(66, 0)
def arc(ra, b0, b1):
    pts = [P2(ra * math.cos(b0 + (b1 - b0) * k / 30), ra * math.sin(b0 + (b1 - b0) * k / 30)) for k in range(31)]
    line(ax, pts[:-2], 'varie', lw=1.5); arrow(ax, pts[-3], pts[-1], 'varie', lw=1.5)
arc(1.6, a0, a0 + math.pi / 2); arc(1.6, a0 + math.pi / 2, a0 + math.pi)
disc(ax, *P2(2, 0.8), 1.1, 'sujet'); disc(ax, *P2(-0.8, 2), 1.1, 'fixe'); disc(ax, *P2(-2, -0.8), 1.1, 'resultat')
text(ax, *P2(2.1, 1.5), 'v', 'sujet', 'm'); text(ax, *P2(-1.55, 2.6), 'T v', 'fixe', 'm')
text(ax, *P2(-2.1, -1.55), '−v', 'resultat', 'm')
text(ax, 66, 40, 'T puis T', 'varie', 'l', weight='bold')
text(ax, 44, 22, '=', 'resultat', 'xl', weight='bold')
save(fig, '57-012')
