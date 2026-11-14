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
fig, ax = canvas(52)
def one(cx, k, title, ordre, role):
    c = (cx, 26); R = 11
    ring(ax, c, R, 'fixe')
    vis = sorted({(k * j) % 12 for j in range(12)})
    for j in range(12): dot(ax, c, R, 30 * j, 'sujet' if j in vis else 'fixe', 1.5 if j in vis else 0.9)
    dot(ax, c, R, 30 * k, 'varie', 1.9)
    text(ax, cx, 8, title, 'varie', 's'); text(ax, cx, 2.5, ordre, role, 's')
one(15, 1, '$\\omega$', 'ordre 12', 'resultat'); one(44, 4, '$\\omega^4$', 'ordre 3', 'limite'); one(73, 6, '$\\omega^6$', 'ordre 2', 'limite')
text(ax, 15, 46, 'primitive', 'resultat', 's'); text(ax, 58.5, 46, 'pas primitives', 'limite', 's')
save(fig, '46-154')
