import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cw = 27; xs = [2, 30.5, 59]
text(ax, 44, 68, 'critère d’Iwasawa : 3 vérifications', 'encre', 'm')
for x in xs: box(ax, x, 28, cw, 33, 'autre')
c = [x + cw / 2 for x in xs]
# 1 : trois points (droites) et paquets
for k, (dx, dy) in enumerate([(-6, -2), (6, -2), (0, 5)]): disc(ax, c[0] + dx, 48 + dy, 2.2, 'sujet')
arrow(ax, (c[0] - 4, 43.5), (c[0] + 4, 43.5), 'varie', lw=0.8, both=True)
# 2 : deux cercles égaux
disc(ax, c[1], 47, 6, 'sujet', fill=False); disc(ax, c[1], 47, 3.5, 'sujet', fill=True)
# 3 : rangée de transvections
for k in range(4): disc(ax, c[2] - 9 + k * 6, 48, 2, 'varie')
line(ax, [(c[2] - 11, 48), (c[2] + 11, 48)], 'varie', lw=0.6)
text(ax, c[0], 35, 'action primitive\nsur les droites', 'encre', 's')
text(ax, c[1], 35, 'égal à son\ngroupe dérivé', 'encre', 's')
text(ax, c[2], 35, 'transvections\nd’une direction', 'encre', 's')
for x in c: arrow(ax, (x, 27), (44 + (x - 44) * 0.3, 17), 'resultat', lw=1.0)
box(ax, 20, 3, 48, 13, 'resultat', label=r'$PSp_{2n}(F)$ est simple', size='s')
save(fig, '75-090')
