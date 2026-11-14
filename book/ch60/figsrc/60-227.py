import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s = 6; x0 = 15; y0 = 26
text(ax, 44, 55, r'$p=3$, partition $2+1$', 'encre', 'm', weight='bold')
for i in range(9):
    for j in range(3):
        ax.add_patch(Rectangle((x0 + i * s, y0 + j * s), s, s, ec=COL['sujet'], fc=FILL['sujet'], lw=0.6, zorder=2))
ax.add_patch(Rectangle((x0, y0), 9 * s, 3 * s, ec=COL['resultat'], fc='none', lw=1.6, zorder=3))
brace(ax, x0, x0 + 9 * s, y0, 'sujet', label=r'$\mathbb{Z}/9$ : 9 éléments')
text(ax, 78, y0 + 1.5 * s, r'$\mathbb{Z}/3$' + '\n3 éléments', 'sujet', 's')
text(ax, 44, 8, r'$9\times3=27=3^3$', 'resultat', 'l', weight='bold')
save(fig, '60-227')
