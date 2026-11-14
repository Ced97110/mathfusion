import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
s, ox, oy = 14.0, 12.0, 8.0
P = lambda x, y: (ox + s * x, oy + s * y)
arrow(ax, (8, oy), (80, oy), 'fixe', lw=0.6)
arrow(ax, (ox, 4.5), (ox, 53), 'fixe', lw=0.6)
text(ax, 82.5, oy, r'$x$', 'fixe', 's')
text(ax, 8.5, 53, r'$y$', 'fixe', 's')
text(ax, 8.5, 4.5, r'$O$', 'fixe', 's')
line(ax, [P(0.4 + 0.02 * i, 1 / (0.4 + 0.02 * i)) for i in range(0, 200)], 'sujet', lw=1.3)
r = math.sqrt(2) * s
line(ax, [(ox + r * math.cos(math.radians(a)), oy + r * math.sin(math.radians(a))) for a in range(3, 88, 3)], 'resultat', lw=0.7, dash=True)
for (a, b) in [(2, 0.5), (4, 0.25)]:
    line(ax, [(ox, oy), P(a, b)], 'fixe', lw=0.7, dash=True)
    disc(ax, *P(a, b), 1.2, 'fixe')
line(ax, [(ox, oy), P(1, 1)], 'resultat', lw=1.4)
disc(ax, *P(1, 1), 1.5, 'resultat')
text(ax, 44, 33, r'$P$ : $d^2=2$', 'resultat', 'm', weight='bold')
arrow(ax, (38, 31.5), (28, 23.5), 'resultat')
text(ax, 40, 22, 'd² = 4,25', 'fixe', 's')
text(ax, 68, 18, 'd² = 16,0625', 'fixe', 's')
text(ax, 62, 47, r'courbe $xy=1$', 'sujet', 's')
save(fig, '70-085')
