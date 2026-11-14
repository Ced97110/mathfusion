import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(86)
f = lambda x: x ** 5 - 6 * x ** 3 - 27 * x - 3
sx, sy, x0, y0 = 10.9, 0.35, 44, 42
X = np.linspace(-3.3, 3.3, 400)
line(ax, [(x0 + sx * x, y0 + sy * f(x)) for x in X], 'sujet', lw=1.1)
arrow(ax, (3, y0), (85, y0), 'fixe', lw=0.7)
line(ax, [(x0, 7), (x0, 80)], 'fixe', lw=0.5)
roots = [-2.9859, -0.1108, 3.0137]
assert all(abs(f(r)) < 0.01 for r in roots)
for r, lab, dx in zip(roots, ('$r_1$', '$r_2$', '$r_3$'), (3, -3.5, 3)):
    disc(ax, x0 + sx * r, y0, 1.4, 'varie')
    text(ax, x0 + sx * r + dx, y0 - 4, lab, 'varie', 'm')
for t, dy in ((-2.177, 5), (2.177, -5)):
    px, py = x0 + sx * t, y0 + sy * f(t)
    line(ax, [(px, y0), (px, py)], 'fixe', lw=0.5, dash=True)
    disc(ax, px, py, 1.1, 'fixe')
    text(ax, px + (7 if t < 0 else -7), py + dy, f'{f(t):.1f}'.replace('.', ',').replace('-', '−'), 'fixe', 's')
text(ax, 44, 84, r'changements de sens : $x\approx\pm2{,}18$', 'fixe', 's')
save(fig, '64-173')
