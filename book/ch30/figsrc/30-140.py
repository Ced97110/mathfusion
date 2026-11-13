import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(52)
x0, x1 = 12, 80
yD = 24
arrow(ax, (x0, 8), (x1 + 4, 8), 'fixe', lw=0.7)
line(ax, [(x0, 8), (x0, 46)], 'fixe', lw=0.7)
xs = np.linspace(x0, x1, 200)
line(ax, list(zip(xs, yD + 10 * np.sin((xs - x0) / (x1 - x0) * 4 * np.pi))), 'fixe', dash=True, lw=1.0)
line(ax, [(x0, yD), (x1, yD)], 'sujet', lw=1.6)
for xv in (x0 + (x1 - x0) / 8, x0 + 5 * (x1 - x0) / 8):
    arrow(ax, (xv, yD + 9), (xv, yD + 1.5), 'varie')
    arrow(ax, (xv + (x1 - x0) / 4, yD - 9), (xv + (x1 - x0) / 4, yD - 1.5), 'varie')
text(ax, x0 - 2.5, yD, r'$D$', 'sujet', 'm')
text(ax, 46, 48, r'$A=0:\ y=D$', 'sujet', 'l')
text(ax, 46, 3, 'les hauteurs sont écrasées sur D', 'varie', 's')
text(ax, 34, 38, r'$A\neq 0$ : oscille', 'fixe', 's')
save(fig, '30-140')
