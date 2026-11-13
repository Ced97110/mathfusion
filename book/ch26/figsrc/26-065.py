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

fig, ax = canvas(58)
A, Bp, C = half(ax, (16, 9), 20, rb='sujet', rc='autre')
arc(ax, C, 7, 240, 270)
text(ax, C[0] - 3.1, C[1] - 11.6, '30°', 'encre', 's')
text(ax, 26, 5.8, 'opposé 1', 'sujet', 's')
text(ax, 22.5, 28, 'hypoténuse 2', 'autre', 's', ha='right')
text(ax, 38, 26, '√3', 'fixe', 's', ha='left')
box(ax, 48, 42, 38, 8, 'sujet', label='côté opposé : 1')
box(ax, 48, 30, 38, 8, 'autre', label='hypoténuse : 2')
box(ax, 48, 18, 38, 8, 'varie', label='1 ÷ 2 = 0,5')
arrow(ax, (67, 42), (67, 38.6), 'fixe'); arrow(ax, (67, 30), (67, 26.6), 'fixe'); arrow(ax, (67, 18), (67, 14.6), 'fixe')
box(ax, 48, 3, 38, 10, 'resultat', label='sin 30° = 1/2', size='l')
save(fig, '26-065')
