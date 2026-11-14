import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, r1, r2 = 30, 30, 12, 24
arrow(ax, (4, cy), (57, cy), 'fixe', lw=0.6); arrow(ax, (cx, 4), (cx, 60), 'fixe', lw=0.6)
ax.add_patch(Circle((cx, cy), r2, ec=COL['limite'], fc='none', lw=0.9, ls='--', zorder=2))
disc(ax, cx, cy, r1, 'sujet')
for x, y, s, dx, dy in [(cx + r1, cy, '1', 2.5, -2.6), (cx - r1, cy, '−1', -2.6, -2.6), (cx, cy + r1, '$i$', 2.6, 2.4)]:
    disc(ax, x, y, 0.9, 'sujet'); text(ax, x + dx, y + dy, s, 'sujet', 's')
text(ax, cx - 6.5, cy - 6.5, r'$\mathbb{T}$', 'sujet', 'l')
a = math.radians(25)
text(ax, 58, 46, 'module 2 : 2 × 2 = 4', 'limite', 's', ha='left')
text(ax, 58, 42.5, 'le produit sort', 'limite', 's', ha='left')
arrow(ax, (57, 44.5), (cx + r2 * math.cos(a) + 0.3, cy + r2 * math.sin(a)), 'limite', lw=0.7)
text(ax, 58, 24, 'module 1 : 1 × 1 = 1', 'resultat', 's', ha='left')
text(ax, 58, 20.5, 'le produit reste', 'resultat', 's', ha='left')
arrow(ax, (57, 22.5), (cx + r1 * math.cos(-0.4) + 0.3, cy + r1 * math.sin(-0.4)), 'resultat', lw=0.7)
save(fig, '46-139')
