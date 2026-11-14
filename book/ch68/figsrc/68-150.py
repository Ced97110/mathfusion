import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(84)
c = 4.2
bw, bh, gap, x0, y0 = 4 * c, 2 * c, 2.2, 7, 30
for bi in range(4):
    for bj in range(4):
        bx = x0 + bj * (bw + gap)
        by = y0 + (3 - bi) * (bh + gap)
        for r in range(2):
            for k in range(4):
                centre = (r == 0 and k == 0)
                ax.add_patch(Rectangle((bx + k * c, by + r * c), c, c, ec=COL['sujet' if centre else 'fixe'],
                                       fc=COL['sujet'] if centre else FILL['fixe'], lw=0.5, zorder=2))
        ax.add_patch(Rectangle((bx, by), bw, bh, fill=False, ec=COL['sujet'], lw=1.0, zorder=3))
gw = 4 * bw + 3 * gap
gh = 4 * bh + 3 * gap
ax.add_patch(Rectangle((x0 - 2, y0 - 2), gw + 4, gh + 4, fill=False, ec=COL['resultat'], lw=1.4, zorder=1))
text(ax, 44, 79, 'boule : 1 centre + 7 voisins', 'sujet', 's')
text(ax, 44, 22, r'$16\times 8 = 128$ mots', 'resultat', 'm')
text(ax, 44, 14, r'$\mathbb{F}_2^7$ : $2^7 = 128$ mots', 'resultat', 'm')
ax.add_patch(Rectangle((14, 3.5), 3, 3, ec=COL['sujet'], fc=COL['sujet'], lw=0.5))
text(ax, 19, 5, 'mot du code', 'encre', 's', ha='left')
ax.add_patch(Rectangle((50, 3.5), 3, 3, ec=COL['fixe'], fc=FILL['fixe'], lw=0.5))
text(ax, 55, 5, 'voisin', 'encre', 's', ha='left')
save(fig, '68-150')
