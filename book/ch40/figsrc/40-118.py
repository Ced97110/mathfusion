import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(84)
x0, gy, u = 5, 56, 6.2
X = lambda t: x0 + u * (t - math.sin(t))
Y = lambda t: gy + u * (1 - math.cos(t))
ts = np.linspace(0, 4 * math.pi, 500)
line(ax, [(X(t), Y(t)) for t in ts], 'sujet', lw=1.4)
line(ax, [(x0 - 2, gy), (X(4 * math.pi) + 2, gy)], 'fixe', lw=0.8)
for k, s in ((0, 't = 0'), (1, 't = 2π'), (2, 't = 4π')):
    px = X(2 * math.pi * k)
    disc(ax, px, gy, 1.2, 'varie')
    text(ax, min(max(px, 11), 77), gy - 4.5, s, 'varie', 's')
text(ax, 44, 79, 'pointe au contact : le point est immobile', 'encre', 's')
text(ax, 44, 43, 'rapport montée ÷ avance', 'encre', 'm')
box(ax, 4, 24, 30, 10, 'fixe', label='t = 0,2 → 15', size='m')
box(ax, 54, 24, 30, 10, 'sujet', label='t = 0,1 → 30', size='m')
arrow(ax, (34, 29), (54, 29), 'varie')
text(ax, 44, 33.5, 't ÷ 2', 'varie', 's')
text(ax, 44, 24.5, 'rapport × 2', 'varie', 's')
save(fig, '40-118')
