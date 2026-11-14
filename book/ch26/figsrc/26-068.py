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
for (A0, u, base, hyp, q, cx) in [((11, 22), 6, '1', '2', '1 ÷ 2 = 0,5', 13), ((43, 22), 18, '3', '6', '3 ÷ 6 = 0,5', 52)]:
    A, Bp, C = half(ax, A0, u, rb='sujet', rc='autre')
    arc(ax, A, 4 if u < 10 else 7, 0, 60)
    text(ax, A[0] - 4.5, A[1] + 1.2, '60°', 'encre', 's')
    text(ax, A[0] + u / 2, A[1] - 3.2, base, 'sujet', 'm')
    text(ax, (A[0] + C[0]) / 2 - 2.5, (A[1] + C[1]) / 2 + 2, hyp, 'autre', 'm', ha='right')
    text(ax, cx, 13.5, q, 'varie', 's')
box(ax, 22, 1.5, 44, 8, 'resultat', label='cos 60° = 1/2', size='l')
save(fig, '26-068')
