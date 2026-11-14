import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 24, 68, r'$6 = 2^1 \times 3$', 'encre', 'm')
hub = (24, 38); L = 18
sp = {'A': (24, 38 + L), 'B': (24 - L * math.cos(math.radians(30)), 38 - L / 2), 'C': (24 + L * math.cos(math.radians(30)), 38 - L / 2)}
for k, p in sp.items():
    d = (p[0] - hub[0], p[1] - hub[1]); n = math.hypot(*d); u = (d[0] / n, d[1] / n)
    line(ax, [(hub[0] + u[0] * 3.4, hub[1] + u[1] * 3.4), (p[0] - u[0] * 4, p[1] - u[1] * 4)], 'sujet', lw=2.4)
for k, p in sp.items():
    disc(ax, p[0], p[1], 4, 'sujet', label=r'$s_%s$' % k, size='s')
disc(ax, hub[0], hub[1], 3.4, 'sujet', label=r'$e$', size='s')
box(ax, 56, 31, 30, 14, 'fixe')
disc(ax, 63.5, 38, 3.4, 'fixe', label=r'$r$', size='s'); disc(ax, 78.5, 38, 3.4, 'fixe', label=r'$r^2$', size='s')
text(ax, 71, 26.5, 'ordre 3 : exclues', 'limite', 's')
text(ax, 44, 8, '3 traits = 3 sous-groupes de 2', 'sujet', 's')
save(fig, '50-085')
