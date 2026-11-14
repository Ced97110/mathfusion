import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
cx, cy, R = 44, 37, 20
V = {k: (cx + R * math.cos(math.radians(90 - 72 * (k - 1))), cy + R * math.sin(math.radians(90 - 72 * (k - 1)))) for k in range(1, 6)}
text(ax, 44, 74, r'$(1j)(1i)(1j)=(ij)$', 'resultat', 'm')
for k in (2, 3, 4, 5):
    def cut(a, b, m=2.8):
        d = math.hypot(b[0] - a[0], b[1] - a[1]); u = ((b[0] - a[0]) / d, (b[1] - a[1]) / d)
        return [(a[0] + m * u[0], a[1] + m * u[1]), (b[0] - m * u[0], b[1] - m * u[1])]
    line(ax, cut(V[1], V[k]), 'sujet' if k == 2 else 'varie', lw=1.0)
line(ax, cut(V[3], V[5]), 'resultat', lw=1.6)
for k, (x, y) in V.items():
    disc(ax, x, y, 2.8, 'encre' if False else 'sujet', label=str(k), size='s')
for k in (2, 3, 4, 5):
    t = 0.55 if k in (2, 5) else 0.4
    px = V[1][0] + t * (V[k][0] - V[1][0]); py = V[1][1] + t * (V[k][1] - V[1][1])
    text(ax, px + (3 if k in (2, 3) else -3), py + (1.5 if k in (2, 5) else -1.5), f'(1{k})', 'sujet' if k == 2 else 'varie', 's')
text(ax, 44, 67, '1 revient à sa place', 'fixe', 's')
text(ax, 44, 8, r'$(35)=(13)(15)(13)$', 'resultat', 'm')
text(ax, 44, 2.5, r'$(12)(12345)=(2345)$', 'sujet', 's')
save(fig, '64-182')
