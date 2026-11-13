import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 4, 14, 58, 36, 'sujet', dash=False, r=3)
text(ax, 33, 56, 'ensemble : de 0 à 6 km', 'sujet', 's')
import itertools
for k in range(30):
    x = 8 + (k % 10) * 5.2; y = 38 + (k // 10) * 4.5 - 12
    if k % 3 == 0: ax.add_patch(Circle((x, y + 1), 0.6, ec='none', fc=COL['sujet'], zorder=3))
for lab, x, y in [('0', 12, 40), ('2,5', 26, 28), ('4', 40, 40), ('6', 52, 28)]:
    disc(ax, x, y, 3.2, 'resultat', label=lab, size='s')
disc(ax, 77, 32, 3.2, 'limite', label='7', size='s')
text(ax, 77, 40, 'dehors', 'limite', 's')
text(ax, 33, 8, 'dedans : toute la collection', 'sujet', 's')
save(fig, '17-009')
