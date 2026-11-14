import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
gx = lambda x: 20 + x * 14; gy = lambda y: 30 + y * 4
line(ax, [(gx(-0.5), gy(0)), (gx(3.5), gy(8))], 'sujet', lw=1.3)
line(ax, [(gx(-0.5), gy(-6)), (gx(3.5), gy(2))], 'autre', lw=1.3)
for x in (0, 3):
    arrow(ax, (gx(x), gy(2 * x - 5)), (gx(x), gy(2 * x + 1)), 'varie', lw=1.2, both=True)
    text(ax, gx(x) + 2, (gy(2 * x - 5) + gy(2 * x + 1)) / 2 + (6 if x == 0 else 0), 'écart 6', 'varie', 's', ha='left')
text(ax, 32, gy(6), r'$y=2x+1$', 'sujet', 's')
text(ax, 66, gy(-2), r'$y=2x-5$', 'autre', 's')
text(ax, 44, 67, 'même pente 2 : l’écart ne change pas', 'encre', 's')
save(fig, '19-108')
