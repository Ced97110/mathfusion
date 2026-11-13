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

fig, ax = canvas(56)
u = 16; Ax, y0 = 18, 12
A = (Ax, y0); Hp = (Ax + u, y0); Bp = (Ax + 2 * u, y0); C = (Ax + u, y0 + u * S3)
poly(ax, [A, Bp, C], 'fixe', lw=0.4)
line(ax, [Hp, Bp], 'fixe', lw=1.2); line(ax, [C, Bp], 'fixe', lw=1.2)
line(ax, [C, Hp], 'fixe', dash=True, lw=0.9)
line(ax, [A, Hp], 'sujet', lw=2.0); line(ax, [A, C], 'autre', lw=2.0)
arc(ax, C, 7, 240, 270)
text(ax, C[0] - 3.1, C[1] - 11.6, '30°', 'encre', 's')
text(ax, 26, 8.6, 'opposé 1', 'sujet', 's')
text(ax, 42, 8.6, '1', 'fixe', 's')
brace(ax, Ax, Bp[0], 6.2, 'fixe', label='base 2')
text(ax, 22.5, 28, 'côté entier 2', 'autre', 's', ha='right')
box(ax, 54, 38, 32, 8, 'sujet', label='opposé = ½ base', size='s')
box(ax, 54, 27, 32, 8, 'autre', label='hypoténuse = base', size='s')
box(ax, 54, 16, 32, 8, 'varie', label='½ base ÷ base = 1/2', size='s')
arrow(ax, (70, 38), (70, 35.6), 'fixe'); arrow(ax, (70, 27), (70, 24.6), 'fixe')
box(ax, 54, 3, 32, 9, 'resultat', label='sin 30° = 1/2', size='m')
save(fig, '26-069')
