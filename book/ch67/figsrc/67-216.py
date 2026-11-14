import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$x^5-4x+2$', 'encre', 'm')
xs = [28 + 9 * i for i in range(5)]
r = 2.8
def dots(y, roles):
    for x, ro in zip(xs, roles):
        disc(ax, x, y, r, ro)
def chain(y, idx):
    for i in idx:
        arrow(ax, (xs[i] + r + 0.4, y), (xs[i + 1] - r - 0.4, y), 'varie')
# modulo 3 : 5-cycle
y1 = 56
text(ax, 2, y1 + 2, 'modulo 3', 'encre', 's', ha='left')
text(ax, 2, y1 - 4, r'$x^5-x-1$', 'encre', 's', ha='left')
dots(y1, ['sujet'] * 5); chain(y1, range(4))
arrow(ax, (xs[4], y1 + r + 0.3), (xs[0], y1 + r + 0.3), 'varie', curve=0.3)
text(ax, 70, y1, '5-cycle', 'varie', 's', ha='left')
# modulo 7 : sigma de type (2)(3)
y2 = 34
text(ax, 2, y2 + 2, 'modulo 7', 'encre', 's', ha='left')
text(ax, 2, y2 - 4, r'$\sigma$', 'encre', 's', ha='left')
dots(y2, ['autre', 'autre', 'sujet', 'sujet', 'sujet'])
arrow(ax, (xs[0] + 0.5, y2 + r + 0.3), (xs[1] - 0.5, y2 + r + 0.3), 'varie', both=True, curve=-0.7)
chain(y2, [2, 3])
arrow(ax, (xs[4], y2 + r + 0.3), (xs[2], y2 + r + 0.3), 'varie', curve=0.5)
text(ax, 70, y2, '(2)(3)', 'varie', 's', ha='left')
# sigma puissance 3
y3 = 12
text(ax, 2, y3, r'$\sigma^3$', 'encre', 's', ha='left')
dots(y3, ['autre', 'autre', 'fixe', 'fixe', 'fixe'])
arrow(ax, (xs[0] + 0.5, y3 + r + 0.3), (xs[1] - 0.5, y3 + r + 0.3), 'varie', both=True, curve=-0.7)
text(ax, 70, y3, 'transposition', 'resultat', 's', ha='left')
save(fig, '67-216')
