import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
cx, cy, R = 24, 32, 14
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.7, ls='--', zorder=1))
line(ax, [(cx - R - 4, cy), (cx + R + 4, cy)], 'sujet', lw=1.6)
line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', lw=0.6)
names = [r'$r$', r'$jr$', r'$j^2r$']
for k in range(3):
    a = math.radians(120 * k)
    x, y = cx + R * math.cos(a), cy + R * math.sin(a)
    role = 'sujet' if k == 0 else 'limite'
    disc(ax, x, y, 2, role)
    text(ax, cx + (R + 5.5) * math.cos(a) - (3 if k == 0 else 0), cy + (R + 4) * math.sin(a) + (3.5 if k == 0 else 0), names[k], role, 's')
text(ax, 24, 58, r'$\mathbb{Q}(r)/\mathbb{Q}$', 'sujet', 'm')
box(ax, 50, 38, 36, 16, 'resultat', label='séparable\n(caractéristique 0)', size='s')
box(ax, 50, 10, 36, 16, 'limite', label='pas normale\n(jr, j²r manquent)', size='s')
save(fig, '63-101')
