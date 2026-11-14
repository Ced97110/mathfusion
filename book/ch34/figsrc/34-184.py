import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(56)
ox, oy, R = 4, 10, 32
P = lambda r, d: (ox + r * math.cos(math.radians(d)), oy + r * math.sin(math.radians(d)))
for k in range(3):
    pts = [(ox, oy)] + [P(R, d) for d in np.linspace(20 * k, 20 * k + 20, 15)]
    poly(ax, pts, 'sujet' if k != 1 else 'fixe')
    text(ax, *P(20, 20 * k + 10), '20°', 'sujet' if k != 1 else 'fixe', 's')
text(ax, *P(R + 5, 30), '60°', 'sujet', 's')
text(ax, 20, 4, 'cos 20° ≈ 0,9397', 'sujet', 's')
box(ax, 46, 32, 40, 14, 'autre', label='pentagone (72°)\n' + r'4$c^2$ + 2$c$ − 1 = 0', size='s')
text(ax, 66, 27.5, 'degré 2 : racines carrées', 'autre', 's')
box(ax, 46, 8, 40, 14, 'sujet', label='trisection (60° en 3)\n' + r'8$c^3$ − 6$c$ − 1 = 0', size='s')
text(ax, 66, 3.5, 'degré 3 : reste du degré 3', 'sujet', 's')
save(fig, '34-184')
