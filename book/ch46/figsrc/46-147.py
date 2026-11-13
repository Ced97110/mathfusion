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
def one(c, n, R=14):
    ring(ax, c, R, 'fixe')
    for k in range(n): dot(ax, c, R, 360 / n * k, 'fixe', 0.7)
    a = 360 / n
    line(ax, [c, P(c, R, 0)], 'fixe'); line(ax, [c, P(c, R, a)], 'sujet')
    arcline(ax, c, 7, 0, a, 'varie')
    dot(ax, c, R, 0, 'fixe', 1.5); dot(ax, c, R, a, 'sujet', 1.8)
    lab(ax, c, R, 0, '1', d=4); lab(ax, c, R, a, '$\\omega$', 'sujet', d=5)
    p = P(c, 11 if n == 4 else 10.5, a / 2)
    text(ax, p[0], p[1], f'{int(a)}°', 'varie', 's')
    text(ax, c[0], 12, f'$n={n}$ : $360°/{n}={int(a)}°$', 'encre', 's')
one((22, 34), 12); one((66, 34), 4)
text(ax, 44, 64, '$\\omega=\\mathrm{cis}(360°/n)$', 'sujet', 'l')
save(fig, '46-147')
