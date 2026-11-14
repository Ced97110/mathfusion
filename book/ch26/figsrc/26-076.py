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

fig, ax = canvas(72)
for (y, a, v, w) in [(61, '89°', 'tan ≈ 57,29', 22), (51, '89,9°', 'tan ≈ 573', 30), (41, '89,99°', 'tan ≈ 5 730', 38)]:
    box(ax, 6, y, 22, 8, 'sujet', label=a)
    arrow(ax, (30, y + 4), (38, y + 4), 'varie')
    box(ax, 40, y, w + 8, 8, 'varie', label=v)
text(ax, 44, 35.5, 'grandit sans s’arrêter', 'varie', 's')
text(ax, 44, 28, 'tan 90° = sin 90° / cos 90°', 'encre', 's')
text(ax, 30, 19, '1', 'resultat', 'l'); text(ax, 44, 19, '÷', 'encre', 'l'); text(ax, 58, 19, '0', 'limite', 'l')
box(ax, 22, 3, 44, 9, 'limite', label='non définie', size='m')
save(fig, '26-076')
