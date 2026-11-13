import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
u = 10.0
text(ax, 44, 90, 'on compare d’abord les entiers', 'encre', 'm')
for y, n, r, lab in ((78, 2, 'sujet', r'$2\ \frac{5}{3}$'), (64, 3, 'autre', r'$3\ \frac{1}{4}$')):
    text(ax, 11, y, lab, r, 'm')
    for i in range(n):
        ax.add_patch(Rectangle((26 + i * u, y - 4), u, 8, ec=COL[r], fc=FILL[r], lw=0.9, zorder=2))
text(ax, 44, 52, 'entiers : 2 < 3', 'resultat', 'm')
line(ax, [(6, 45), (82, 45)], 'fixe', lw=0.6, dash=True)
text(ax, 44, 38, r'mais $\frac{5}{3}>1$ : le test trompe', 'limite', 'm')
w1, w2 = 44 / 12 * 16, 39 / 12 * 16
ax.add_patch(Rectangle((8, 23), w1, 6, ec=COL['sujet'], fc=FILL['sujet'], lw=0.9, zorder=2))
ax.add_patch(Rectangle((8, 11), w2, 6, ec=COL['autre'], fc=FILL['autre'], lw=0.9, zorder=2))
text(ax, 8 + w1 + 2, 26, r'$\frac{44}{12}$', 'sujet', 's', ha='left')
text(ax, 8 + w2 + 2, 14, r'$\frac{39}{12}$', 'autre', 's', ha='left')
save(fig, '07-061')
