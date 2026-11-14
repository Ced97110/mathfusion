import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 53, '7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040', 'encre', 'm', weight='bold')
x0, cw, y, h = 6.5, 2.5, 28, 10
for i in range(30):
    if i == 0:
        ax.add_patch(Rectangle((x0, y), cw, h, fc=COL['resultat'], ec=FILL['encre'], lw=0.4, zorder=2))
    else:
        ax.add_patch(Rectangle((x0 + i * cw, y), cw, h, fc=FILL['fixe'], ec=FILL['encre'], lw=0.4, zorder=2))
ax.add_patch(Rectangle((x0, y), 30 * cw, h, fc='none', ec=COL['fixe'], lw=0.8, zorder=3))
brace(ax, x0, x0 + 30 * cw, y + h + 0.5, 'fixe', 'les 5040 permutations', down=False)
text(ax, 83, 22.5, 'une case = 168 permutations', 'fixe', 's', ha='right')
arrow(ax, (14, 15.5), (x0 + cw / 2, y - 0.8), 'resultat')
text(ax, 15, 12, 'celles qui laissent le code stable : 168', 'resultat', 's', ha='left')
text(ax, 44, 4.5, r'$(8-1)(8-2)(8-4) = 168$', 'resultat', 'm', weight='bold')
save(fig, '68-218')
