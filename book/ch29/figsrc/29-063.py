import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(56)
cx, cy, r = 22, 30, 14
poly(ax, [(cx, cy)] + arc(cx, cy, r, 0, 270), 'resultat')
ax.add_patch(Circle((cx, cy), r, ec=COL['resultat'], fc='none', lw=1.2, zorder=3))
text(ax, cx, 51, '270°', 'resultat', 'l', weight='bold')
text(ax, cx, 10, 'trois quarts de tour', 'resultat', 's')
text(ax, cx, 4.5, r'= 3$\pi$/2 ≈ 4,712', 'resultat', 's')
line(ax, [(44, 4), (44, 52)], 'fixe', dash=True)
n = 0
for i in range(5):
    for j in range(9):
        if n < 43:
            ax.add_patch(Circle((52 + j * 3.8, 44 - i * 3.8), 1.5, ec=COL['limite'], fc=FILL['limite'], lw=0.6, zorder=2))
            n += 1
text(ax, 66, 51, '270 sans °', 'limite', 'l', weight='bold')
text(ax, 66, 10, '≈ 43 tours', 'limite', 's')
text(ax, 66, 4.5, '270 radians, pas 3$\\pi$/2', 'limite', 's')
save(fig, '29-063')
