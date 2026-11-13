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
A, Bp, C = half(ax, (12, 9), 20, rh='sujet', rc='autre')
arc(ax, A, 7, 0, 60)
text(ax, A[0] + 9.5, A[1] + 3.5, '60°', 'encre', 's')
text(ax, 22, 5.8, 'base 1', 'fixe', 's')
text(ax, 19, 28, 'hypoténuse 2', 'autre', 's', ha='right')
text(ax, 34, 26, 'opposé √3', 'sujet', 's', ha='left')
box(ax, 52, 42, 34, 8, 'sujet', label='côté opposé : √3')
box(ax, 52, 30, 34, 8, 'autre', label='hypoténuse : 2')
box(ax, 52, 18, 34, 8, 'varie', label='√3 ÷ 2 ≈ 0,8660')
arrow(ax, (69, 42), (69, 38.6), 'fixe'); arrow(ax, (69, 30), (69, 26.6), 'fixe'); arrow(ax, (69, 18), (69, 14.6), 'fixe')
box(ax, 52, 3, 34, 10, 'resultat', label='sin 60° = √3/2', size='m')
save(fig, '26-067')
