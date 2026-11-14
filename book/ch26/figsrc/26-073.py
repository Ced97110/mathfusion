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
for (y, L, hyp, adj) in [(44, 14, '10', '9,9985'), (26, 70, '50', '49,99')]:
    line(ax, [(8, y), (8 + L, y)], 'autre', lw=2.4)
    line(ax, [(8, y - 3), (8 + L - 0.1, y - 3)], 'sujet', lw=2.4)
    line(ax, [(8 + L, y + 1.5), (8 + L, y - 4.5)], 'fixe', lw=0.6, dash=True)
    text(ax, 8, y + 4, 'hypoténuse ' + hyp, 'autre', 's', ha='left')
    text(ax, 8, y - 7, 'adjacent ≈ ' + adj, 'sujet', 's', ha='left')
text(ax, 40, 44, 'angle de 1°', 'encre', 's', ha='left')
text(ax, 44, 12.5, 'à 0° : adjacent = hypoténuse', 'encre', 's')
box(ax, 14, 1, 60, 8, 'resultat', label='10/10 = 50/50 = 1 : cos 0° = 1', size='s')
save(fig, '26-073')
