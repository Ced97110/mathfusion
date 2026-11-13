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

fig, ax = canvas(66)
ys = [58, 48, 38, 28, 18]
ang = ['0°', '30°', '45°', '60°', '90°']
for i, y in enumerate(ys):
    box(ax, 4, y - 3.5, 34, 7, 'sujet', label=f'sin {ang[i]} = √{i}/2', size='s')
    box(ax, 50, y - 3.5, 34, 7, 'autre', label=f'cos {ang[i]} = √{4 - i}/2', size='s')
for i, y in enumerate(ys):
    arrow(ax, (38.5, y), (49.5, ys[4 - i]), 'varie', lw=0.8)
box(ax, 22, 3, 44, 8, 'fixe', label='cos A = sin(90° − A)', size='s')
save(fig, '26-079')
