import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(52)
cx, cy, r = 27, 26, 20
line(ax, [(cx - r, cy), (cx + r, cy)], 'fixe', dash=True)
line(ax, arc(cx, cy, r, 0, 180), 'sujet', lw=2.0)
line(ax, arc(cx, cy, r, 180, 360), 'autre', lw=2.0)
text(ax, cx, cy + 8, r'$\pi$', 'sujet', 'l')
text(ax, cx, cy - 8, r'$\pi$', 'autre', 'l')
text(ax, 50, cy + 14, r'demi-tour : 180° = $\pi$', 'sujet', 's', ha='left')
text(ax, 50, cy - 14, r'demi-tour : 180° = $\pi$', 'autre', 's', ha='left')
text(ax, 50, cy, r'tour : 360° = 2$\pi$', 'resultat', 's', ha='left', weight='bold')
save(fig, '29-049')
