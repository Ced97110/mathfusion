import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(70)
cx, cy, S = 40, 32, 24
th = np.radians(np.linspace(0, 180, 500)); r = np.cos(3 * th)
line(ax, list(zip(cx + S * r * np.cos(th), cy + S * r * np.sin(th))), 'sujet', lw=1.3)
line(ax, [(cx - 30, cy), (cx + 36, cy)], 'fixe', lw=0.5)
P = lambda rr, d: (cx + S * rr * math.cos(math.radians(d)), cy + S * rr * math.sin(math.radians(d)))
disc(ax, *P(1, 0), 1.3, 'varie'); text(ax, P(1, 0)[0] + 3, cy + 3, '0° : r = 1', 'varie', 's', ha='left')
disc(ax, cx, cy, 1.3, 'fixe')
arrow(ax, (cx + 25 * 0.5, cy + 25 * 0.866), (cx + 3 * 0.5, cy + 3 * 0.866), 'fixe')
text(ax, cx + 14, cy + 29, '30° : r = 0', 'fixe', 's', ha='left')
p = P(-1, 60); disc(ax, *p, 1.3, 'varie'); text(ax, p[0], p[1] - 5, '60° : r = −1', 'varie', 's')
text(ax, 4, 62, r'$r = \cos 3\theta$', 'sujet', 'l', ha='left')
save(fig, '34-178')
