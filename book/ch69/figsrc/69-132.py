import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 44, 86, r'dans $\mathbb{Z}/5\mathbb{Z}$', 'encre', 'm')
text(ax, 44, 80.5, 'on suppose 1 positif', 'encre', 'm')
cx, cy, R, r = 44, 46, 24, 4.5
P = []
for i in range(5):
    a = math.radians(90 - 72 * i)
    P.append((cx + R * math.cos(a), cy + R * math.sin(a)))
for i in range(5):
    (x1, y1), (x2, y2) = P[i], P[(i + 1) % 5]
    d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    arrow(ax, (x1 + ux * (r + 0.8), y1 + uy * (r + 0.8)), (x2 - ux * (r + 0.8), y2 - uy * (r + 0.8)), 'varie')
for i, (x, y) in enumerate(P):
    disc(ax, x, y, r, 'limite' if i == 0 else 'sujet', label=str(i))
text(ax, cx, cy, r'$1+1+1+1+1=0$', 'encre', 's')
text(ax, 72, 17, 'chaque flèche : +1', 'varie', 's')
text(ax, 44, 6, '0 positif : impossible', 'limite', 'm')
save(fig, '69-132')
