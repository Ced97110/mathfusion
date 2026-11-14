import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
ax.add_patch(Circle((30, 40), 24, ec=COL['sujet'], fc=FILL['sujet'], lw=0.9, alpha=0.6, zorder=1))
ax.add_patch(Circle((58, 40), 24, ec=COL['autre'], fc=FILL['autre'], lw=0.9, alpha=0.6, zorder=1))
text(ax, 22, 70, 'sans inverse', 'sujet', 's')
text(ax, 66, 70, 'diviseur de zéro', 'autre', 's')
text(ax, 17, 40, '$2$ dans $\\mathbb{Z}$', 'sujet', 's')
for i in range(2):
    for j in range(2):
        on = (i, j) == (0, 0)
        ax.add_patch(Rectangle((40.5 + j * 6, 46 - i * 6), 6, 6, ec=COL['encre'], fc=FILL['sujet'] if on else 'white', lw=0.8, zorder=3))
text(ax, 44, 30, 'ce tableau', 'encre', 's')
text(ax, 44, 8, 'les deux listes se confondent-elles ?', 'fixe', 's')
save(fig, '51-287')
