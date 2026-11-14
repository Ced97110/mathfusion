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
fig, ax = canvas(74)
c = (27, 38); R = 17
ring(ax, c, R, 'sujet', 1.0)
for a in range(0, 360, 6):
    p = P(c, R, a); disc(ax, p[0], p[1], 0.45, 'sujet')
poly(ax, [P(c, R, a) for a in (0, 120, 240)], 'resultat', fill=False, lw=0.9)
poly(ax, [P(c, R, a) for a in (0, 90, 180, 270)], 'varie', fill=False, lw=0.9)
for a in (120, 240): dot(ax, c, R, a, 'resultat', 1.6)
for a in (0, 90, 180, 270): dot(ax, c, R, a, 'varie', 1.6)
lab(ax, c, R, 0, '1', d=4); lab(ax, c, R, 90, '$i$', d=4); lab(ax, c, R, 180, '$-1$', d=5); lab(ax, c, R, 270, '$-i$', d=4)
text(ax, 27, 66, 'cercle $\\mathbb{T}$ : infini', 'sujet', 'm')
text(ax, 27, 13, 'carré : ordre 4', 'varie', 's'); text(ax, 27, 7, 'triangle : ordre 3', 'resultat', 's')
f = numberline(ax, 52, 82, 38, -3, 3, labels=False, arrow_right=False)
for v in (-1, 1): disc(ax, f(v), 38, 1.6, 'autre')
text(ax, f(-1), 33, '$-1$', 'autre', 's'); text(ax, f(1), 33, '1', 'autre', 's')
text(ax, 67, 47, '$\\mathbb{R}^*$ : ordre 1 ou 2', 'autre', 'm')
text(ax, 67, 22, 'aucun sous-groupe\nd’ordre 3', 'limite', 's')
save(fig, '46-145')
