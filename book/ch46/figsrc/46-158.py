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
fig, ax = canvas(64)
xs = row(ax, 20, 44, range(1, 9), 'autre')
for x in xs:
    box(ax, x - 3.6, 39, 7.2, 10, 'autre'); box(ax, x - 3.6, 19, 7.2, 10, 'sujet', fill=False, dash=True)
text(ax, 9, 44, 'nombre', 'autre', 's'); text(ax, 9, 24, 'image', 'sujet', 's')
arrow(ax, (xs[0], 38), (xs[0], 30), 'varie')
box(ax, xs[0] - 4.0, 18.5, 8.0, 31, 'varie', fill=False, lw=1.2)
text(ax, xs[0] + 6, 56, 'une colonne', 'varie', 's')
brace(ax, xs[0] - 4, xs[-1] + 4, 16, 'fixe', label='8 colonnes')
save(fig, '46-158')
