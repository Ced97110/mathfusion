import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role='varie', lw=0.9, n=30):
    line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
fig, ax = canvas(76)
C = (44, 38); R = 26
V = {k: pol(C, R, a) for k, a in zip('ABCDE', (90, 18, -54, -126, 162))}
poly(ax, [V['A'], V['B'], V['C']], 'fixe'); poly(ax, [V['A'], V['D'], V['E']], 'fixe')
poly(ax, [V['A'], V['C'], V['D']], 'sujet')
poly(ax, [V[k] for k in 'ABCDE'], 'encre', fill=False, lw=1.2)
A = V['A']
for k in 'BCDE':
    pass
dirs = {k: math.degrees(math.atan2(V[k][1] - A[1], V[k][0] - A[0])) for k in 'BCDE'}
for k1, k2 in (('B', 'C'), ('C', 'D'), ('D', 'E')):
    text(ax, *pol(A, 14, (dirs[k1] + dirs[k2]) / 2), '36°', 'varie', 's')
    arc(ax, A, 9, dirs[k1], dirs[k2], 'varie', lw=0.9) if dirs[k1] > dirs[k2] else arc(ax, A, 9, dirs[k2], dirs[k1], 'varie', lw=0.9)
for k in 'CD':
    g = ((A[0] + V['C'][0] + V['D'][0]) / 3, (A[1] + V['C'][1] + V['D'][1]) / 3)
    q = (V[k][0] + 0.3 * (g[0] - V[k][0]), V[k][1] + 0.3 * (g[1] - V[k][1]))
    text(ax, q[0], q[1] + 2.5, '72°', 'varie', 's')
q = (V['B'][0] + 0.3 * (C[0] - V['B'][0]), V['B'][1] + 0.3 * (C[1] - V['B'][1]))
text(ax, q[0] - 1, q[1] + 3, '108°', 'fixe', 's')
for k, (dx, dy) in zip('ABCDE', ((0, 5), (5, 2), (4, -4), (-4, -4), (-5, 2))):
    text(ax, V[k][0] + dx, V[k][1] + dy, k, 'encre', 'm', weight='bold')
text(ax, 44, 4, '36° + 72° + 72° = 180°', 'resultat', 's')
save(fig, '26-131')
