import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(52)
cx, cy, R = 6, 5, 38
P = lambda r, d: (cx + r * math.cos(math.radians(d)), cy + r * math.sin(math.radians(d)))
line(ax, [P(R, d) for d in np.linspace(0, 90, 60)], 'fixe')
line(ax, [(cx, cy), (cx + R + 2, cy)], 'fixe', lw=0.5); line(ax, [(cx, cy), (cx, cy + R + 2)], 'fixe', lw=0.5)
arrow(ax, (cx, cy), P(R, 20), 'sujet', lw=1.3)
arrow(ax, (cx, cy), P(R, 80), 'autre', lw=1.3)
line(ax, [P(20, d) for d in np.linspace(20, 80, 40)], 'varie', lw=1.2)
text(ax, *P(26, 50), '60°', 'varie', 's')
text(ax, P(R, 20)[0] - 1, P(R, 20)[1] + 3, '20°', 'sujet', 's')
text(ax, P(R, 80)[0] + 5, P(R, 80)[1] - 1, '80°', 'autre', 's')
box(ax, 48, 38, 38, 8, 'autre', label='(cos 80°, sin 80°)', size='s')
box(ax, 48, 27, 38, 8, 'sujet', label='(cos 20°, sin 20°)', size='s')
box(ax, 48, 14, 38, 8, 'varie', label='0,1632 + 0,3368', size='s')
box(ax, 48, 2, 38, 8, 'resultat', label='0,5 = cos 60°', size='s')
arrow(ax, (67, 27), (67, 22.8), 'varie'); arrow(ax, (67, 14), (67, 10.8), 'varie')
save(fig, '34-180')
