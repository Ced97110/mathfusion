import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(66)
a = 0.35
x0, gy, u = 6, 14, 34
X = lambda t: x0 + u * a * (t - math.sin(t))
Y = lambda t: gy + u * a * (1 - math.cos(t))
ts = np.linspace(0, 2 * math.pi, 300)
line(ax, [(X(t), Y(t)) for t in ts], 'sujet', lw=1.4)
line(ax, [(x0 - 2, gy), (X(2 * math.pi) + 3, gy)], 'fixe', lw=0.8)
labels = [(math.pi / 2, 't = π/2\n(0,20 ; 0,35)', 'left', 4),
          (math.pi, 't = π\n(1,10 ; 0,70)', 'center', None),
          (2 * math.pi, 't = 2π\n(2,20 ; 0)', 'right', 84)]
for t, s, ha, lx in labels:
    px, py = X(t), Y(t)
    disc(ax, px, py, 1.2, 'varie')
    xx = px if lx is None else lx
    line(ax, [(px, py + 1.6), (px, 49)], 'fixe', lw=0.5, dash=True)
    text(ax, xx, 54, s, 'varie', 's', ha=ha)
brace(ax, x0, X(2 * math.pi), gy - 1.5, 'fixe', label='un tour de roue : 2πa ≈ 2,20 m', depth=1.6)
text(ax, 44, 4, 'roue de rayon a = 0,35 m', 'encre', 's')
save(fig, '40-116')
