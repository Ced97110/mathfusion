import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
u = 10; ox, oy = 44, 20
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, P(-3, 0), P(3.3, 0), 'fixe', lw=0.7); arrow(ax, P(0, -1.5), P(0, 2.6), 'fixe', lw=0.7)
v = (2, 0.8); r = math.hypot(*v); a0 = math.atan2(v[1], v[0])
def arc(ra, b0, b1, role):
    pts = [P(ra * math.cos(b0 + (b1 - b0) * k / 30), ra * math.sin(b0 + (b1 - b0) * k / 30)) for k in range(31)]
    line(ax, pts[:-2], role, lw=1.3); arrow(ax, pts[-3], pts[-1], role, lw=1.3)
arc(1.2, a0, a0 + math.pi / 2, 'varie'); arc(1.2, a0 + math.pi / 2, a0 + math.pi, 'varie')
line(ax, [P(2, 0.8), P(-2, -0.8)], 'fixe', lw=0.8, dash=True)
pts = [(2, 0.8, 'sujet'), (-0.8, 2, 'varie'), (-2, -0.8, 'resultat')]
for x, y, role in pts:
    arrow(ax, P(0, 0), P(x, y), role, lw=1.1); disc(ax, *P(x, y), 1.1, role)
text(ax, *P(2.1, 1.45), 'v (2 ; 0,8)', 'sujet', 'm')
text(ax, *P(-0.6, 2.3), 'T v (−0,8 ; 2)', 'varie', 'm', ha='left')
text(ax, *P(-2, -1.35), 'T²v (−2 ; −0,8)', 'resultat', 'm')
text(ax, *P(0.75, 1.6), 'T', 'varie', 'm', weight='bold')
text(ax, *P(-1.35, 0.55), 'T', 'varie', 'm', weight='bold')
text(ax, *P(1.9, -1.2), 'T²v = −v', 'resultat', 'l', weight='bold')
save(fig, '57-011')
