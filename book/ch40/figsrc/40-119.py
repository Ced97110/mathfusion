import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(62)
a = 0.35
x0, gy, u = 6, 16, 34
X = lambda t: x0 + u * a * (t - math.sin(t))
Y = lambda t: gy + u * a * (1 - math.cos(t))
t1 = np.linspace(0, math.pi, 200)
t2 = np.linspace(math.pi, 2 * math.pi, 200)
line(ax, [(X(t), Y(t)) for t in t1], 'sujet', lw=1.6)
line(ax, [(X(t), Y(t)) for t in t2], 'fixe', lw=1.4)
line(ax, [(x0 - 2, gy), (X(2 * math.pi) + 3, gy)], 'fixe', lw=0.8)
hy = Y(math.pi / 2)
line(ax, [(x0, hy), (X(2 * math.pi), hy)], 'fixe', lw=0.6, dash=True)
text(ax, 84, hy + 3, 'y = 0,35', 'fixe', 's', ha='right')
disc(ax, X(math.pi / 2), hy, 1.3, 'resultat')
disc(ax, X(3 * math.pi / 2), hy, 1.3, 'limite')
text(ax, 20, hy + 11, 'formule : 0,20 ✓', 'resultat', 's')
text(ax, 72, hy + 12.5, 'x = 2,00\nformule : 0,20 ✗', 'limite', 's')
brace(ax, x0, X(math.pi), gy - 1.5, 'sujet', label='demi-arche : valable', depth=1.6)
brace(ax, X(math.pi), X(2 * math.pi), gy - 1.5, 'fixe', label='autre moitié', depth=1.6)
text(ax, 44, 57, r'$x=at-\sqrt{2ay-y^2}$', 'encre', 'm')
save(fig, '40-119')
