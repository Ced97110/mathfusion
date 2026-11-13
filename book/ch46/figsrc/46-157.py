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
for c, n, prim, title in (((21, 34), 12, (1, 5, 7, 11), '$\\varphi(12)=4$'), ((67, 34), 8, (1, 3, 5, 7), '$\\varphi(8)=4$')):
    R = 13
    ring(ax, c, R, 'fixe')
    for j in range(n):
        dot(ax, c, R, 360 / n * j, 'varie' if j in prim else 'fixe', 1.8 if j in prim else 1.0)
    for j in prim:
        s = '$\\omega$' if j == 1 else f'$\\omega^{{{j}}}$'
        lab(ax, c, R, 360 / n * j, s, 'varie', 's', d=5.5)
    text(ax, c[0], 8, title, 'resultat', 'm')
    text(ax, c[0], 58, f'racines {n}-ièmes', 'sujet', 's')
save(fig, '46-157')
