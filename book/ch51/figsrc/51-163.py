import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 29, 57, 'se défait', 'resultat', 'm')
text(ax, 73, 57, 'ne se défait pas', 'limite', 'm')
# etirement
line(ax, [(6, 44), (14, 44)], 'sujet', lw=2.0)
line(ax, [(6, 28), (22, 28)], 'varie', lw=2.0)
arrow(ax, (9, 41), (9, 31), 'varie')
text(ax, 12, 36, r'$\times 2$', 'varie', 's', ha='left')
arrow(ax, (19, 31), (19, 41), 'resultat')
text(ax, 22, 36, r'$\div 2$', 'resultat', 's', ha='left')
text(ax, 15, 18, 'étirement', 'encre', 's')
# quart de tour
c = (46, 36)
for p in [(c[0] + 10, c[1]), (c[0], c[1] + 10)]:
    line(ax, [c, p], 'fixe', lw=0.6, dash=True)
disc(ax, c[0] + 10, c[1], 1.6, 'sujet')
disc(ax, c[0], c[1] + 10, 1.6, 'varie')
arrow(ax, (c[0] + 10 - 0.5, c[1] + 2), (c[0] + 2, c[1] + 10 - 0.5), 'varie', curve=0.35)
arrow(ax, (c[0] + 2, c[1] + 8.5), (c[0] + 8.5, c[1] + 2), 'resultat', curve=0.35)
text(ax, 46, 18, 'quart de tour', 'encre', 's')
# tableau nul
ys = [46, 36, 26]
for y in ys:
    disc(ax, 66, y, 1.6, 'sujet')
    arrow(ax, (68, y), (79.5, 36 + (y - 36) * 0.15), 'limite', lw=0.8)
disc(ax, 82, 36, 2.0, 'limite')
text(ax, 73, 18, 'tableau nul', 'encre', 's')
text(ax, 73, 12, 'tout va au même point', 'limite', 's')
save(fig, '51-163')
