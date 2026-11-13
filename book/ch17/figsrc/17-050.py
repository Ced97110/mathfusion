import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(44)
y = 22
f = numberline(ax, 8, 70, y, -3, 1, arrow_right=False)
arrow(ax, (f(-1) - 1.8, y), (3, y), 'sujet', lw=2.4)
ax.add_patch(Circle((f(-1), y), 1.7, ec=COL['sujet'], fc=COL['sujet'], lw=1.3, zorder=3))
for v, r in [(-2, 'resultat'), (0, 'limite')]:
    ax.add_patch(Circle((f(v), y), 1.1, ec=COL[r], fc=FILL[r], lw=0.9, zorder=3))
text(ax, 44, 40, r'$x \leq -1$', 'sujet', 'xl')
text(ax, 20, 29, 'flèche à gauche', 'sujet', 's')
text(ax, f(-1) + 14, 29, 'point plein en −1', 'sujet', 's')
line(ax, [(f(-1), 24.5), (f(-1) + 6, 27.5)], 'sujet')
for v, s, r in [(-2, 'accepté', 'resultat'), (-1, 'accepté', 'resultat'), (0, 'refusé', 'limite')]:
    text(ax, f(v), 10, s, r, 's')
text(ax, 44, 3.5, 'ou égal : le −1 est accepté', 'fixe', 's')
save(fig, '17-050')
