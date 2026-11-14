import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(104)
cx, cy, R = 28, 80, 18
P = lambda r, d: (cx + r * math.cos(math.radians(d)), cy + r * math.sin(math.radians(d)))
line(ax, [P(R, d) for d in np.linspace(0, 360, 200)], 'fixe')
line(ax, [(cx - R - 2, cy), (cx + R + 2, cy)], 'fixe', lw=0.5)
xs = P(R, 144)[0]
line(ax, [(xs, P(R, 216)[1]), (xs, P(R, 144)[1])], 'resultat', dash=True, lw=1.1)
for d, role in ((72, 'sujet'), (144, 'autre'), (216, 'varie')):
    arrow(ax, (cx, cy), P(R, d), role, lw=1.2)
text(ax, *P(R + 4.5, 72), '72°', 'sujet', 's')
text(ax, P(R, 144)[0] - 1.5, P(R, 144)[1] + 3, '144°', 'autre', 's', ha='right')
text(ax, P(R, 216)[0] - 1.5, P(R, 216)[1] - 3, '216°', 'varie', 's', ha='right')
text(ax, xs + 6, cy - R - 5, '≈ −0,809', 'resultat', 's')
box(ax, 54, 88, 32, 8, 'sujet', label='72° = 360° ÷ 5', size='s')
box(ax, 54, 77, 32, 8, 'varie', label='3 × 72° = 216°', size='s')
box(ax, 54, 66, 32, 8, 'autre', label='2 × 72° = 144°', size='s')
text(ax, 70, 59, '216° + 144° = 360°', 'resultat', 's')
box(ax, 2, 38, 84, 9, 'resultat', label=r'$\cos 3\theta=\cos 2\theta$ pour $\theta=72°$', size='s')
arrow(ax, (44, 37), (44, 28), 'varie'); text(ax, 48, 32.5, r'$c=\cos 72°$', 'varie', 's', ha='left')
box(ax, 2, 19, 84, 9, 'sujet', label=r'$4c^3-3c=2c^2-1$', size='s')
arrow(ax, (44, 18), (44, 12), 'varie'); text(ax, 48, 15, r'on retire le facteur $c-1$', 'varie', 's', ha='left')
box(ax, 2, 2, 84, 9, 'resultat', label=r'$4c^2+2c-1=0$', size='s')
save(fig, '34-183')
