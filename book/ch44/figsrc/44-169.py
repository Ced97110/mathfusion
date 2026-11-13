import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
u = 1.9
x0 = 44 - 20.5 * u
text(ax, 44, 68, r'$5\times 8 = 40$ cases', 'sujet', 'm')
for b in range(3):
    for i in range(13):
        ax.add_patch(Rectangle((x0 + (b * 13 + i) * u, 46), u, 8, ec=COL['fixe'], fc=FILL['fixe'], lw=0.3, zorder=2))
    brace(ax, x0 + b * 13 * u, x0 + (b + 1) * 13 * u, 45, 'fixe', label='13', down=True, depth=1.2)
ax.add_patch(Rectangle((x0 + 39 * u, 46), u, 8, ec=COL['resultat'], fc=FILL['resultat'], lw=0.6, zorder=2))
text(ax, x0 + 39.5 * u, 58.5, 'reste 1', 'resultat', 's')
box(ax, 6, 8, 76, 12, 'varie', label=r'$5\times 8 + 13\times(-3) = 40-39 = 1$', size='s')
text(ax, 44, 28, r'$40 = 3\times 13 + 1$', 'resultat', 's')
save(fig, '44-169')
