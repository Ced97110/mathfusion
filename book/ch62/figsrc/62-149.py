import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(82)
cx, cy, u = 44, 40, 17.0
arrow(ax, (5, cy), (84, cy), 'fixe', lw=0.9)
arrow(ax, (cx, 4), (cx, 79), 'fixe', lw=0.9)
text(ax, 84, cy + 4, 'réel', 'fixe', 's', ha='right')
text(ax, cx + 3, 78, 'imaginaire', 'fixe', 's', ha='left')
r2 = math.sqrt(2)
pts = [(r2, 0, r'$\sqrt{2}$', 'sujet', 0, 5), (-r2, 0, r'$-\sqrt{2}$', 'sujet', 0, 5),
       (0, 2, r'$2i$', 'autre', -5, 0), (0, -2, r'$-2i$', 'autre', -5, 0)]
for a, b, lab, role, dx, dy in pts:
    px, py = cx + a * u, cy + b * u
    disc(ax, px, py, 2.2, role)
    text(ax, px + dx, py + dy, lab, role, 'm', ha='right' if dx < 0 else 'center')
text(ax, 66, 30, r'racines de $x^2-2$', 'sujet', 's')
text(ax, 67, 62, r'racines de $x^2+4$', 'autre', 's')
text(ax, 66, 26, '≈ ±1,41 sur l’axe réel', 'sujet', 's')
save(fig, '62-149')
