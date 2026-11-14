import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
s = 6.0
lx, ly = 22.0, 40.0
rx, ry = 66.0, 40.0
text(ax, lx, 68, 'Cercle et parabole', 'sujet', 'm', weight='bold')
text(ax, rx, 68, 'Deux cercles', 'autre', 'm', weight='bold')
P = lambda x, y: (lx + s * x, ly + s * y)
disc(ax, *P(0, 0), 2 * s, 'sujet', fill=False, lw=1.3)
line(ax, [P(t / 20, (t / 20) ** 2 - 2) for t in range(-34, 35)], 'varie', lw=1.3)
box(ax, 3, 6, 38, 11, 'resultat', label=r'$y=x^2-2$ : $y$ donné', size='s')
text(ax, lx, 22, 'on peut remplacer', 'resultat', 's')
# two circles with different centres
disc(ax, rx - 5, ry - 1, 2 * s, 'sujet', fill=False, lw=1.3)
disc(ax, rx + 5, ry + 1, 2 * s, 'autre', fill=False, lw=1.3)
text(ax, rx - 11, ry - 1, r'$y^2$', 'sujet', 'm')
text(ax, rx + 11, ry + 1, r'$y^2$', 'autre', 'm')
box(ax, 47, 6, 38, 11, 'limite', label='aucun « y = »', size='s')
text(ax, rx, 22, 'on ne peut pas remplacer', 'limite', 's')
save(fig, '70-004')
