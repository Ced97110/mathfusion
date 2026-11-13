import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
xs = [44, 58, 72]
rows = [(56, ['2', '3', '4'], ['sujet', 'fixe', 'sujet'], 'départ'),
        (32, ['4', '3', '2'], ['varie', 'fixe', 'varie'], r'après $\tau$'),
        (8, ['2', '3', '4'], ['resultat', 'resultat', 'resultat'], r'après $\tau$ encore')]
for y, labs, roles, name in rows:
    text(ax, 2, y + 4.5, name, 'encre', 's', ha='left')
    for x, l, r in zip(xs, labs, roles):
        box(ax, x - 5, y, 10, 9, r, label=l, size='l')
for y in (56, 32):
    arrow(ax, (58, y - 1), (58, y - 14), 'varie')
    text(ax, 62, y - 7.5, r'$\tau$', 'varie', 'm', ha='left')
save(fig, '46-194')
