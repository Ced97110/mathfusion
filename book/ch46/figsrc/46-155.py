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
R = 13
for c, role, names in (((20, 34), 'autre', ['0', '4', '8']), ((68, 34), 'sujet', ['1', '$\\omega^4$', '$\\omega^8$'])):
    ring(ax, c, R, 'fixe')
    for j in range(12): dot(ax, c, R, 30 * j, 'fixe', 0.8)
    poly(ax, [P(c, R, a) for a in (0, 120, 240)], role, fill=False, lw=1.0)
    for i, a in enumerate((0, 120, 240)):
        dot(ax, c, R, a, role, 1.8); lab(ax, c, R, a, names[i], role, 's', d=4.5 if i == 0 else 6)
arrow(ax, (42, 34), (50, 34), 'varie', both=True)
text(ax, 46, 39, 'même forme', 'varie', 's')
text(ax, 20, 8, '$\\langle4\\rangle=\\{0,4,8\\}$', 'autre', 's'); text(ax, 68, 8, '$\\langle\\omega^4\\rangle$ : triangle', 'sujet', 's')
save(fig, '46-155')
