import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
# top: 4 elements to 4 places, injective so every place is reached ; bottom: doubling on 0, 1, 2 ... leaves 1 and 3 unreached
text(ax, 44, 81, 'corps à 4 éléments : tout est atteint', 'resultat', 's')
xs = [14 + k * 20 for k in range(4)]
for x in xs:
    disc(ax, x, 68, 3.5, 'sujet')
    disc(ax, x, 52, 3.5, 'resultat')
for a, b in [(0, 0), (1, 1), (2, 3), (3, 2)]:
    arrow(ax, (xs[a], 64), (xs[b], 56), 'varie')
line(ax, [(2, 44), (86, 44)], 'fixe', dash=True)
text(ax, 44, 39, 'entiers naturels : on double', 'limite', 's')
for k, v in enumerate([0, 1, 2]):
    box(ax, 4 + (2 * k) * 17, 24, 14, 8, 'sujet', label=str(v), size='s')
    arrow(ax, (11 + 2 * k * 17, 23), (11 + 2 * k * 17, 17), 'varie')
for k in range(5):
    ok = k % 2 == 0
    box(ax, 4 + k * 17, 8, 14, 8, 'resultat' if ok else 'limite', label=str(k), size='s')
text(ax, 44, 3, "1 et 3 : rien n'y arrive", 'limite', 's')
save(fig, '67-089')
