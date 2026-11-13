import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(60)
cx, cy, r = 27, 28, 22
A = 57.296
poly(ax, [(cx, cy)] + arc(cx, cy, r, 0, A), 'sujet')
ax.add_patch(Circle((cx, cy), r, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))
line(ax, [(cx, cy), (cx + r, cy)], 'fixe', lw=1.2)
text(ax, cx + r / 2, cy - 3, r'$r$', 'fixe', 's')
line(ax, [(cx, cy), (cx + 27 * math.cos(math.radians(60)), cy + 27 * math.sin(math.radians(60)))], 'fixe', dash=True)
line(ax, [(cx, cy), arc(cx, cy, r, A, A, 1)[0]], 'sujet', lw=1.4)
line(ax, arc(cx, cy, r, 0, A), 'varie', lw=2.4)
text(ax, cx + 27 * math.cos(math.radians(60)) + 3, cy + 27 * math.sin(math.radians(60)) + 2.5, '60°', 'fixe', 's')
text(ax, 57, 52, 'arc = rayon', 'varie', 's', ha='left')
arrow(ax, (56, 50.2), (cx + r * math.cos(math.radians(A / 2)) + 0.8, cy + r * math.sin(math.radians(A / 2)) + 0.8), 'varie')
text(ax, 57, 33, '1 radian', 'sujet', 'm', ha='left')
text(ax, 57, 27, '≈ 57,296°', 'sujet', 'l', ha='left', weight='bold')
text(ax, 57, 19, 'un peu moins que 60°', 'fixe', 's', ha='left')
save(fig, '29-061')
