import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 24, 30, 18
P = lambda k: (cx + R * math.sin(math.radians(30 * k)), cy + R * math.cos(math.radians(30 * k)))
mem = {0, 8, 4}
for k in range(12):
    x, y = P(k)
    disc(ax, x, y, 2.0 if k in mem else 0.9, 'sujet' if k in mem else 'fixe')
for k in mem:
    x, y = P(k); text(ax, cx + (x - cx) * 1.28, cy + (y - cy) * 1.28, str(k), 'sujet', 's')
for a, b in [(0, 8), (8, 4), (4, 0)]:
    (x0, y0), (x1, y1) = P(a), P(b)
    t0, t1 = 0.14, 0.86
    arrow(ax, (x0 + (x1 - x0) * t0, y0 + (y1 - y0) * t0), (x0 + (x1 - x0) * t1, y0 + (y1 - y0) * t1), 'varie', lw=0.9)
text(ax, cx, cy, 'pas de 8', 'varie', 's')
text(ax, 66, 54, r'$n$ = 12, $k$ = 8', 'encre', 'm')
box(ax, 48, 36, 36, 8, 'fixe', label='PGCD(8, 12) = 4', size='s')
arrow(ax, (66, 36), (66, 30), 'fixe')
box(ax, 48, 21, 36, 9, 'resultat', label=r'ordre = 12 ÷ 4 = 3', size='s')
text(ax, 66, 13, '3 pas pour revenir à 0', 'varie', 's')
save(fig, '46-123')
