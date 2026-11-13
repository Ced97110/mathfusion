import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
c = (31, 36); s = 9.0
def P(r, d): return (c[0] + s * r * math.cos(math.radians(d)), c[1] + s * r * math.sin(math.radians(d)))
def arc(r, d0, d1, n=50): return [P(r, d0 + (d1 - d0) * i / n) for i in range(n + 1)]
line(ax, arc(2, 0, 360), 'fixe', dash=True)
for d in (0, 120, 240):
    line(ax, [c, P(2, d)], 'sujet', lw=0.9)
for d in (120, 240): disc(ax, *P(2, d), 1.6, 'sujet')
disc(ax, *P(2, 0), 1.6, 'resultat')
# three steps of 120° just outside the circle; the last one lands back on z0
for d0, role in ((4, 'varie'), (124, 'varie'), (244, 'varie')):
    pts = arc(2.45, d0, d0 + 112); line(ax, pts, role, lw=1.2); arrow(ax, pts[-3], pts[-1], role, lw=1.2)
text(ax, *P(3.05, 60), 'k = 1', 'varie', 's')
text(ax, *P(3.05, 180), 'k = 2', 'varie', 's')
text(ax, *P(3.05, 300), 'k = 3', 'varie', 's')
text(ax, P(2, 120)[0] - 3, P(2, 120)[1] + 2.5, '$z_1$', 'sujet', 's')
text(ax, P(2, 240)[0] - 3, P(2, 240)[1] - 2.5, '$z_2$', 'sujet', 's')
text(ax, P(2, 0)[0] + 3, P(2, 0)[1] + 3, '$z_0$', 'resultat', 's')
box(ax, 62, 44, 24, 12, 'varie', label='k = 3 : retour', size='s')
text(ax, 74, 38, '3 × 120° = 360°', 'varie', 's')
text(ax, 74, 33.5, 'un tour complet :', 'varie', 's')
text(ax, 74, 29, 'retour sur $z_0$', 'varie', 's')
save(fig, '39-094')
