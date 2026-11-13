import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(88)
cx, cy, R = 44, 44, 30
for n in range(12):
    a = math.radians(90 - 30 * n); x, y = cx + R * math.cos(a), cy + R * math.sin(a)
    if n % 3 == 0 and n % 2 == 0:
        disc(ax, x, y, 4.6, 'autre'); disc(ax, x, y, 3.0, 'sujet', label=str(n), size='s')
    elif n % 3 == 0: disc(ax, x, y, 4.4, 'sujet', label=str(n))
    elif n % 2 == 0: disc(ax, x, y, 4.4, 'autre', label=str(n))
    else: disc(ax, x, y, 4.4, 'varie', label=str(n))
a1 = math.radians(60)
line(ax, [(cx + (R + 5) * math.cos(a1), cy + (R + 5) * math.sin(a1)), (cx + 36 * math.cos(a1), cy + 36 * math.sin(a1))], 'varie', lw=0.6)
text(ax, 63, 77, r'$3 - 2 = 1$', 'varie', 's', ha='left')
text(ax, cx, cy, 'sup : tout G', 'resultat', 'm', weight='bold')
save(fig, '79-075')
