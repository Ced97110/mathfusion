import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(60)
labs = [r'$\alpha^{0}=1_S$', r'$\alpha^{1}=\alpha$', r'$\alpha^{2}=\alpha\circ\alpha$']
cx = [14, 44, 74]
for k, x in enumerate(cx):
    t = math.radians(90 * k)
    pts = [(x + 8 * (math.cos(t) * a - math.sin(t) * b), 30 + 8 * (math.sin(t) * a + math.cos(t) * b)) for a, b in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]
    poly(ax, pts, 'sujet')
    mx, my = pts[3]; disc(ax, mx * 0.82 + x * 0.18, my * 0.82 + 30 * 0.18, 1.8, 'varie')
    text(ax, x, 12, labs[k], 'sujet', 'm')
    text(ax, x, 48, f'{k} fois' if k != 1 else '1 fois', 'fixe', 's')
for a, b in [(24, 34), (54, 64)]:
    arrow(ax, (a, 30), (b, 30), 'varie'); text(ax, (a + b) / 2, 34, r'$\circ\,\alpha$', 'varie', 's')
save(fig, '44-079')
