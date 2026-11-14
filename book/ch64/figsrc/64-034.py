import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
xs = [3, 24, 45, 66]; w = 17; y = 22; h = 12
for x, l in zip(xs, ['24', '12', '4', '1']):
    box(ax, x, y, w, h, 'sujet', label=l, size='l')
for i in range(3):
    arrow(ax, (xs[i] + w + 0.4, y + h / 2), (xs[i + 1] - 0.4, y + h / 2), 'varie')
    text(ax, (xs[i] + w + xs[i + 1]) / 2, y + h + 3.5, str(i + 1), 'varie', 'm', weight='bold')
brace(ax, xs[0], xs[3] + w, y + h + 8, 'fixe', label='4 termes', down=False)
brace(ax, xs[0] + w / 2, xs[3] + w / 2, y - 3, 'resultat', label='longueur = 3 inclusions', down=True)
save(fig, '64-034')
