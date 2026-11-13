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
fig, ax = canvas(62)
f = numberline(ax, 8, 76, 30, -4, 4, arrow_right=True)
disc(ax, f(-1), 30, 1.7, 'resultat'); disc(ax, f(1), 30, 1.7, 'resultat')
for v in (2, 4): disc(ax, f(v), 30, 1.7, 'limite')
arrow(ax, (f(2), 33), (f(4), 33), 'limite', curve=-0.5)
text(ax, 60, 44, '2, 4, 8, … : plus de retour', 'limite', 's')
brace(ax, f(-1), f(1), 23, 'resultat', label='$\\{1,-1\\}$')
text(ax, 44, 56, '$\\mathbb{R}^*$ : seuls $\\{1\\}$ et $\\{1,-1\\}$', 'autre', 'm')
save(fig, '46-149')
