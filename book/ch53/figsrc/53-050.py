import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fa, fn = (2 * 0 + 3) % 26, (2 * 13 + 3) % 26
assert fa == 3 and fn == 3 and 2 * 13 + 3 == 29

fig, ax = canvas(60)
box(ax, 2, 42, 16, 12, 'sujet', label='A\n0')
box(ax, 2, 6, 16, 12, 'autre', label='N\n13')
box(ax, 68, 6, 18, 48, 'limite', label='D\n3', size='l')
arrow(ax, (19, 48), (67, 48), 'varie')
arrow(ax, (19, 12), (67, 12), 'varie')
text(ax, 43, 52, r'$2 \times 0 + 3 = 3$', 'varie', 's')
text(ax, 43, 16, r'$2 \times 13 + 3 = 29$, reste 3', 'varie', 's')
text(ax, 43, 30, r'$a = 2,\ b = 3$', 'encre', 'm')
text(ax, 43, 25, 'deux lettres, même image', 'limite', 's')
save(fig, '53-050')
