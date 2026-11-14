import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(40)
y0 = 14
for cx, r, k in [(22, 9, 3), (62, 15, 5)]:
    line(ax, [(cx - r, y0), (cx + r, y0)], 'fixe')
    line(ax, arc(cx, y0, r, 0, 180), 'sujet', lw=1.8)
    line(ax, [(cx, y0), (cx + r, y0)], 'varie', lw=1.8)
    text(ax, cx, y0 + 3.5, '180°', 'sujet', 's')
    text(ax, cx + r / 2 + 2, y0 - 3, f'rayon {k} cm', 'varie', 's')
    text(ax, cx, y0 + r + 3, rf'arc {k}$\pi$', 'sujet', 's')
    text(ax, cx, 4.5, r'arc ÷ rayon = $\pi$', 'resultat', 's')
save(fig, '29-048')
