import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, x1, y = 6, 78, 20
f = numberline(ax, x0, x1, y, -0.75, 0.25, step=0.25, arrow_right=False)
p1 = -0.5714; p2 = p1 + 0.0714
arrow(ax, (f(0), 29), (f(p1), 29), 'varie')
text(ax, (f(0) + f(p1)) / 2, 33, r'$\cos 175°\cos 55°$ = −0,5714', 'varie', 's')
arrow(ax, (f(p1), 42), (f(p2), 42), 'autre')
text(ax, 44, 46.5, r'+ $\sin 175°\sin 55°$ = 0,0714', 'autre', 's')
line(ax, [(f(p1), 29), (f(p1), 42)], 'fixe', lw=0.6, dash=True)
line(ax, [(f(p2), 20), (f(p2), 42)], 'resultat', lw=0.6, dash=True)
disc(ax, f(p2), y, 1.4, 'resultat')
text(ax, f(p2), 11, r'−0,5 = $\cos 120°$', 'resultat', 'm')
text(ax, 44, 3, r'175° − 55° = 120°', 'encre', 's')
save(fig, '34-119')
