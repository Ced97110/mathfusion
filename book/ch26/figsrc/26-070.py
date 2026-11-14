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

fig, ax = canvas(54)
A, Bp, C = half(ax, (10, 9), 20, rb='sujet', rh='autre', rc='fixe')
arc(ax, C, 7, 240, 270); arc(ax, A, 7, 0, 60)
text(ax, C[0] - 3.1, C[1] - 11.6, '30°', 'encre', 's')
text(ax, 18.5, 12.8, '60°', 'encre', 's')
text(ax, 20, 5.8, '1', 'sujet', 'm')
text(ax, 32.5, 26, '√3', 'autre', 'm', ha='left')
text(ax, 17, 28, '2', 'fixe', 'm', ha='right')
box(ax, 44, 36, 42, 9, 'fixe', label='30° + 60° = 90°', size='m')
box(ax, 44, 22, 42, 9, 'sujet', label='sin 30° = cos 60° = 1/2', size='s')
box(ax, 44, 8, 42, 9, 'autre', label='cos 30° = sin 60° = √3/2', size='s')
save(fig, '26-070')
