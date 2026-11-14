import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s = 3.2; gx, gy = 5, 14
for i in range(8):
    for j in range(8):
        hot = (i, j) == (2, 5)
        ax.add_patch(Rectangle((gx + i * s, gy + j * s), s, s, ec=COL['sujet'], fc=FILL['varie'] if hot else FILL['sujet'], lw=0.5, zorder=2))
text(ax, gx + 4 * s, gy + 8 * s + 5, r'$G \times G$', 'sujet', 'm')
text(ax, gx + 4 * s, 7, '64 couples', 'sujet', 's')
for k in range(8):
    disc(ax, 56 + (k % 4) * 8, 36 - (k // 4) * 9 + 4, 3.2, 'resultat', fill=True)
disc(ax, 56 + 2 * 8, 40, 3.2, 'varie')
text(ax, 72, 54, r'$G$', 'resultat', 'm')
text(ax, 72, 25, '8 mouvements', 'resultat', 's')
arrow(ax, (gx + 2.5 * s + 1.6, gy + 5.5 * s), (68, 40), 'varie', curve=-0.2)
text(ax, 44, 61, 'un couple, un seul produit', 'varie', 's')
save(fig, '44-106')
