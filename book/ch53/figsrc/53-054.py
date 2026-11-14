import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

assert 26 == 5 * 5 + 1 and 1 == 26 - 5 * 5 and -5 + 26 == 21 and 5 * 21 == 105 == 4 * 26 + 1

fig, ax = canvas(84)
ys = [68, 50, 32, 12]
specs = [('sujet', r'$26 = 5 \times 5 + 1$'),
         ('varie', r'$1 = 26 - 5 \times 5$'),
         ('resultat', r'coefficient de 5 : $-5$, et $-5 + 26 = 21$'),
         ('fixe', r'$5 \times 21 = 105 = 4 \times 26 + 1$')]
for y, (role, lab) in zip(ys, specs):
    box(ax, 6, y, 76, 11, role, label=lab)
notes = ['isoler le reste 1', 'lire le coefficient de 5', 'vérifier le résultat']
for i, n in enumerate(notes):
    y_top, y_next = ys[i], ys[i + 1] + 11
    arrow(ax, (20, y_top), (20, y_next), 'fixe')
    text(ax, 25, (y_top + y_next) / 2, n, 'fixe', 's', ha='left')
save(fig, '53-054')
