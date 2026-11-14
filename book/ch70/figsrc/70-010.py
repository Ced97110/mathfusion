import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
s, ox, oy = 9.0, 30.0, 36.0
P = lambda x, y: (ox + s * x, oy + s * y)
r3 = 3 ** 0.5
arrow(ax, P(-2.6, 0), P(2.7, 0), 'fixe', lw=0.6)
arrow(ax, P(0, -2.6), P(0, 3.6), 'fixe', lw=0.6)
text(ax, P(2.7, 0)[0] + 2.5, oy - 1.5, r'$x$', 'fixe', 's')
disc(ax, *P(0, 0), 2 * s, 'sujet', fill=False, lw=1.3)
line(ax, [P(t / 20, (t / 20) ** 2 - 2) for t in range(-46, 47)], 'varie', lw=1.3)
pts = [('A', -r3, 1, (-1.0, 0.5)), ('B', r3, 1, (1.0, 0.5)), ('C', 0, -2, (0.55, -0.5))]
for name, a, b, (dx, dy) in pts:
    line(ax, [P(a, b), P(a, 0)], 'resultat', lw=0.8, dash=True)
    disc(ax, *P(a, b), 1.2, 'resultat')
    text(ax, P(a, b)[0] + dx * 3.2, P(a, b)[1] + dy * 5, name, 'resultat', 'm', weight='bold')
    ax.add_patch(Rectangle((P(a, 0)[0] - 1.1, oy - 1.1), 2.2, 2.2, ec=COL['resultat'], fc=COL['resultat'], zorder=4))
text(ax, P(-r3, 0)[0], oy - 4.5, r'$-\sqrt{3}$', 'resultat', 's')
text(ax, P(r3, 0)[0], oy - 4.5, r'$\sqrt{3}$', 'resultat', 's')
text(ax, P(0, 0)[0] - 3, oy - 4.5, '0', 'resultat', 's')
text(ax, 72, 62, r'cercle $f=0$', 'sujet', 's')
text(ax, 72, 54, r'parabole $g=0$', 'varie', 's')
text(ax, 72, 40, 'valeurs sur l\'axe', 'resultat', 's')
text(ax, 72, 33, r'$x^2(x^2-3)=0$', 'resultat', 's')
save(fig, '70-010')
