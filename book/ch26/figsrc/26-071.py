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

fig, ax = canvas(80)
k = 4.0
rows = [(30, 50, '5 cm', '8,66 cm'), (10, 30, '1,74 cm', '9,85 cm'), (1, 14, '0,17 cm', '10,00 cm')]
for (th, yb, o, a) in rows:
    A = (8, yb); Bp = (8 + 10 * k * math.cos(math.radians(th)), yb); C = (Bp[0], yb + 10 * k * math.sin(math.radians(th)))
    poly(ax, [A, Bp, C], 'fixe', lw=0.4)
    line(ax, [A, Bp], 'varie', lw=1.8); line(ax, [Bp, C], 'sujet', lw=1.8); line(ax, [A, C], 'fixe', lw=1.4)
    arc(ax, A, 14, 0, th)
    text(ax, 52, yb + 8, f'{th}°', 'encre', 'm', ha='left', weight='bold')
    text(ax, 52, yb + 4.2, 'opposé ' + o, 'sujet', 's', ha='left')
    text(ax, 52, yb + 0.6, 'adjacent ' + a, 'varie', 's', ha='left')
text(ax, 22, 64, 'hypoténuse 10 cm', 'fixe', 's', ha='right')
box(ax, 14, 1, 60, 8, 'resultat', label='rapports vers 0 et vers 1', size='s')
save(fig, '26-071')
