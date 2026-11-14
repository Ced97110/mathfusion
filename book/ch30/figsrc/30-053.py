import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
X = lambda x: 6 + (x + 1.6) * 12
Y = lambda v: 32 + 8 * v
a = math.atan(3)
for k in (0, 1):
    line(ax, [(X(k * math.pi - a + i * 2 * a / 60), Y(math.tan(k * math.pi - a + i * 2 * a / 60))) for i in range(61)], 'sujet', lw=1.3)
line(ax, [(X(-1.6), 32), (X(4.8), 32)], 'fixe', lw=0.6)
for x in (-math.pi / 2, math.pi / 2, 3 * math.pi / 2):
    line(ax, [(X(x), 6), (X(x), 58)], 'fixe', dash=True)
x1, x2 = 0.5, 0.5 + math.pi; yv = Y(0.5463)
line(ax, [(X(x1), yv), (X(x2), yv)], 'resultat', dash=True)
disc(ax, X(x1), yv, 1.4, 'varie'); disc(ax, X(x2), yv, 1.4, 'varie')
for x in (x1, x2): line(ax, [(X(x), yv), (X(x), 32)], 'varie', dash=True)
text(ax, X(x1) - 2, yv + 5, '0,5', 'varie', 's', ha='right'); text(ax, X(x2) - 2, yv + 5, '3,6416', 'varie', 's', ha='right')
text(ax, 50, yv + 3.5, 'tan = 0,5463', 'resultat', 's')
brace(ax, X(x1), X(x2), 28, 'varie', label='π', size='l')
save(fig, '30-053')
