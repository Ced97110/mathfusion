import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
def ax2(ax, cx, cy, r):
    arrow(ax, (cx - r, cy), (cx + r, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy - r), (cx, cy + r), 'fixe', lw=0.6)

cx, cy, s = 44, 40, 18
ax2(ax, cx, cy, 26)
arrow(ax, (cx, cy), (cx + s, cy + s), 'limite', lw=1.4)
arrow(ax, (cx, cy), (cx + s, cy), 'sujet', lw=1.4)
disc(ax, cx, cy, 1.3, 'fixe')
text(ax, cx + s + 2, cy + s + 3, 'isotrope : carré 0', 'limite', 's', ha='center')
text(ax, cx + s + 3, cy - 5, 'carré 1', 'sujet', 's')
text(ax, cx - 14, cy + 6, 'vecteur nul', 'fixe', 's')
text(ax, 44, 6, r'$u \neq 0$ et $B(u, u) = 0$', 'limite', 'm')
save(fig, '72-035')
