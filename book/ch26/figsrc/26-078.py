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

fig, ax = canvas(60)
xs = [10, 27, 44, 61, 78]
data = [('0°', '0', '√0/2'), ('30°', '0,5', '√1/2'), ('45°', '0,7071', '√2/2'), ('60°', '0,8660', '√3/2'), ('90°', '1', '√4/2')]
text(ax, 44, 56, 'en décimaux : pas de loi', 'fixe', 's')
for x, (a, d, r) in zip(xs, data):
    text(ax, x, 46, a + chr(10) + d, 'fixe', 's')
    line(ax, [(x, 41.5), (x, 32)], 'fixe', lw=0.7, dash=True)
    box(ax, x - 5.5, 21, 11, 10, 'sujet', label=r, size='s')
for x0, x1 in zip(xs[:-1], xs[1:]):
    arrow(ax, (x0 + 6.2, 26), (x1 - 6.2, 26), 'varie')
text(ax, 44, 13, 'racines : 0, 1, 2, 3, 4', 'varie', 's')
save(fig, '26-078')
