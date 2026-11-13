import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin
fig, ax = canvas(84)
c = (28, 52); per = 7.0; a = per / (2 * pi)  # 7 mm dessinés par tour : r proportionnel à l'angle
pts = [(c[0] + a * t * cos(t), c[1] + a * t * sin(t)) for t in [i * 8 * pi / 600 for i in range(601)]]
line(ax, pts, 'sujet', lw=1.2)
disc(ax, c[0], c[1], 1.0, 'fixe')
text(ax, c[0] - 6, c[1] + 4, 'axe', 'fixe', 's')
line(ax, [c, (c[0] + 4 * per + 3, c[1])], 'fixe', dash=True)
for n in range(1, 5):
    x = c[0] + n * per
    disc(ax, x, c[1], 0.9, 'varie')
    line(ax, [(x, c[1] - 1.2), (x, 17)], 'fixe', lw=0.4, dash=True)
f = numberline(ax, c[0], c[0] + 4 * per, 14, 0, 0.4, step=0.1, arrow_right=False, role='fixe')
text(ax, 13, 14, 'distance (mm)', 'encre', 's')
text(ax, 13, 6, 'tours', 'encre', 's')
for n in range(0, 5):
    text(ax, f(n * 0.1), 6, str(n), 'varie', 's')
text(ax, 74, 52, '+0,1 mm\npar tour', 'varie', 's')
arrow(ax, (c[0] + 7, c[1] + 10), (c[0] - 4, c[1] + 12.5), 'varie', curve=0.5)
save(fig, '40-001')
