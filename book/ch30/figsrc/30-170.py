import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
x0, y0, sy, L = 14, 40, 18 / 13, 58
line(ax, [(x0, y0), (x0 + L + 4, y0)], 'fixe')
line(ax, [(x0, 20), (x0, 60)], 'fixe')
for s, role in [(1, 'sujet'), (-1, 'autre')]:
    line(ax, [(x0 + L * i / 100, y0 + s * 13 * sy * math.sin(3 * math.pi * (2 / 3) * i / 100)) for i in range(101)], role, lw=1.6)
disc(ax, x0, y0, 1.5, 'resultat')
text(ax, 8, y0, '0', 'fixe', 's')
text(ax, 28.5, 71.5, "monte d'abord", 'sujet', 'm')
text(ax, 28.5, 66, r'$13\,\sin(3\pi t)$', 'sujet', 'm')
text(ax, 28.5, 12, r'$-13\,\sin(3\pi t)$', 'autre', 'm')
text(ax, 28.5, 6.5, "descend d'abord", 'autre', 'm')
text(ax, 80, y0 + 3, 't', 'fixe', 's')
save(fig, '30-170')
