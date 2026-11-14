import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
s, ox, oy = 8.0, 28.0, 34.0
P = lambda x, y: (ox + s * x, oy + s * y)
r3 = 3 ** 0.5
arrow(ax, P(-2.6, 0), P(2.7, 0), 'fixe', lw=0.6)
arrow(ax, P(0, -2.5), P(0, 3.4), 'fixe', lw=0.6)
disc(ax, *P(0, 0), 2 * s, 'sujet', fill=False, lw=1.3)
line(ax, [P(t / 20, (t / 20) ** 2 - 2) for t in range(-46, 47)], 'varie', lw=1.3)
# x = 1 : the circle gives y = +-sqrt(3), the parabola gives y = -1 : no common height
line(ax, [P(1, -2.3), P(1, 2.6)], 'limite', lw=0.8, dash=True)
for h in (r3, -r3):
    disc(ax, *P(1, h), 1.0, 'sujet')
disc(ax, *P(1, -1), 1.0, 'varie')
# x = sqrt(3) : common height 1
line(ax, [P(r3, -2.3), P(r3, 2.6)], 'resultat', lw=0.8, dash=True)
disc(ax, *P(r3, 1), 1.3, 'resultat')
text(ax, 70, 62, r'$x=1$ : valeur $-2$', 'limite', 's')
text(ax, 70, 57, 'pas de hauteur commune', 'limite', 's')
text(ax, 70, 42, r'$x=\sqrt{3}$ : valeur 0', 'resultat', 's')
text(ax, 70, 37, 'hauteur commune : 1', 'resultat', 's')
save(fig, '70-016')
