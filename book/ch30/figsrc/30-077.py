import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(84)
Y0, S = 42, 14
X = lambda x: 8 + x / (2 * math.pi) * 72
line(ax, [(4, Y0), (84, Y0)], 'fixe')
for x in (math.pi / 2, 3 * math.pi / 2):
    line(ax, [(X(x), 4), (X(x), 80)], 'fixe', dash=True)
line(ax, [(X(2 * math.pi * i / 200), Y0 + S * math.cos(2 * math.pi * i / 200)) for i in range(201)], 'autre', lw=1.3)
a = math.acos(1 / 2.7)
for lo, hi in ((0, a), (math.pi - a, math.pi + a), (2 * math.pi - a, 2 * math.pi)):
    line(ax, [(X(lo + (hi - lo) * i / 60), Y0 + S / math.cos(lo + (hi - lo) * i / 60)) for i in range(61)], 'sujet', lw=1.4)
for x, y in ((0, 1), (math.pi, -1), (2 * math.pi, 1)):
    disc(ax, X(x), Y0 + S * y, 1.3, 'resultat')
text(ax, X(math.pi / 2), 2, r'$\pi/2$', 'encre', 's'); text(ax, X(3 * math.pi / 2), 2, r'$3\pi/2$', 'encre', 's')
for y, r, s in ((26, 'autre', 'cosinus'), (19, 'sujet', 'sécante')):
    line(ax, [(66, y), (71, y)], r, lw=1.4); text(ax, 73, y, s, r, 's', ha='left')
disc(ax, 68.5, 12, 1.3, 'resultat'); text(ax, 73, 12, 'cos = sec', 'resultat', 's', ha='left')
line(ax, [(66, 5), (71, 5)], 'fixe', dash=True); text(ax, 73, 5, 'asymptote', 'fixe', 's', ha='left')
save(fig, '30-077')
