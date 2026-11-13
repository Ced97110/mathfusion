import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
gx = lambda x: 36 + x * 12; gy = lambda y: 34 + y * 4
line(ax, [(gx(0), gy(-7)), (gx(0), gy(9))])
line(ax, [(gx(-0.5), gy(0)), (gx(3), gy(7))], 'sujet', lw=1.3)
line(ax, [(gx(-0.5), gy(-6)), (gx(3), gy(1))], 'autre', lw=1.3)
disc(ax, gx(0), gy(1), 1.1, 'sujet'); disc(ax, gx(0), gy(-5), 1.1, 'autre')
arrow(ax, (gx(0) - 5, gy(1)), (gx(0) - 5, gy(-5)), 'varie', lw=1.3)
text(ax, gx(0) - 7, (gy(1) + gy(-5)) / 2, 'décalage 6', 'varie', 's', ha='right')
text(ax, gx(0) + 2.5, gy(1) + 3, r'$b=1$', 'sujet', 's', ha='left')
text(ax, gx(0) + 2.5, gy(-5) - 3.5, r'$b=-5$', 'autre', 's', ha='left')
text(ax, 62, gy(8.5), r'$y=2x+1$', 'sujet', 's'); text(ax, 70, gy(-1.5), r'$y=2x-5$', 'autre', 's')
text(ax, 44, 75, 'même pente, autre hauteur de départ', 'encre', 's')
save(fig, '19-111')
