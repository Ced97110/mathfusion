import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, R, a): return (c[0] + R * math.cos(math.radians(a)), c[1] + R * math.sin(math.radians(a)))
def ring(ax, c, R, role='fixe', lw=0.8): ax.add_patch(Circle(c, R, fill=False, ec=COL[role], lw=lw, zorder=1))
def dot(ax, c, R, a, role, r=1.4):
    p = P(c, R, a); disc(ax, p[0], p[1], r, role); return p
def lab(ax, c, R, a, s, role='encre', size='s', d=5, ha='center'):
    p = P(c, R + d, a); text(ax, p[0], p[1], s, role, size, ha=ha)
def arcline(ax, c, R, a0, a1, role, n=24): line(ax, [P(c, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=1.0)
EM, SP = 0.636, 0.318
def row(ax, x0, y, seq, role, size=9.0, sep=6):
    text(ax, x0, y, (' ' * sep).join(str(v) for v in seq), role, size, ha='left')
    pitch = (EM + sep * SP) * size * 25.4 / 72; dw = EM * size * 25.4 / 72
    return [x0 + dw / 2 + i * pitch for i in range(len(seq))]

a = [1, 2, 3, 4, 5, 6, 7, 8]; b = [3, 6, 5, 4, 8, 2, 7, 1]
fig, ax = canvas(62)
xs = row(ax, 20, 52, a, 'autre'); row(ax, 20, 14, b, 'sujet')
for x, v in zip(xs, b):
    box(ax, x - 3.6, 47, 7.2, 10, 'autre'); box(ax, x - 3.6, 9, 7.2, 10, 'sujet')
    arrow(ax, (x, 46), (x, 20), 'varie')
text(ax, 9, 52, 'nombre', 'autre', 's'); text(ax, 9, 14, 'image', 'sujet', 's')
text(ax, 9, 33, '$\\sigma$', 'varie', 'l')
text(ax, 50, 3, '1 à 8, chacun une fois en bas', 'resultat', 's')
save(fig, '46-159')
