import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role, label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(100)
cx, cy, u = 44, 50, 13
text(ax, 44, 94, r'$a^2+b^2=1$', 'sujet', 'l')
line(ax, [(cx - 30, cy), (cx + 30, cy)], 'fixe'); line(ax, [(cx, cy - 30), (cx, cy + 30)], 'fixe')
text(ax, cx + 33, cy, r'$a$', 'fixe', 's'); text(ax, cx, cy + 33, r'$b$', 'fixe', 's')
import math
t = [math.radians(a) for a in range(0, 361, 5)]
line(ax, [(cx + u * math.cos(a), cy + u * math.sin(a)) for a in t], 'sujet', dash=True)
bad = {(1, 1): 'carrés : 2', (2, 0): 'carrés : 4'}
for a in range(-2, 3):
    for b in range(-2, 3):
        if (a, b) in [(1, 0), (-1, 0), (0, 1), (0, -1)]: continue
        role = 'limite' if (a, b) in bad else 'fixe'
        disc(ax, cx + a * u, cy + b * u, 1.4, role)
for (a, b), s, dx, dy in (((1, 0), '1', 3.5, -3.5), ((-1, 0), r'$-1$', -4, -3.5), ((0, 1), r'$i$', 3.5, 3.5), ((0, -1), r'$-i$', 4, -3.5)):
    disc(ax, cx + a * u, cy + b * u, 2.0, 'resultat')
    text(ax, cx + a * u + dx, cy + b * u + dy, s, 'resultat', 'm')
text(ax, cx + u + 1, cy + u + 5, 'carrés : 2', 'limite', 's')
text(ax, cx + 2 * u, cy + 5, 'carrés : 4', 'limite', 's')
save(fig, '51-261')
