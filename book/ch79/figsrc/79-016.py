import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, 'règle a ≤ b : trois propriétés', 'encre', 'm')
r = 4
text(ax, 3, 50, 'toujours sous lui-même', 'encre', 's', ha='left')
disc(ax, 66, 48, r, 'sujet', label='4', size='s'); arrow(ax, (63.4, 51.2), (68.6, 51.2), 'resultat', curve=-1.6)
text(ax, 3, 34, 'jamais dans les deux sens', 'encre', 's', ha='left')
disc(ax, 56, 34, r, 'sujet', label='4', size='s'); disc(ax, 80, 34, r, 'autre', label='12', size='s')
arrow(ax, (60.5, 34), (75.5, 34), 'resultat'); arrow(ax, (77, 30.5), (59, 30.5), 'limite', curve=-0.4)
text(ax, 68, 23.5, 'non', 'limite', 's')
text(ax, 3, 10, '4 ≤ 12, 12 ≤ 60 : 4 ≤ 60', 'encre', 's', ha='left')
xs = [52, 66, 80]
disc(ax, xs[0], 10, r, 'sujet', label='4', size='s'); disc(ax, xs[1], 10, r, 'autre', label='12', size='s'); disc(ax, xs[2], 10, r, 'resultat', label='60', size='s')
arrow(ax, (xs[0] + 4.5, 10), (xs[1] - 4.5, 10), 'varie'); arrow(ax, (xs[1] + 4.5, 10), (xs[2] - 4.5, 10), 'varie')
arrow(ax, (xs[0] + 1, 14.2), (xs[2] - 1, 14.2), 'resultat', curve=-0.35)
save(fig, '79-016')
