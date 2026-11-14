import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, yb, sx, sy = 44, 24, 14, 7
ts = [-2 + 4 * i / 60 for i in range(61)]
line(ax, [(4, yb), (84, yb)], 'fixe', lw=0.7)
line(ax, [(cx + sx * t, yb + sy * (t * t + 1)) for t in ts], 'sujet', lw=1.2)
line(ax, [(cx + sx * t, yb + sy * (t * t - 1)) for t in ts], 'autre', lw=1.2)
disc(ax, cx - sx, yb, 1.4, 'autre')
disc(ax, cx + sx, yb, 1.4, 'autre')
text(ax, cx - sx, yb + 4, r'$-1$', 'autre', 's')
text(ax, cx + sx, yb + 4, r'$1$', 'autre', 's')
text(ax, 8, 60, r'$x^2+1$', 'sujet', 'm')
text(ax, 8, 46, r'$x^2-1$', 'autre', 'm')
text(ax, cx, 40, 'jamais 0', 'sujet', 's')
text(ax, cx, 10, 'deux racines', 'autre', 's')
save(fig, '54-187')
