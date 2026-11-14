import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(76)
tw, th, x0, y0 = 18, 9, 8, 28
for i in range(4):
    for j in range(4):
        x, y = x0 + j * tw, y0 + i * th
        ax.add_patch(Rectangle((x, y), tw, th, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
        ax.add_patch(Circle((x + tw / 2, y + th / 2), 1.4, ec=COL['sujet'], fc=COL['sujet'], zorder=3))
ax.add_patch(Rectangle((x0 - 1.5, y0 - 1.5), 4 * tw + 3, 4 * th + 3, fill=False, ec=COL['resultat'], lw=1.4, zorder=1))
text(ax, 44, 71, r'$\mathbb{F}_2^7$ : 128 mots', 'resultat', 'm')
text(ax, 30, 21, 'boule de rayon 1 : 8 mots', 'sujet', 's')
arrow(ax, (19, 23.5), (15, 28), 'sujet')
text(ax, 44, 12, r'$16 \times 8 = 128$ : aucun mot dehors', 'resultat', 's')
save(fig, '68-151')
