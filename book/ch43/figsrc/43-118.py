import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
x0, y0, d = 14, 12, 12
P = lambda m, n: (x0 + d * m, y0 + d * n)
arrow(ax, (x0 - 6, y0 - 6), (x0 + 4 * d + 10, y0 - 6), 'fixe', lw=0.8)
arrow(ax, (x0 - 6, y0 - 6), (x0 - 6, y0 + 4 * d + 8), 'fixe', lw=0.8)
text(ax, x0 + 4 * d + 14, y0 - 6, r'$m$', 'fixe', 'm')
text(ax, x0 - 10, y0 + 4 * d + 6, r'$n$', 'fixe', 'm')
path = []
for dd in range(4):
    cells = [(m, dd - m) for m in range(dd + 1)]
    path += cells if dd % 2 == 1 else cells[::-1]
path = [(1, 0) if False else c for c in path]
# d=0: (0,0); d=1: (1,0),(0,1); d=2: (0,2),(1,1),(2,0); d=3: (3,0),...
order = [(0, 0), (1, 0), (0, 1), (0, 2), (1, 1), (2, 0), (3, 0), (2, 1), (1, 2), (0, 3)]
line(ax, [P(*c) for c in order], 'sujet', lw=1.0)
for m in range(5):
    for n in range(5):
        if m + n > 3: disc(ax, *P(m, n), 1.3, 'fixe')
for k, c in enumerate(order):
    disc(ax, *P(*c), 3.6, 'encre')
    text(ax, *P(*c), str(k), 'varie', 's', weight='bold')
save(fig, '43-118')
