import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(60)
u = 17.45
x0 = 14
for n, y, v1, v2 in ((2, 40, '0,03490', '0,03490'), (3, 12, '0,05235', '0,05234')):
    for i in range(n):
        poly(ax, [(x0 + i * u, y + 2), (x0 + (i + 1) * u, y + 2), (x0 + (i + 1) * u, y + 8), (x0 + i * u, y + 8)], 'autre')
    xl = float(v2.replace(',', '.')) * 1000
    poly(ax, [(x0, y - 8), (x0 + xl, y - 8), (x0 + xl, y - 2), (x0, y - 2)], 'sujet')
    text(ax, 2, y + 5, f'{n} × sin 1°', 'autre', 's', ha='left') if False else None
    text(ax, x0 + n * u + 2, y + 5, v1, 'autre', 's', ha='left')
    text(ax, x0 + xl + 2, y - 5, v2, 'sujet', 's', ha='left')
    text(ax, 7, y + 5, f'{n} ×\nsin 1°', 'autre', 's')
    text(ax, 7, y - 5, f'sin {n}°', 'sujet', 's')
text(ax, 44, 57, 'quasi la même longueur', 'varie', 's')
save(fig, '29-012')
