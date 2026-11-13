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
A = (10, 6); R = 40
line(ax, [A, (52, 6)], 'fixe', lw=1.0)
for th in (30, 89, 90):
    E = (A[0] + R * math.cos(math.radians(th)), A[1] + R * math.sin(math.radians(th)))
    line(ax, [A, E], 'fixe', lw=1.6)
    line(ax, [E, (E[0], A[1])], 'sujet', lw=1.8)
text(ax, 47, 27, '30°', 'encre', 'm', ha='left')
text(ax, 14, 46, '89°', 'encre', 'm', ha='left')
text(ax, 5.5, 46, '90°', 'encre', 'm')
text(ax, 22, 36, 'opposé ≈ 9,9985 cm', 'sujet', 's', ha='left')
text(ax, 22, 51, 'hypoténuse 10 cm', 'fixe', 's', ha='left')
text(ax, 71, 40, '10 ÷ 10 = 1', 'varie', 's')
arrow(ax, (71, 37), (71, 31), 'fixe')
box(ax, 56, 19, 30, 11, 'resultat', label='sin 90° = 1', size='m')
save(fig, '26-074')
