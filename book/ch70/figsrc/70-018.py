import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
s, ox, oy = 11.0, 44.0, 36.0
P = lambda x, y: (ox + s * x, oy + s * y)
r3 = 3 ** 0.5
arrow(ax, P(-2.5, 0), P(2.5, 0), 'fixe', lw=0.6)
arrow(ax, P(0, -2.5), P(0, 2.8), 'fixe', lw=0.6)
disc(ax, *P(0, 0), 2 * s, 'sujet', fill=False, lw=1.3)
line(ax, [P(t / 20, (t / 20) ** 2 - 2) for t in range(-40, 41)], 'varie', lw=1.3)
# horizontal ruler through C : touches both curves without cutting them
line(ax, [P(-1.7, -2), P(1.7, -2)], 'fixe', lw=0.9, dash=True)
for a, b in [(-r3, 1), (r3, 1), (0, -2)]:
    disc(ax, *P(a, b), 1.2, 'resultat')
text(ax, P(-r3, 1)[0] - 1.5, P(-r3, 1)[1] + 4, r'$A$', 'resultat', 'm', weight='bold')
text(ax, P(r3, 1)[0] + 1.5, P(r3, 1)[1] + 4, r'$B$', 'resultat', 'm', weight='bold')
text(ax, P(0, -2)[0] + 4, P(0, -2)[1] - 4, r'$C$', 'resultat', 'm', weight='bold')
text(ax, 11, 62, r'en $A$ et $B$ :', 'varie', 's')
text(ax, 11, 57, 'elle traverse', 'varie', 's')
text(ax, 72, 9, r'en $C$ : elle touche', 'resultat', 's')
text(ax, 72, 4, 'tangente horizontale', 'fixe', 's')
save(fig, '70-018')
