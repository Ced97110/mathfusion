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
fig, ax = canvas(70)
R = 11
for c, role, names, shape in (((18, 38), 'autre', ['0', '1', '2', '3'], 'horloge'), ((70, 38), 'sujet', ['1', '$i$', '$-1$', '$-i$'], 'racines')):
    ring(ax, c, R, 'fixe')
    poly(ax, [P(c, R, 90 * k) for k in range(4)], role, fill=False, lw=0.8)
    for k in range(4): dot(ax, c, R, 90 * k, role, 1.7)
    for k in range(4): lab(ax, c, R, 90 * k, names[k], role, 's', d=4 if k != 2 or role == 'autre' else 5)
arrow(ax, (37, 38), (50, 38), 'varie', both=True)
text(ax, 44, 43, '$\\cong$', 'varie', 'l')
text(ax, 18, 63, 'horloge $\\mathbb{Z}/4\\mathbb{Z}$', 'autre', 's'); text(ax, 70, 63, 'racines 4-ièmes de 1', 'sujet', 's')
text(ax, 18, 14, 'addition : $1+3=0$', 'autre', 's'); text(ax, 70, 14, '$i\\times(-i)=1$', 'sujet', 's')
save(fig, '46-148')
