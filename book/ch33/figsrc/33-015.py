import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(58)
k = 70 / 180; y0, amp = 28, 16
X = lambda d: 8 + (d + 90) * k
Y = lambda d: y0 + amp * math.sin(math.radians(d))
ax.add_patch(Rectangle((X(-90), y0 - amp - 3), 180 * k, 2 * amp + 6, fc=FILL['sujet'], ec=COL['sujet'], lw=0.6, zorder=1))
line(ax, [(X(-90), y0), (X(90), y0)], 'fixe', lw=0.6)
d = np.linspace(-90, 90, 200)
ax.plot(X(d), y0 + amp * np.sin(np.radians(d)), color=COL['encre'], lw=1.1, zorder=3)
for a, lab in ((-90, '−1'), (-30, '−0,5'), (0, '0'), (30, '0,5'), (90, '1')):
    disc(ax, X(a), Y(a), 1.2, 'varie')
    line(ax, [(X(a), Y(a) - 1.4), (X(a), 11)], 'fixe', lw=0.5, dash=True)
    text(ax, X(a), 7.5, f'{a}°'.replace('-', '−'), 'sujet', 's')
    if a == -90: text(ax, X(a) + 6, Y(a) + 2, lab, 'varie', 's')
    elif a == 90: text(ax, X(a) - 3.5, Y(a) + 3, lab, 'varie', 's')
    else: text(ax, X(a) - 5.5, Y(a) + 2.5, lab, 'varie', 's')
text(ax, 44, 53, 'la hauteur monte toujours', 'varie')
save(fig, '33-015')
