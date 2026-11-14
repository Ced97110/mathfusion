import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(54)
x = 4.0; u = 12.0; y = 28; h = 8
for i in range(6):
    box(ax, x + i * u, y, u, h, 'sujet', label=r'$r$', size='m')
rest = 0.28 * u
box(ax, x + 6 * u, y, rest, h, 'varie', r=0.3)
text(ax, 4, 49, 'cercle de rayon 5 cm, déroulé', 'encre', 's', ha='left')
text(ax, x + 6 * u + rest / 2, 43, 'reste ≈ 1,4 cm', 'varie', 's')
arrow(ax, (x + 6 * u + rest / 2, 41.2), (x + 6 * u + rest / 2, y + h + 0.8), 'varie')
brace(ax, x, x + 6 * u, y - 0.5, 'sujet', label='6 rayons de 5 cm = 30 cm')
text(ax, 44, 10, r'le rayon rentre ≈ 6,28 fois ($2\pi$)', 'resultat', 's')
save(fig, '29-050')
