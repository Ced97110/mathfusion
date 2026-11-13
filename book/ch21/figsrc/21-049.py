import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, u = 12, 8, 14.0   # origine, mm par unité
X = lambda v: ox + v * u
Y = lambda v: oy + (v - 1) * 0 + v * 9.5
arrow(ax, (ox - 2, Y(0)), (X(3.6), Y(0)), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 2), (ox, Y(6.2)), 'fixe', lw=0.8)
for v in range(4):
    line(ax, [(X(v), Y(0) - 1), (X(v), Y(0) + 1)], 'fixe')
    text(ax, X(v), Y(0) - 3.5, str(v), 'fixe', 's')
g = 0.22
line(ax, [(X(0), Y(2)), (X(2 - g), Y(4 - g))], 'sujet', lw=1.3)
line(ax, [(X(2 + g), Y(4 + g)), (X(3.4), Y(5.4))], 'sujet', lw=1.3)
for (a, b, dx, dy) in [(0, 2, 6, 3.5), (1, 3, 7, -3.5), (3, 5, 7, -3.5)]:
    disc(ax, X(a), Y(b), 1.3, 'sujet')
    text(ax, X(a) + dx, Y(b) + dy, f'({a}, {b})', 'sujet', 's')
disc(ax, X(2), Y(4), 1.5, 'varie', fill=False)
text(ax, X(2) - 13, Y(4) + 6, 'point manquant', 'varie', 's')
text(ax, X(3.4) + 1, Y(5.4) + 4, r'$y = x + 2$', 'sujet', 'm', ha='right')
save(fig, '21-049')
