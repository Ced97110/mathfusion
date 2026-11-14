import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 11; ox, oy = 44, 12
P = lambda x, y: (ox + x * u, oy + y * u)
for i in range(-3, 4): line(ax, [P(i, 0), P(i, 3.4)], 'fixe', lw=0.2)
for j in range(0, 4): line(ax, [P(-3, j), P(3, j)], 'fixe', lw=0.2)
arrow(ax, P(-3, 0), P(3.4, 0), 'fixe', lw=0.7); arrow(ax, P(0, 0), P(0, 3.5), 'fixe', lw=0.7)
r = math.sqrt(5); a0 = math.atan2(1, 2); a1 = a0 + math.pi / 2
pts = [P(r * math.cos(a0 + (a1 - a0) * k / 30), r * math.sin(a0 + (a1 - a0) * k / 30)) for k in range(31)]
line(ax, pts[:-2], 'varie', lw=1.4); arrow(ax, pts[-3], pts[-1], 'varie', lw=1.4)
line(ax, [P(0, 0), P(2, 1)], 'fixe', lw=0.8, dash=True); line(ax, [P(0, 0), P(-1, 2)], 'fixe', lw=0.8, dash=True)
disc(ax, *P(2, 1), 1.2, 'sujet'); disc(ax, *P(-1, 2), 1.2, 'resultat')
text(ax, *P(2.15, 1.0), '(2, 1)', 'sujet', 'm', ha='left')
text(ax, *P(-1.2, 2.0), '(−1, 2)', 'resultat', 'm', ha='right')
text(ax, *P(0.95, 2.75), 'T', 'varie', 'l', weight='bold')
text(ax, *P(1.6, 3.2), 'quart de tour', 'varie', 's')
text(ax, 44, 4, '(x, y)  devient  (−y, x)', 'encre', 's')
save(fig, '57-009')
