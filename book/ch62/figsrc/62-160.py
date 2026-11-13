import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(90)
text(ax, 44, 84, r'$x^p-1$ : le corps a pour degré $p-1$', 'encre', 'm')
def polygon(cx, cy, r, n, role):
    pts = [(cx + r * math.cos(math.radians(90 + 360 * k / n)), cy + r * math.sin(math.radians(90 + 360 * k / n))) for k in range(n)]
    poly(ax, pts, role)
polygon(22, 58, 15, 5, 'sujet')
polygon(66, 58, 15, 7, 'autre')
assert 5 - 1 == 2 * 2 and 7 - 1 == 2 * 3
text(ax, 22, 36, r'$p=5$ côtés', 'sujet', 'm')
text(ax, 66, 36, r'$p=7$ côtés', 'autre', 'm')
text(ax, 22, 30, '5 − 1 = 4', 'sujet', 's')
text(ax, 66, 30, '7 − 1 = 6', 'autre', 's')
box(ax, 2, 6, 40, 16, 'resultat', label='4 = 2 × 2\npuissance de 2', size='s')
box(ax, 46, 6, 40, 16, 'limite', label='6 = 2 × 3\npas une puissance de 2', size='s')
arrow(ax, (22, 26), (22, 23), 'resultat', lw=1.0)
arrow(ax, (66, 26), (66, 23), 'limite', lw=1.0)
save(fig, '62-160')
