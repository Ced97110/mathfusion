import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
cx, cy, u = 40, 42, 10.5
R = 10 ** 0.5
ax.add_patch(Circle((cx, cy), R * u, ec=COL['sujet'], fc=FILL['sujet'], lw=1.0, alpha=0.45, zorder=1))
arrow(ax, (cx - 36, cy), (cx + 38, cy), 'fixe', lw=0.7)
arrow(ax, (cx, cy - 36), (cx, cy + 38), 'fixe', lw=0.7)
text(ax, cx + 42, cy, r'$x$', 'fixe', 's'); text(ax, cx + 3, cy + 40, r'$y$', 'fixe', 's')
line(ax, [(cx - 34, cy - 34), (cx + 34, cy + 34)], 'resultat', lw=1.0, dash=True)
text(ax, cx + 30, cy + 38, r'$y=x$', 'resultat', 's')
P = (cx + 1 * u, cy + 3 * u); Q = (cx + 3 * u, cy + 1 * u)
arrow(ax, (P[0] + 2, P[1] - 2), (Q[0] - 2, Q[1] + 2), 'varie', both=True)
for pt in (P, Q):
    disc(ax, pt[0], pt[1], 1.7, 'varie')
text(ax, P[0] + 9, P[1] + 4, r'$P(1,\,3)$', 'varie', 's')
text(ax, Q[0] + 9, Q[1] - 3, r'$Q(3,\,1)$', 'varie', 's')
text(ax, cx - 22, cy - 28, r'$x^2+y^2=10$', 'sujet', 'm')
save(fig, '55-064')
