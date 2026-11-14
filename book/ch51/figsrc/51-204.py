import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
import math
cx, cy, R = 24, 34, 15
P = lambda k: (cx + R*math.sin(math.radians(72*k)), cy + R*math.cos(math.radians(72*k)))
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.8, zorder=1))
for k in range(5):
    x, y = P(k)
    role = 'sujet' if k == 2 else ('autre' if k == 3 else 'fixe')
    disc(ax, x, y, 3.4, role, label=str(k), size='s')
p2, p3 = P(2), P(3)
line(ax, [(p2[0] - 3.8, p2[1]), (p3[0] + 3.8, p3[1])], 'varie', lw=1.2, dash=True)
text(ax, cx, 8, 'cadran à 5 h', 'fixe', 's')
text(ax, 24, 56, r'$2+3=0$ : opposés', 'varie', 's')
text(ax, 66, 48, r'$(-2)(-3)=3\cdot 2=1$', 'sujet', 's')
text(ax, 66, 38, r'$2\cdot 3=1$', 'autre', 's')
text(ax, 66, 28, 'égaux ✓', 'resultat', 'm', weight='bold')
text(ax, 66, 18, 'sans l’avoir posée', 'fixe', 's')
save(fig, '51-204')
