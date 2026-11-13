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

fig, ax = canvas(60)
for (A0, u, adj, hyp, q, la, lh, lb) in [((12, 22), 8, '1,7321', '2', '1,7321 ÷ 2 ≈ 0,8660', 16, 'x', 0), ((44, 22), 16, '3,4641', '4', '3,4641 ÷ 4 ≈ 0,8660', 52, 'x', 0)]:
    A, Bp, C = half(ax, A0, u, rh='sujet', rc='autre')
    arc(ax, C, 4 if u < 10 else 7, 240, 270)
    text(ax, C[0] - 6.5, C[1] + 1, '30°', 'encre', 's')
    text(ax, Bp[0] + 1.8, (Bp[1] + C[1]) / 2, adj, 'sujet', 's', ha='left')
    text(ax, (A[0] + C[0]) / 2 - 2.8, (A[1] + C[1]) / 2 + 2, hyp, 'autre', 'm', ha='right')
    text(ax, la, 16, q, 'varie', 's')
text(ax, 35, 16, '=', 'encre', 'm')
box(ax, 22, 2, 44, 9, 'resultat', label='cos 30° = √3/2', size='l')
save(fig, '26-066')
