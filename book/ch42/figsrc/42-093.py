import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
k, s = 14.0, 8.0; x0 = 44; y0 = 12
line(ax, [(4, y0), (84, y0)], 'fixe', lw=1.0)
xs = [i / 40 for i in range(-80, 81)]
line(ax, [(x0 + x * k, y0 + x * x * s) for x in xs], 'sujet', lw=1.4)
r = 2 ** 0.5
line(ax, [(4, y0 + 2 * s), (84, y0 + 2 * s)], 'varie', lw=0.9, dash=True)
text(ax, 80, y0 + 2 * s + 4, 'x² = 2', 'varie', 's')
for x in (-r, r):
    disc(ax, x0 + x * k, y0 + 2 * s, 1.8, 'resultat')
    line(ax, [(x0 + x * k, y0 + 2 * s), (x0 + x * k, y0)], 'resultat', lw=0.7, dash=True)
text(ax, x0 + r * k + 1, y0 - 4, '√2', 'resultat', 's'); text(ax, x0 - r * k - 1, y0 - 4, '−√2', 'resultat', 's')
text(ax, 44, 66, 'il existe x réel : x² = 2', 'resultat', 'm', weight='bold')
text(ax, 44, 58, 'au moins un : ici deux', 'fixe', 's')
save(fig, '42-093')
