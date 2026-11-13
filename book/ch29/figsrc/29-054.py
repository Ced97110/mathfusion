import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(66)
text(ax, 44, 60, r'même facteur $\pi$/180 ≈ 0,01745', 'fixe', 's')
for yc, a, b in [(46, '90°', r'$\pi$/2'), (30, '45°', r'$\pi$/4'), (14, '10°', r'$\pi$/18')]:
    box(ax, 4, yc - 5, 20, 10, 'sujet', label=a)
    arrow(ax, (25, yc), (60, yc), 'varie')
    text(ax, 42.5, yc + 3.2, r'$\times\ \pi$/180', 'varie', 's')
    box(ax, 62, yc - 5, 22, 10, 'resultat', label=b)
save(fig, '29-054')
