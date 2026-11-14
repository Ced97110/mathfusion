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
A = (8, 18); R = 50
for th in (30, 1, 0):
    E = (A[0] + R * math.cos(math.radians(th)), A[1] + R * math.sin(math.radians(th)))
    line(ax, [A, E], 'fixe', lw=1.6)
    if th > 0: line(ax, [E, (E[0], A[1])], 'sujet', lw=1.8)
text(ax, 54, 44, '30°', 'encre', 'm', ha='left')
text(ax, 62, 21.5, '1°', 'encre', 'm', ha='left')
text(ax, 62, 15, '0°', 'encre', 'm', ha='left')
text(ax, 4, 31, 'hypoténuse 10 cm', 'fixe', 's', ha='left')
text(ax, 34, 13.5, 'opposé → 0', 'sujet', 's')
arrow(ax, (57, 41), (68, 27), 'varie', curve=-0.3)
text(ax, 77, 36, 'on couche', 'varie', 's')
box(ax, 18, 1.5, 52, 9, 'resultat', label='0 ÷ 10 = 0 : sin 0° = 0', size='m')
save(fig, '26-072')
