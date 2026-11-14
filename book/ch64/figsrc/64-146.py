import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(80)
cx, cy, Rr = 44, 42, 24
ax.add_patch(Circle((cx, cy), Rr, ec=COL['fixe'], fc='none', lw=0.9, zorder=1))
line(ax, [(cx - Rr - 4, cy), (cx + Rr + 4, cy)], 'fixe', lw=0.5)
line(ax, [(cx, cy - Rr - 4), (cx, cy + Rr + 4)], 'fixe', lw=0.5)
for k in range(4):
    a = math.radians(90 * k)
    p = (cx + Rr * math.cos(a), cy + Rr * math.sin(a))
    line(ax, [(cx, cy), p], 'sujet', lw=0.6, dash=True)
    disc(ax, p[0], p[1], 2.4, 'sujet')
    q = (cx + (Rr + 7.5) * math.cos(a), cy + (Rr + 6) * math.sin(a))
    text(ax, q[0], q[1], f'{90 * k}°', 'sujet', 'm')
ax.add_patch(Arc((cx, cy), 20, 20, theta1=0, theta2=90, ec=COL['varie'], lw=1.3, zorder=4))
text(ax, cx + 13.5, cy + 13.5, 'écart 90°', 'varie', 's')
text(ax, 44, 4, 'n = 4 : cercle de rayon 1', 'encre', 'm')
save(fig, '64-146')
