import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(56)
cx, cy, R = 6, 6, 32
P = lambda r, d: (cx + r * math.cos(math.radians(d)), cy + r * math.sin(math.radians(d)))
t = np.radians(np.linspace(0, 90, 60))
line(ax, [(cx + R * math.cos(a), cy + R * math.sin(a)) for a in t], 'fixe')
line(ax, [(cx, cy), (cx + R + 3, cy)], 'fixe'); line(ax, [(cx, cy), (cx, cy + R + 3)], 'fixe')
arrow(ax, (cx, cy), P(R, 30), 'sujet', lw=1.3)
arrow(ax, (cx, cy), P(R, 60), 'resultat', lw=1.3)
for d, role in ((30, 'sujet'), (60, 'resultat')):
    a = np.radians(np.linspace(0, d, 30))
    line(ax, [P(12 if d == 30 else 17, math.degrees(x)) for x in a], role)
text(ax, *P(R + 5, 30), '30°', 'sujet', 's')
text(ax, *P(R + 5, 60), '60°', 'resultat', 's')
box(ax, 46, 40, 40, 9, 'sujet', label=r'cos 30° + $i$ sin 30°', size='s')
arrow(ax, (66, 40), (66, 34), 'varie')
text(ax, 70, 37, 'fois lui-même', 'varie', 's', ha='left')
box(ax, 46, 22, 40, 9, 'resultat', label='réelle : 0,75 − 0,25 = 0,5', size='s')
box(ax, 46, 11, 40, 9, 'resultat', label=r'imag. : 2×0,5×0,866 = 0,866', size='s')
text(ax, 66, 5, 'cos 60° et sin 60°', 'resultat', 's')
save(fig, '34-177')
