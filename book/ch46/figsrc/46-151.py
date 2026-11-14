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
fig, ax = canvas(60)
f = numberline(ax, 4, 38, 28, 0, 9, labels=False, arrow_right=False)
for v in (1, 2, 4, 8): disc(ax, f(v), 28, 1.5, 'limite' if v > 1 else 'fixe')
for v in (1, 2, 4, 8): text(ax, f(v), 23.5, str(v), 'limite' if v > 1 else 'fixe', 's')
for a, b in ((1, 2), (2, 4), (4, 8)): arrow(ax, (f(a), 31), (f(b), 31), 'limite', curve=-0.5)
text(ax, 21, 54, 'droite : on s’éloigne', 'limite', 's')
text(ax, 21, 3, 'jamais de retour', 'limite', 's')
c = (66, 28); R = 15
ring(ax, c, R, 'fixe')
for a in (0, 120, 240): dot(ax, c, R, a, 'resultat' if a else 'fixe', 1.7)
for a in (0, 120, 240): arrow(ax, P(c, R, a + 12), P(c, R, a + 108), 'resultat', curve=0.38)
lab(ax, c, R, 0, '1', d=4); lab(ax, c, R, 120, '120°', 'resultat', d=6); lab(ax, c, R, 240, '240°', 'resultat', d=6)
text(ax, 66, 54, 'cercle : on revient', 'resultat', 's')
text(ax, 66, 3, 'après 3 pas : en 1', 'resultat', 's')
save(fig, '46-151')
