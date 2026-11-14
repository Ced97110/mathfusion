import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(84)
text(ax, 44, 77, r'$8^{81}=8\times8^{40}\times8^{40}$', 'sujet', 'l')
xs = [2, 20, 54]; ws = [12, 28, 28]
def row(y, labs, roles):
    for x, w, lab, r in zip(xs, ws, labs, roles):
        box(ax, x, y, w, 11, r, label=lab)
    text(ax, 17, y + 5.5, '×', 'encre', 'm'); text(ax, 51, y + 5.5, '×', 'encre', 'm')
row(56, ['8', r'$8^{40}$', r'$8^{40}$'], ['sujet', 'varie', 'varie'])
row(26, ['8', '1', '1'], ['sujet', 'resultat', 'resultat'])
arrow(ax, (27, 55.5), (27, 37.5), 'varie'); arrow(ax, (61, 55.5), (61, 37.5), 'varie')
text(ax, 44, 46.5, r'Euler : $8^{40}\equiv1$', 'varie', 's')
arrow(ax, (44, 25.5), (44, 15.5), 'fixe')
box(ax, 30, 4, 28, 11, 'resultat', label=r'$8^{81}\equiv8$')
save(fig, '53-138')
