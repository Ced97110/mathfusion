import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
cols = ['sujet', 'varie', 'resultat', 'limite']
c = 8
for t, x0, role, name in ((0, 7, 'sujet', 'horloge'), (1, 49, 'autre', 'rotations')):
    for i in range(4):
        for j in range(4):
            ax.add_patch(Rectangle((x0 + j * c, 8 + (3 - i) * c), c, c, ec=COL['encre'], fc=FILL[cols[(i + j) % 4]], lw=0.6, zorder=2))
    ax.add_patch(Rectangle((x0, 8), 4 * c, 4 * c, ec=COL[role], fc='none', lw=1.6, zorder=3))
    text(ax, x0 + 16, 46, name, role, 'm')
text(ax, 44, 24, r'$=$', 'resultat', 'xl')
text(ax, 44, 3.5, 'noms effacés : même motif', 'encre', 's')
save(fig, '45-019')
