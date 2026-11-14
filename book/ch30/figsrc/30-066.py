import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(72)
Y0, S = 36, 7
X = lambda d: 8 + d / 360 * 72
cot = lambda d: 1 / math.tan(math.radians(d))
line(ax, [(4, Y0), (84, Y0)], 'fixe')
for d in (0, 180, 360):
    line(ax, [(X(d), 8), (X(d), 62)], 'fixe', dash=True)
for lo in (15, 195):
    line(ax, [(X(lo + 150 * i / 60), Y0 + S * cot(lo + 150 * i / 60)) for i in range(61)], 'sujet', lw=1.4)
y = Y0 + S * cot(60)
line(ax, [(X(60), y), (X(240), y)], 'resultat', dash=True)
disc(ax, X(60), y, 1.3, 'sujet'); disc(ax, X(240), y, 1.3, 'varie')
text(ax, X(60), Y0 - 3.5, '60°', 'sujet', 's'); text(ax, X(240), Y0 - 3.5, '240°', 'varie', 's')
text(ax, 31, 50, 'même hauteur 0,577', 'resultat', 's')
arrow(ax, (X(60), 64), (X(240), 64), 'varie')
line(ax, [(X(60), y + 1.5), (X(60), 64)], 'varie', dash=True); line(ax, [(X(240), y + 1.5), (X(240), 64)], 'varie', dash=True)
text(ax, X(150), 68, r'$+\pi$ : un demi-tour', 'varie', 's')
save(fig, '30-066')
