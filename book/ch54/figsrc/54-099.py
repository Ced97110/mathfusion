import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
base = [1, 2, 3]
res = [5 * v for v in base]
assert res == [5, 10, 15]
box(ax, 4, 52, 12, 9, 'sujet', label='5', size='m')
arrow(ax, (18, 56.5), (28, 56.5), 'fixe', both=True)
text(ax, 23, 60.5, 'identifié', 'fixe', 's')
box(ax, 30, 52, 40, 9, 'sujet', label=r'$(5,0,0,\ldots)$', size='m')
cw, x0 = 14, 30
text(ax, 14, 37, 'avant', 'autre', 's')
text(ax, 14, 11, 'après', 'resultat', 's')
for i, v in enumerate(base):
    box(ax, x0 + i * cw, 33, cw - 1, 8, 'autre', label=str(v), size='m')
    arrow(ax, (x0 + i * cw + 6.5, 32.5), (x0 + i * cw + 6.5, 20.5), 'varie')
    box(ax, x0 + i * cw, 12, cw - 1, 8, 'resultat', label=str(res[i]), size='m')
text(ax, 77, 26.5, r'$\times\,5$', 'varie', 'l')
text(ax, 44, 4, 'chaque barre est multipliée par 5', 'encre', 's')
save(fig, '54-099')
