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
fig, ax = canvas(72)
f = numberline(ax, 8, 66, 36, 0, 5)
disc(ax, f(1), 36, 1.8, 'fixe')
for v in (2, 4): disc(ax, f(v), 36, 1.6, 'varie')
for v in (0.5, 0.25): disc(ax, f(v), 36, 1.3, 'varie')
text(ax, f(0.5) + 1, 40.5, '½', 'varie', 's'); text(ax, f(0.25) - 1, 40.5, '¼', 'varie', 's')
arrow(ax, (f(0.5) - 1, 44), (f(0.25) + 1, 44), 'varie')
arrow(ax, (f(2), 39), (f(4), 39), 'varie', curve=-0.5)
text(ax, 63, 43, '8…', 'varie', 's')
text(ax, f(1), 29, '', 'fixe')
box(ax, 14, 58, 60, 9, 'sujet', label='départ : $|x|\\neq1$')
text(ax, 20, 49, '$|x|<1$ : rapetisse', 'varie', 's'); text(ax, 62, 49, '$|x|>1$ : grandit', 'varie', 's')
box(ax, 14, 4, 60, 9, 'resultat', label='arrivée : jamais $|x|^k=1$')
arrow(ax, (44, 22), (44, 14), 'resultat')
save(fig, '46-150')
