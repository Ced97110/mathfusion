import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(84)

def bits(ax, x, y, s, roles, cw, ch=5.5, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

def d(a, b):
    return sum(p != q for p, q in zip(a, b))

W = {'x': '10101', 'y': '11010', 'z': '00011'}
R = {'x': 'sujet', 'y': 'autre', 'z': 'resultat'}
dxy, dxz, dyz = d(W['x'], W['y']), d(W['x'], W['z']), d(W['y'], W['z'])
assert (dxy, dxz, dyz) == (4, 3, 3)
assert [w.count('1') for w in W.values()] == [3, 3, 2]
text(ax, 62, 79, 'poids', 'fixe', 's')
for k, (n, w) in enumerate(W.items()):
    y = 70 - k * 8
    text(ax, 12, y + 2.75, r'$%s$' % n, R[n], 'm', weight='bold')
    bits(ax, 20, y, w, [R[n] if c == '1' else 'fixe' for c in w], 6.0)
    text(ax, 62, y + 2.75, str(w.count('1')), R[n], 'm', weight='bold')
# triangle de côtés 4, 3, 3 (8 mm par unité)
u = 8.0
A = (24, 10); B = (A[0] + dxy * u, 10)
h = math.sqrt((dxz * u) ** 2 - (dxy * u / 2) ** 2)
C = (A[0] + dxy * u / 2, 10 + h)
assert abs(math.dist(B, C) - dyz * u) < 1e-6
def cut(P, Q, r=3.0):
    dx, dy = Q[0] - P[0], Q[1] - P[1]; L = math.hypot(dx, dy)
    return (P[0] + dx / L * r, P[1] + dy / L * r), (Q[0] - dx / L * r, Q[1] - dy / L * r)
for P, Q in [(A, B), (B, C), (C, A)]:
    line(ax, list(cut(P, Q)), 'fixe', lw=1.0)
for P, n in [(A, 'x'), (B, 'y'), (C, 'z')]:
    disc(ax, P[0], P[1], 3.0, R[n], label=r'$%s$' % n)
text(ax, (A[0] + B[0]) / 2, 5, str(dxy), 'varie', 'm', weight='bold')
text(ax, (A[0] + C[0]) / 2 - 3.5, (A[1] + C[1]) / 2 + 1.5, str(dxz), 'varie', 'm', weight='bold')
text(ax, (B[0] + C[0]) / 2 + 3.5, (B[1] + C[1]) / 2 + 1.5, str(dyz), 'varie', 'm', weight='bold')
text(ax, 70, 22, 'distances :\nles côtés', 'varie', 's')
save(fig, '68-049')
