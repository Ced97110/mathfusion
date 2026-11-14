import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
xs = [34 + 9 * i for i in range(6)]
r = 3.0
text(ax, 44, 84, 'factoriser modulo 2, 3, 5', 'encre', 'm')
def chain(y, a, b):
    for i in range(a, b):
        arrow(ax, (xs[i] + r + 0.4, y), (xs[i + 1] - r - 0.4, y), 'varie')
# modulo 2 : 6-cycle
y1 = 66
text(ax, 2, y1 + 2, 'modulo 2', 'encre', 's', ha='left')
text(ax, 2, y1 - 4, '6-cycle', 'varie', 's', ha='left')
for x in xs: disc(ax, x, y1, r, 'sujet')
chain(y1, 0, 5)
arrow(ax, (xs[5], y1 + r + 0.3), (xs[0], y1 + r + 0.3), 'varie', curve=0.3)
# modulo 3 : 1 + 5
y2 = 46
text(ax, 2, y2 + 2, 'modulo 3', 'encre', 's', ha='left')
text(ax, 2, y2 - 4, '1 + 5', 'varie', 's', ha='left')
for i, x in enumerate(xs): disc(ax, x, y2, r, 'fixe' if i == 0 else 'sujet')
chain(y2, 1, 5)
arrow(ax, (xs[5], y2 + r + 0.3), (xs[1], y2 + r + 0.3), 'varie', curve=0.4)
# modulo 5 : 2 + 1 + 1 + 1 + 1
y3 = 28
text(ax, 2, y3 + 2, 'modulo 5', 'encre', 's', ha='left')
text(ax, 2, y3 - 4, '2 + 1×4', 'varie', 's', ha='left')
for i, x in enumerate(xs): disc(ax, x, y3, r, 'sujet' if i < 2 else 'fixe')
arrow(ax, (xs[0] + 0.5, y3 + r + 0.3), (xs[1] - 0.5, y3 + r + 0.3), 'varie', both=True, curve=-0.7)
box(ax, 8, 6, 72, 11, 'resultat', label=r'3 réductions $\Rightarrow$ $G_f=S_6$')
save(fig, '67-234')
