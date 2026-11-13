import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
S3 = 3 ** 0.5
def arc(ax, P, r, a0, a1, role='encre'):
    pts = [(P[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 20)), P[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 20))) for i in range(21)]
    line(ax, pts, role, lw=0.7)
def half(ax, A, u, rb='fixe', rh='fixe', rc='fixe'):
    B = (A[0] + u, A[1]); C = (A[0] + u, A[1] + u * S3)
    poly(ax, [A, B, C], 'fixe', lw=0.4)
    line(ax, [A, B], rb, lw=1.8); line(ax, [B, C], rh, lw=1.8); line(ax, [A, C], rc, lw=1.8)
    s = min(2.0, u * 0.2)
    line(ax, [(B[0] - s, B[1]), (B[0] - s, B[1] + s), (B[0], B[1] + s)], 'fixe', lw=0.7)
    return A, B, C

fig, ax = canvas(72)
k = 1.1
for (x0, L, hyp, adj, lx) in [(22, 10, '10', '0,17', 26), (56, 50, '50', '0,87', 60)]:
    A = (x0, 10); C = (x0 + L * k * math.cos(math.radians(89)), 10 + L * k * math.sin(math.radians(89))); Bp = (C[0], 10)
    line(ax, [A, C], 'autre', lw=1.8); line(ax, [A, Bp], 'sujet', lw=2.4); line(ax, [Bp, C], 'fixe', lw=0.6, dash=True)
    text(ax, lx, 10 + L * k / 2 + (2 if L < 20 else 0), 'hypoténuse ' + hyp, 'autre', 's', ha='left')
    text(ax, x0, 5.5, 'adjacent ≈ ' + adj, 'sujet', 's')
for x0 in (22, 56): text(ax, x0 - 5, 14, '89°', 'encre', 's')
text(ax, 74, 28, 'adjacent → 0', 'sujet', 's')
box(ax, 62, 52, 24, 12, 'resultat', label='cos 90° = 0', size='m')
arrow(ax, (82, 51), (82, 31), 'fixe')
save(fig, '26-075')
