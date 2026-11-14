import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
px = [3, 32, 61]
for x, r in zip(px, ['sujet', 'autre', 'autre']):
    box(ax, x, 4, 26, 68, r, fill=False)
text(ax, 16, 66, 'Klein', 'sujet', 'm', weight='bold')
text(ax, 45, 66, r'$\mathbb{Z}/4\mathbb{Z}$', 'autre', 'm', weight='bold')
text(ax, 74, 66, r'$S_3$', 'autre', 'm', weight='bold')
for (x, y), l in zip([(10, 52), (22, 52), (10, 40), (22, 40)], ['1', r'$\sigma$', r'$\tau$', r'$\sigma\tau$']):
    disc(ax, x, y, 4.6, 'sujet', label=l, size='s')
for (x, y), l in zip([(39, 52), (51, 52), (39, 40), (51, 40)], ['0', '1', '2', '3']):
    disc(ax, x, y, 4.6, 'autre', label=l, size='s')
for (x, y), l in zip([(66, 52), (74, 52), (82, 52), (66, 40), (74, 40), (82, 40)],
                     ['1', r'$\sigma$', r'$\sigma^2$', r'$\tau$', r'$\sigma\tau$', r'$\sigma^2\tau$']):
    disc(ax, x, y, 3.8, 'autre', label=l, size='s')
text(ax, 16, 26, r'$\sigma^2=\tau^2=1$', 'sujet', 's')
text(ax, 16, 17, r'$\sigma\tau=\tau\sigma$', 'sujet', 's')
text(ax, 45, 26, r'$1+1=2\neq0$', 'autre', 's')
text(ax, 74, 26, r'$\tau\sigma\neq\sigma\tau$', 'autre', 's')
save(fig, '63-055')
