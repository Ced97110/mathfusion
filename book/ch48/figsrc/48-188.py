import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(80)
c, r = (28, 40), 20
pos = {}
for k in range(12):
    a = math.pi / 2 - 2 * math.pi * k / 12; x, y = c[0] + r * math.cos(a), c[1] + r * math.sin(a); pos[k] = (x, y)
    on = k % 3 == 0
    disc(ax, x, y, 2.8 if on else 1.3, 'sujet' if on else 'fixe', label=str(k) if on else None, size='s')
for k in (0, 3, 6, 9):
    a0 = math.pi / 2 - 2 * math.pi * (k + 0.8) / 12; a1 = math.pi / 2 - 2 * math.pi * (k + 2.2) / 12
    arrow(ax, (c[0] + (r + 0) * math.cos(a0), c[1] + r * math.sin(a0)), (c[0] + r * math.cos(a1), c[1] + r * math.sin(a1)), 'varie', curve=-0.25)
text(ax, 28, 40, 'ajouter 3', 'varie', 's'); text(ax, 28, 35, 'ordre 4', 'sujet', 's')
text(ax, 68, 70, 'revient à 0 pour n =', 'varie', 's')
for i, v in enumerate((4, 8, 12)):
    box(ax, 56, 52 - i * 12, 24, 9, 'varie', label=str(v))
text(ax, 68, 14, 'et les suivants :', 'varie', 's'); text(ax, 68, 8, 'multiples de 4', 'varie', 's')
save(fig, '48-188')
