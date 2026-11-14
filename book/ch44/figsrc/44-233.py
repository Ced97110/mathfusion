import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(60)
o, u = (18, 14), 14
cubes(ax, [(0, 0, 0)], o, u, 'sujet')
P = lambda a, b: iso(a, b, 1, o, u)
poly(ax, [P(0, 0), P(1, 0), P(1, 1), P(0, 1)], 'varie')
text(ax, 18, 52, 'dessus', 'varie', 's'); arrow(ax, (18, 49.5), (18, 44), 'varie')
for i in range(6):
    for j in range(4):
        box(ax, 42 + i * 7, 22 + j * 7, 6, 6, 'varie' if i == 0 else 'sujet', r=0.6, lw=0.6)
brace(ax, 42, 83.5, 52, 'varie', label=None, down=False, depth=1.6)
text(ax, 62.5, 57.5, '6 faces au dessus', 'varie', 's')
text(ax, 62.5, 17, '4 tours par face', 'sujet', 's')
box(ax, 8, 3, 72, 9, 'resultat', label=r'$6 \times 4 = 24 = 4!$ : le groupe $S_4$', size='m')
save(fig, '44-233')
