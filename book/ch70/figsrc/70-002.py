import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
# left panel: two lines (neighbour), right panel: the garden
s = 7.0
lx, ly = 22.0, 30.0
rx, ry = 66.0, 30.0
text(ax, lx, 64, 'Deux droites', 'fixe', 'm', weight='bold')
text(ax, rx, 64, 'Le jardin', 'sujet', 'm', weight='bold')
# left: two straight lines crossing once
box(ax, 2, 6, 40, 52, 'fixe', fill=False, lw=0.6, dash=True)
line(ax, [(8, 14), (36, 46)], 'fixe', lw=1.4)
line(ax, [(8, 44), (36, 20)], 'fixe', lw=1.4)
disc(ax, 21.2, 30.8, 1.1, 'resultat')
text(ax, lx, 10, 'linéaire', 'fixe', 'm')
text(ax, lx, 54, r'$x$ et $y$ seuls', 'fixe', 's')
# right: circle + parabola
box(ax, 46, 6, 40, 52, 'sujet', fill=False, lw=0.6, dash=True)
P = lambda x, y: (rx + s * x, ry + s * y)
disc(ax, *P(0, 0), 2 * s, 'sujet', fill=False, lw=1.3)
line(ax, [P(t / 20, (t / 20) ** 2 - 2) for t in range(-34, 35)], 'varie', lw=1.3)
for (a, b) in [(-3 ** 0.5, 1), (3 ** 0.5, 1), (0, -2)]:
    disc(ax, *P(a, b), 1.1, 'resultat')
text(ax, rx, 10, 'non linéaire', 'sujet', 'm')
text(ax, rx, 54, r'$x^2$ et $y^2$', 'sujet', 's')
save(fig, '70-002')
