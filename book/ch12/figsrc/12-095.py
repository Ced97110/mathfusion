import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(84)
box(ax, 2, 32, 84, 50, 'sujet'); text(ax, 44, 77, 'réels ℝ', 'sujet', 'm', weight='bold')
disc(ax, 12, 64, 5, 'sujet', label='5', size='l'); disc(ax, 30, 64, 5, 'autre', label='2', size='l')
text(ax, 42, 70, '5 ÷ 2', 'varie', 's')
arrow(ax, (37, 64), (53, 64), 'resultat')
box(ax, 55, 57, 26, 14, 'resultat', label='5/2 : un réel', size='s')
disc(ax, 12, 42, 5, 'sujet', label='5', size='l'); disc(ax, 30, 42, 5, 'autre', label='0', size='l')
arrow(ax, (36, 38), (56, 17), 'limite')
text(ax, 45, 48, '5 ÷ 0', 'varie', 's')
box(ax, 55, 6, 30, 16, 'limite', dash=True, label='5/0 : pas un réel', size='s')
save(fig, '12-095')
