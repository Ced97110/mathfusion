import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def ax2(ax, cx, cy, r):
    arrow(ax, (cx - r, cy), (cx + r, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy - r), (cx, cy + r), 'fixe', lw=0.6)

cx, cy, s = 40, 38, 8
ax2(ax, cx, cy, 30)
line(ax, [(cx - 28, cy - 28), (cx + 28, cy + 28)], 'limite', lw=1.4)
arrow(ax, (cx, cy), (cx + s, cy + s), 'limite', lw=1.2)
arrow(ax, (cx, cy), (cx + 3 * s, cy + 3 * s), 'limite', lw=1.2)
text(ax, cx + s - 6, cy + s + 3, '(1, 1)', 'limite', 's')
text(ax, cx + 3 * s - 7, cy + 3 * s + 3, '(3, 3)', 'limite', 's')
text(ax, 72, 66, r'$U$', 'limite', 'l')
text(ax, 68, 22, r'$1 \times 3 - 1 \times 3 = 0$', 'limite', 's')
text(ax, 68, 15, r'$U \subseteq U^\perp$', 'limite', 'm')
text(ax, 44, 5, 'tous les nombres entre vecteurs de U : 0', 'fixe', 's')
save(fig, '72-037')
