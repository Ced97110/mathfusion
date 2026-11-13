import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
X0, X1, YM, A = 8, 76, 30, 13
fx = lambda d: X0 + (X1 - X0) * d / 720
line(ax, [(4, YM), (80, YM)], 'fixe')
line(ax, [(fx(d), YM + A * math.sin(math.radians(d))) for d in range(0, 361, 6)], 'sujet', lw=1.4)
line(ax, [(fx(d), YM + A * math.sin(math.radians(d))) for d in range(360, 721, 6)], 'autre', lw=1.4)
for d in (0, 360, 720):
    disc(ax, fx(d), YM, 1.5, 'varie')
    text(ax, fx(d), 12, f'{d}°', 'fixe', 's')
brace(ax, fx(0), fx(360), 47, 'sujet', label='360°', down=False)
brace(ax, fx(360), fx(720), 47, 'autre', label='360°', down=False)
text(ax, 44, 5, 'le même dessin se répète', 'encre', 'm')
save(fig, '32-014')
