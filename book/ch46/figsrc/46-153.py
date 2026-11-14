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
fig, ax = canvas(84)
c = (44, 44); R = 22
ring(ax, c, R, 'fixe')
for k in range(12): dot(ax, c, R, 30 * k, 'sujet' if k % 3 == 0 else 'fixe', 1.8 if k % 3 == 0 else 1.2)
arcline(ax, c, 12, 0, 30, 'varie')
line(ax, [c, P(c, R, 0)], 'fixe', lw=0.6); line(ax, [c, P(c, R, 30)], 'fixe', lw=0.6)
lab(ax, c, R, 30, '$\\omega^1$', 'sujet', d=5)
p = P(c, 17, 15); text(ax, p[0], p[1], '30°', 'varie', 's')
text(ax, c[0] + R + 3, c[1], '$\\omega^0=1$', 'sujet', 's', ha='left')
text(ax, c[0], c[1] + R + 4, '$\\omega^3=i$', 'sujet', 's')
text(ax, c[0] - R - 3, c[1], '$\\omega^6=-1$', 'sujet', 's', ha='right')
text(ax, c[0], c[1] - R - 4, '$\\omega^9=-i$', 'sujet', 's')
text(ax, 44, 6, '$\\omega^k$ : angle $k\\times30°$', 'varie', 'm')
save(fig, '46-153')
