import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
bx, by, bs = 4, 8, 48
box(ax, bx, by, bs, bs, 'sujet', label=None)
cx, cy = bx + bs / 2, by + bs / 2
ax.add_patch(Circle((cx, cy), 3.2, ec=COL['limite'], fc='white', lw=1.0, zorder=3, ls='--'))
text(ax, bx + 3, by + bs - 4, r'$\mathbb{C}^*$', 'sujet', 'xl', ha='left')
arrow(ax, (cx + 16, cy + 14), (cx + 3, cy + 2.5), 'limite', lw=0.9)
text(ax, cx + 17, cy + 17, r'$0$ exclu', 'limite', 's')
text(ax, 70, 52, r'$\mathbb{C}$ : tous les complexes', 'sujet', 's')
text(ax, 70, 44, r'$*$ : sans $0$', 'limite', 's')
text(ax, 70, 32, r'$z\in\mathbb{C}^*$ : $z\neq 0$', 'sujet')
text(ax, 70, 20, 'multiplier, diviser :', 'resultat', 's')
text(ax, 70, 14, r'on reste dans $\mathbb{C}^*$', 'resultat', 's')
save(fig, '39-130')
