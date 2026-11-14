import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(78)
res = {3: 2, 4: 0, 5: 1}
calc = {3: '1 × 2 = 2', 4: '3 × 0 = 0', 5: '2 × 3 = 1'}
cy, rr = 54, 10
for cx, m in [(16, 3), (44, 4), (72, 5)]:
    text(ax, cx, 69, f'{m} heures', 'sujet', 'm')
    disc(ax, cx, cy, rr, 'sujet')
    for i in range(m):
        a = math.radians(90 - 360 * i / m)
        p = (cx + 0.78 * rr * math.cos(a), cy + 0.78 * rr * math.sin(a))
        if i == res[m]:
            line(ax, [(cx, cy), p], 'resultat', lw=1.2)
            disc(ax, p[0], p[1], 1.7, 'resultat')
        else:
            disc(ax, p[0], p[1], 0.9, 'fixe')
    text(ax, cx, 38, calc[m], 'varie', 'm')
    arrow(ax, (cx, 35), (44 + (cx - 44) * 0.4, 17), 'varie')
box(ax, 34, 7, 20, 10, 'resultat', label='56')
save(fig, '52-248')
