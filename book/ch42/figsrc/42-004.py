import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
ox, oy, ux, uy = 8, 10, 8, 4.5
P = lambda x, y: (ox + x * ux, oy + y * uy)
arrow(ax, P(0, 0), (ox + 4.9 * ux, oy), 'fixe', lw=0.7); arrow(ax, P(0, 0), (ox, oy + 9.9 * uy), 'fixe', lw=0.7)
text(ax, ox + 4.9 * ux + 2, oy - 2.5, '$x$', 'fixe', 's'); text(ax, ox - 3, oy + 9.9 * uy, '$y$', 'fixe', 's')
line(ax, [P(0, 1), P(4, 9)], 'sujet', lw=1.4)
line(ax, [P(3, 0), P(3, 9.5)], 'varie', dash=True)
disc(ax, *P(3, 7), 1.3, 'resultat')
text(ax, P(3, 7)[0] + 3, P(3, 7)[1] - 3.5, '(3, 7)', 'resultat', 's', ha='left')
text(ax, 24, 63, 'droite : 1 seul point', 'resultat', 's', weight='bold')
cx, cy, r = 66, 30, 18
ux2 = r / 5
arrow(ax, (cx - r - 2, cy), (cx + r + 3, cy), 'fixe', lw=0.7); arrow(ax, (cx, cy - r - 2), (cx, cy + r + 3), 'fixe', lw=0.7)
ax.add_patch(Circle((cx, cy), r, ec=COL['autre'], fc='none', lw=1.4, zorder=2))
x3 = cx + 3 * ux2
line(ax, [(x3, cy - r - 1), (x3, cy + r + 1)], 'varie', dash=True)
disc(ax, x3, cy + 4 * ux2, 1.3, 'limite'); disc(ax, x3, cy - 4 * ux2, 1.3, 'limite')
text(ax, x3 + 2.5, cy + 4 * ux2 + 2.5, '(3, 4)', 'limite', 's', ha='left')
text(ax, x3 + 2.5, cy - 4 * ux2 - 2.5, '(3, −4)', 'limite', 's', ha='left')
text(ax, 66, 63, 'cercle : 2 points', 'limite', 's', weight='bold')
save(fig, '42-004')
