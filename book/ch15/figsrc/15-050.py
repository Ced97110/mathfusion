import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s, g = 4.5, 0.7
xa = (88 - (13 * s + 12 * g + 2)) / 2
pa = [xa + i * (s + g) + (2 if i >= 8 else 0) for i in range(13)]
for x in pa: box(ax, x, 44, s, s, 'varie', lw=0.6, r=0.4)
brace(ax, pa[0], pa[12] + s, 49.1, 'resultat', r'même $x$ : $x(8 + 5)$', down=False)
brace(ax, pa[0], pa[7] + s, 43.4, 'fixe', r'$8x$')
brace(ax, pa[8], pa[12] + s, 43.4, 'fixe', r'$5x$')
xb = (88 - (5 * s + 4 * g + 2)) / 2
pb = [xb + i * (s + g) + (2 if i >= 3 else 0) for i in range(5)]
for i, x in enumerate(pb): box(ax, x, 18, s, s, 'varie' if i < 3 else 'autre', lw=0.6, r=0.4)
brace(ax, pb[0], pb[2] + s, 17.4, 'varie', r'$3x$')
brace(ax, pb[3], pb[4] + s, 17.4, 'autre', r'$2y$')
text(ax, 44, 5, 'pas de facteur commun', 'limite', 'm')
save(fig, '15-050')
