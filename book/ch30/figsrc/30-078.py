import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(70)
Y0, S = 34, 14
X = lambda d: 10 + d / 180 * 70
c = lambda d: math.cos(math.radians(d))
line(ax, [(6, Y0), (84, Y0)], 'fixe')
line(ax, [(X(90), 4), (X(90), 66)], 'fixe', dash=True)
line(ax, [(X(180 * i / 100), Y0 + S * c(180 * i / 100)) for i in range(101)], 'autre', lw=1.3)
a = math.degrees(math.acos(1 / 2.2))
for lo, hi in ((0, a), (180 - a, 180)):
    line(ax, [(X(lo + (hi - lo) * i / 60), Y0 + S / c(lo + (hi - lo) * i / 60)) for i in range(61)], 'sujet', lw=1.4)
y1, y2 = Y0 + S * 0.5, Y0 + S * 2
line(ax, [(X(60), y1), (X(60), y2)], 'fixe', dash=True)
arrow(ax, (X(60), y1 + 1.5), (X(60), y2 - 1.5), 'varie')
disc(ax, X(60), y1, 1.2, 'autre'); disc(ax, X(60), y2, 1.2, 'sujet')
text(ax, X(60) - 6, 37.5, '0,5', 'autre', 's'); text(ax, 38, 68, '1 ÷ 0,5 = 2', 'varie', 's')
text(ax, 30, 14, 'cos = 0 : pas de point', 'fixe', 's'); text(ax, X(60), 30.5, '60°', 'encre', 's')
text(ax, 66, 27.5, 'cosinus', 'autre', 'm'); text(ax, 20, 66, 'sécante', 'sujet', 'm')
save(fig, '30-078')
