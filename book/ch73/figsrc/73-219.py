import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(66)
cx, cy, r = 28, 32, 26
disc(ax, cx, cy, r, 'fixe', fill=False)
line(ax, [(2, cy), (54, cy)], 'fixe', lw=0.6); line(ax, [(cx, 4), (cx, 60)], 'fixe', lw=0.6)
px, py = cx + r * 0.6, cy + r * 0.8
poly(ax, [(cx, cy), (px, cy), (px, py)], 'sujet')
disc(ax, px, py, 1.3, 'sujet')
t = np.linspace(0, np.arctan2(4, 3), 20)
line(ax, [(cx + 7 * np.cos(a), cy + 7 * np.sin(a)) for a in t], 'varie')
text(ax, cx + 11, cy + 4.6, r'$\theta$', 'varie', 's')
text(ax, (cx + px) / 2, cy - 3.5, r'$\cos\theta=3/5$', 'encre', 's')
text(ax, px + 10.5, (cy + py) / 2, r'$\sin\theta=4/5$', 'encre', 's', ha='left')
text(ax, (cx + px) / 2 - 3, (cy + py) / 2 + 2, '1', 'sujet', 's')
text(ax, px + 2, py + 7.5, r'$(3/5,\ 4/5)$', 'sujet', 's', ha='left')
text(ax, 58, 22, r'$\theta\approx 53{,}13^\circ$', 'varie', 'm')
save(fig, '73-219')
