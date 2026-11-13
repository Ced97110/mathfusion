import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(66)
cx, cy, r = 44, 33, 21
ax.add_patch(Circle((cx, cy), r, ec=COL['sujet'], fc=FILL['sujet'], lw=1.4, zorder=2))
for k, ang in enumerate((0, 90, 180, 270)):
    px, py = cx + r * math.cos(math.radians(ang)), cy + r * math.sin(math.radians(ang))
    ax.add_patch(Circle((px, py), 1.3, ec=COL['resultat' if ang == 180 else 'sujet'], fc=COL['resultat' if ang == 180 else 'sujet'], zorder=4))
text(ax, cx + r + 3, cy + 2.5, '0° = 0', 'sujet', 's', ha='left')
text(ax, cx + r + 3, cy - 2.5, r'360° = 2$\pi$', 'sujet', 's', ha='left')
text(ax, cx, cy + r + 4, r'90° = $\pi$/2', 'sujet', 's')
text(ax, cx - r - 3, cy, r'180° = $\pi$', 'resultat', 's', ha='right', weight='bold')
text(ax, cx, cy - r - 4, r'270° = 3$\pi$/2', 'sujet', 's')
text(ax, cx, cy, 'degrés = radians', 'fixe', 's')
save(fig, '29-062')
