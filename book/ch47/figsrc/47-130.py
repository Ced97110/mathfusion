import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 3, 14, 54, 40, 'sujet', fill=False, lw=1.2)
text(ax, 8, 50, r'$N$', 'sujet', 'l')
xs = [13, 25, 37, 49]
labs = [r'$1$', r'$r$', r'$r^{2}$', r'$r^{3}$']
for x, l in zip(xs, labs):
    disc(ax, x, 32, 4.2, 'sujet', label=l, size='m')
arrow(ax, (xs[1], 37), (xs[3], 37), 'varie', curve=-0.45, both=True)
text(ax, 31, 49, r'$g=s$', 'varie', 'm')
text(ax, 30, 20, r'$1$ et $r^{2}$ restent', 'fixe', 's')
box(ax, 63, 24, 22, 20, 'limite', fill=False, dash=True, lw=1.0)
text(ax, 74, 34, 'hors de N', 'limite', 's')
text(ax, 74, 18, "rien n'y arrive", 'resultat', 's')
save(fig, '47-130')
