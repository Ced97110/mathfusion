import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
cx, cy, R = 44, 46, 26
vals = [pow(3, k, 7) for k in range(1, 7)]  # 3, 2, 6, 4, 5, 1
assert vals == [3, 2, 6, 4, 5, 1]
pts = []
for k in range(6):
    a = math.radians(90 - 60 * k)
    pts.append((cx + R * math.cos(a), cy + R * math.sin(a), a))
for k in range(6):
    x, y, a = pts[k]
    x2, y2, a2 = pts[(k + 1) % 6]
    d = math.hypot(x2 - x, y2 - y)
    ux, uy = (x2 - x) / d, (y2 - y) / d
    arrow(ax, (x + ux * 5.3, y + uy * 5.3), (x2 - ux * 5.3, y2 - uy * 5.3), 'varie', lw=0.9)
for k in range(6):
    x, y, a = pts[k]
    disc(ax, x, y, 4.6, 'resultat', label=str(vals[k]))
    text(ax, cx + (R + 10.5) * math.cos(a), cy + (R + 9) * math.sin(a), rf'$3^{k+1}$', 'varie', 's')
text(ax, cx, cy + 2.5, r'3 engendre', 'sujet', 's')
text(ax, cx, cy - 2.5, r'les 6 éléments', 'sujet', 's')
save(fig, '54-267')
