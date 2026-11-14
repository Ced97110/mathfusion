import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'diviseur $g=2x-1$, degré $m=1$', 'encre', 'm')
y0 = 38  # axe des rangs
u = 8    # mm par unité de coefficient
line(ax, [(14, y0), (74, y0)], 'fixe')
# rang 0 : coefficient -1 (gris) ; rang 1 : coefficient 2 (bleu)
ax.add_patch(Rectangle((22, y0 - 1 * u), 14, 1 * u, ec=COL['fixe'], fc=FILL['fixe'], lw=0.8, zorder=2))
ax.add_patch(Rectangle((50, y0), 14, 2 * u, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
text(ax, 29, y0 + 4, 'rang 0', 'fixe', 's')
text(ax, 57, y0 - 4, 'rang 1', 'sujet', 's')
text(ax, 29, y0 - 1 * u - 4, r'$-1$', 'fixe', 's')
text(ax, 57, y0 + 2 * u + 4, r'$2$', 'sujet', 'm', weight='bold')
text(ax, 44, 12, r'$b_m=b_1=2$ : coefficient du rang $m$', 'sujet', 'm')
text(ax, 44, 5, 'le dernier terme non nul de $g$', 'sujet', 's')
save(fig, '54-151')
