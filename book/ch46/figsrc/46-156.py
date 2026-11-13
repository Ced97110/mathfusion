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
fig, ax = canvas(80)
text(ax, 44, 74, 'ordre de $\\omega^k$ : $12/d$', 'sujet', 'm')
for y, k, d in ((56, 4, 4), (34, 5, 1), (12, 6, 6)):
    c = (16, y); R = 9
    ring(ax, c, R, 'fixe')
    vis = {(k * j) % 12 for j in range(12)}
    for j in range(12): dot(ax, c, R, 30 * j, 'sujet' if j in vis else 'fixe', 1.4 if j in vis else 0.8)
    dot(ax, c, R, 30 * k, 'varie', 1.8)
    text(ax, 32, y + 3.5, f'$\\omega^{k}$ : $d={d}$', 'varie', 'm', ha='left')
    text(ax, 32, y - 3.5, f'$12/{d}={12 // d}$ points', 'resultat', 'm', ha='left')
save(fig, '46-156')
