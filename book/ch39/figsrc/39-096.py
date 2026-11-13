import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
s = 11.0
def mk(c):
    P = lambda r, d: (c[0] + s * r * math.cos(math.radians(d)), c[1] + s * r * math.sin(math.radians(d)))
    arc = lambda r, d0, d1, n=50: [P(r, d0 + (d1 - d0) * i / n) for i in range(n + 1)]
    return P, arc
# top: cube roots of 8 (radius 2)
c1 = (34, 76); P, arc = mk(c1)
arrow(ax, (c1[0] - 25, c1[1]), (c1[0] + 26, c1[1]), 'fixe', lw=0.5)
arrow(ax, (c1[0], c1[1] - 25), (c1[0], c1[1] + 25), 'fixe', lw=0.5)
line(ax, arc(2, 0, 360), 'fixe', dash=True)
for d in (0, 120, 240):
    line(ax, [c1, P(2, d)], 'sujet', lw=0.9); disc(ax, *P(2, d), 1.5, 'sujet')
text(ax, P(2, 0)[0] + 3, P(2, 0)[1] + 3, '$z_0$', 'sujet', 's')
text(ax, P(2, 120)[0] - 3.5, P(2, 120)[1] + 2.5, '$z_1$', 'sujet', 's')
text(ax, P(2, 240)[0] - 3.5, P(2, 240)[1] - 2.5, '$z_2$', 'sujet', 's')
text(ax, 72, 90, 'distance 2 de O', 'sujet', 's')
text(ax, 72, 85, 'écart de 120°', 'sujet', 's')
text(ax, c1[0] - 3, c1[1] - 3, 'O', 'fixe', 's')
# bottom: sixth roots of 1 (radius 1)
c2 = (34, 24); P, arc = mk(c2)
line(ax, arc(1, 0, 360), 'fixe', dash=True)
for k in range(6):
    disc(ax, *P(1, 60 * k), 1.3, 'resultat' if k == 3 else 'autre')
for k in range(3):
    pts = arc(1.5, 60 * k + 6, 60 * k + 54, 12); line(ax, pts, 'varie', lw=1.1); arrow(ax, pts[-3], pts[-1], 'varie', lw=1.1)
text(ax, P(1, 0)[0] + 2.5, P(1, 0)[1] + 2.5, '1', 'autre', 's')
text(ax, *P(2.0, 60), 'ω', 'varie', 'm', weight='bold')
text(ax, *P(2.0, 120), 'ω²', 'varie', 'm', weight='bold')
text(ax, P(1, 180)[0] - 3, P(1, 180)[1], 'ω³', 'resultat', 's', ha='right')
text(ax, 72, 34, 'distance 1 de O', 'autre', 's')
text(ax, 72, 29, 'écart de 60°', 'autre', 's')
text(ax, 72, 22, 'ω = cis 60°', 'varie', 's')
text(ax, 72, 17, 'ω³ = −1 :', 'resultat', 's')
text(ax, 72, 12.5, 'demi-tour', 'resultat', 's')
save(fig, '39-096')
