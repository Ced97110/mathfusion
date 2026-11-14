import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(60)
Y0, S = 12, 9
X = lambda d: 8 + d / 90 * 72
tn = lambda d: math.tan(math.radians(d))
line(ax, [(4, Y0), (84, Y0)], 'fixe')
line(ax, [(X(45), 12), (X(45), 52)], 'varie', dash=True)
line(ax, [(X(72 * i / 60), Y0 + S * tn(72 * i / 60)) for i in range(61)], 'sujet', lw=1.4)
line(ax, [(X(18 + 72 * i / 60), Y0 + S / tn(18 + 72 * i / 60)) for i in range(61)], 'autre', lw=1.4)
y = Y0 + S * tn(30)
line(ax, [(X(30), y), (X(60), y)], 'resultat', dash=True)
disc(ax, X(30), y, 1.2, 'sujet'); disc(ax, X(60), y, 1.2, 'autre')
for d, r in ((30, 'sujet'), (45, 'varie'), (60, 'autre')):
    text(ax, X(d), 8, f'{d}°', r, 's')
text(ax, 28, 21.5, 'tan = 0,577', 'sujet', 's'); text(ax, 62, 21.5, 'cotan = 0,577', 'autre', 's')
text(ax, 71, 38, 'tan', 'sujet', 'm'); text(ax, 17, 38, 'cotan', 'autre', 'm')
text(ax, X(45), 56, r'miroir en $\pi/4$', 'varie', 's')
save(fig, '30-070')
