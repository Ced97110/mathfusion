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

fig, ax = canvas(64)
text(ax, 44, 61, 'à 90°, hypoténuse 10 cm', 'encre', 's')
for (x, role, head, frac, den, st) in [(3, 'resultat', 'sinus', '10 ÷ 10', 'hypoténuse', 'possible'), (31, 'resultat', 'cosinus', '0 ÷ 10', 'hypoténuse', 'possible'), (59, 'limite', 'tangente', '10 ÷ 0', 'adjacent', 'impossible')]:
    box(ax, x, 4, 26, 50, role, label=None)
    text(ax, x + 13, 47, head, role, 'm', weight='bold')
    text(ax, x + 13, 36, frac, role, 'l')
    text(ax, x + 13, 23, 'dénominateur' + chr(10) + den, role, 's')
    box(ax, x + 3, 7, 20, 8, role, label=st, size='s', fill=False)
save(fig, '26-077')
