import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b, _d = box, disc
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
def disc(ax, x, y, r, role='fixe', label=None, size='m', **k): return _d(ax, x, y, r, role, label=label, size=size, **k)
fig, ax = canvas(96)
text(ax, 44, 91, 'un entier sur trois', 'sujet')
for n in range(13):
    x = 6 + 6.2 * n
    disc(ax, x, 80, 1.1 if n % 3 else 2.2, 'fixe' if n % 3 else 'sujet')
    if n % 3 == 0: text(ax, x, 73, str(n), 'sujet', 's')
cx, cy, R = 44, 41, 19
P = {k: (cx + R * math.sin(math.radians(90 * k)), cy + R * math.cos(math.radians(90 * k))) for k in range(4)}
for k, (x, y) in P.items(): disc(ax, x, y, 5, 'resultat', str(k), 'l')
order = [0, 3, 2, 1, 0]
for a, b in zip(order, order[1:]):
    (x1, y1), (x2, y2) = P[a], P[b]; d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    arrow(ax, (x1 + 6.2 * ux, y1 + 6.2 * uy), (x2 - 6.2 * ux, y2 - 6.2 * uy), 'varie')
text(ax, 44, 7, '+ 3 : un cran en arrière', 'varie', 's')
text(ax, 44, 3, 'les 4 positions sont atteintes', 'resultat', 's') if False else None
save(fig, '48-062')
