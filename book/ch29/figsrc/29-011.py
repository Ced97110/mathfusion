import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(48)
k = 60 / 0.05234
for d, v, y in ((1, '0,01745', 36), (2, '0,03490', 24), (3, '0,05234', 12)):
    x = float(v.replace(',', '.')) * k
    text(ax, 3, y, f'{d}°', 'varie', 'm', ha='left')
    poly(ax, [(14, y - 4), (14 + x, y - 4), (14 + x, y + 4), (14, y + 4)], 'sujet')
    text(ax, 14 + x + 2, y, v, 'sujet', 's', ha='left')
text(ax, 44, 45, 'sinus de l’angle', 'sujet', 's')
save(fig, '29-011')
