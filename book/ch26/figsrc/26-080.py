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

fig, ax = canvas(62)
O = (14, 10); X = lambda a: O[0] + a * 62 / 90; Y = lambda v: O[1] + v * 40
arrow(ax, O, (80, 10), 'fixe', lw=0.8); arrow(ax, O, (14, 54), 'fixe', lw=0.8)
for a in (30, 60, 90):
    line(ax, [(X(a), 8.8), (X(a), 11.2)], 'fixe', lw=0.7); text(ax, X(a), 5.5, f'{a}°', 'fixe', 's')
text(ax, 10, 10, '0', 'fixe', 's'); text(ax, 10, Y(1), '1', 'fixe', 's')
line(ax, [(14, 10), (X(90), Y(1))], 'fixe', dash=True, lw=1.0)
line(ax, [(X(a), Y(math.sin(math.radians(a)))) for a in range(0, 91, 3)], 'sujet', lw=1.8)
for a, v, vp in [(30, '0,5', '0,3333'), (60, '0,8660', '0,6667')]:
    s = math.sin(math.radians(a))
    disc(ax, X(a), Y(s), 1.0, 'sujet'); disc(ax, X(a), Y(a / 90), 1.0, 'fixe')
text(ax, 30, 33, '0,5', 'sujet', 's'); text(ax, 38.5, 19, '0,3333', 'fixe', 's', ha='left')
text(ax, 49, 48, '0,8660', 'sujet', 's'); text(ax, 58.5, 32, '0,6667', 'fixe', 's', ha='left')
text(ax, 66, 53, 'sinus', 'sujet', 's')
text(ax, 70, 37, 'proportionnel', 'fixe', 's')
save(fig, '26-080')
