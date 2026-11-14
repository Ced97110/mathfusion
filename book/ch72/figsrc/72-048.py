import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
def ax2(ax, cx, cy, r):
    arrow(ax, (cx - r, cy), (cx + r, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy - r), (cx, cy + r), 'fixe', lw=0.6)

cx, cy, s = 40, 38, 18
ax2(ax, cx, cy, 30)
line(ax, [(cx - 24, cy - 24), (cx + 24, cy + 24)], 'fixe', lw=0.8, dash=True)
line(ax, [(cx - 24, cy + 24), (cx + 24, cy - 24)], 'fixe', lw=0.8, dash=True)
arrow(ax, (cx, cy), (cx + s, cy + s), 'sujet', lw=1.6)
arrow(ax, (cx, cy), (cx + s / 2, cy - s / 2), 'autre', lw=1.6)
text(ax, cx + s - 9, cy + s + 3, r'$u$ = (1, 1)', 'sujet', 's')
text(ax, cx + 14, cy - 5, r'$v$ = (0,5 ; $-$0,5)', 'autre', 's', ha='left')
text(ax, 20, 70, r'$B(u, u) = 0$', 'sujet', 's')
text(ax, 62, 70, r'$B(v, v) = 0$', 'autre', 's')
text(ax, 44, 7, r'$B(u, v) = 1$', 'resultat', 'l')
save(fig, '72-048')
