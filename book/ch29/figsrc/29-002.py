import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(60)
k = 60 / 209.4
rows = [(6, '52,4 m', 46), (12, '104,7 m', 30), (24, '209,4 m', 14)]
x0 = 16
for d, lab, y in rows:
    Lm = float(lab.split()[0].replace(',', '.'))
    text(ax, 8, y, f'{d}°', 'varie', 'm')
    poly(ax, [(x0, y - 4), (x0 + Lm * k, y - 4), (x0 + Lm * k, y + 4), (x0, y + 4)], 'sujet')
    text(ax, x0 + Lm * k + 2, y, lab, 'sujet', 's', ha='left')
for y in (38, 22):
    arrow(ax, (5, y + 3), (5, y - 3), 'varie')
    text(ax, 11, y, '×2', 'varie', 's')
    arrow(ax, (x0 + 72 * k, y + 3) if False else (84, y + 3), (84, y - 3), 'varie')
    text(ax, 78, y, '×2', 'varie', 's')
save(fig, '29-002')
