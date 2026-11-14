import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 63, r'$2^7 \div 8 = 16$', 'resultat', 'l', weight='bold')
x0, cw, y0 = 8.0, 4.5, 14.0
for c in range(16):
    for r in range(8):
        role = 'sujet' if r == 7 else 'varie'
        ax.add_patch(Rectangle((x0 + c * cw, y0 + r * cw), cw, cw, fc=FILL[role], ec=FILL['encre'], lw=0.3, zorder=2))
    ax.add_patch(Rectangle((x0 + c * cw, y0), cw, 8 * cw, fc='none', ec=COL['fixe'], lw=0.7, zorder=3))
brace(ax, x0, x0 + 16 * cw, y0 + 8 * cw + 0.8, 'fixe', '16 boules de 8 mots = 128 mots', down=False)
ax.add_patch(Rectangle((8, 5), 4, 4, fc=FILL['sujet'], ec=COL['sujet'], lw=0.5, zorder=2))
text(ax, 14, 7, 'centre : 1 mot', 'fixe', 's', ha='left')
ax.add_patch(Rectangle((46, 5), 4, 4, fc=FILL['varie'], ec=COL['varie'], lw=0.5, zorder=2))
text(ax, 52, 7, '7 voisins', 'fixe', 's', ha='left')
save(fig, '68-222')
