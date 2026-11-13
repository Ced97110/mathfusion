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
c = (44, 52); R = 22
ring(ax, c, R, 'fixe')
line(ax, [(c[0] - R - 3, c[1]), (c[0] + R + 3, c[1])], 'fixe', lw=0.6, dash=True)
seq = [(5 * k) % 12 * 30 for k in range(13)]
line(ax, [P(c, R, a) for a in seq], 'fixe', lw=0.5)
for a0, a1 in ((30, 330), (150, 210)):
    line(ax, [P(c, R, a0), P(c, R, a1)], 'varie', lw=0.9, dash=True)
text(ax, c[0] + R + 4, c[1] + 3, 'miroir', 'varie', 's', ha='left')
poly(ax, [P(c, R, a) for a in (0, 120, 240)], 'sujet', fill=False, lw=1.1)
for k in range(12):
    a = 30 * k
    role = 'varie' if k in (1, 5, 7, 11) else ('sujet' if k in (0, 4, 8) else 'fixe')
    dot(ax, c, R, a, role, 1.8 if role != 'fixe' else 1.2)
for k, s in ((1, '$\\omega$'), (5, '$\\omega^5$'), (7, '$\\omega^7$'), (11, '$\\omega^{11}$')): lab(ax, c, R, 30 * k, s, 'varie', d=5)
text(ax, 8, 20, 'orange : primitives, en miroir', 'varie', 's', ha='left')
text(ax, 8, 13, 'bleu : triangle à 120°', 'sujet', 's', ha='left')
text(ax, 8, 6, 'gris : 0, 5, 10, 3, ... (12 pas)', 'fixe', 's', ha='left')
save(fig, '46-152')
