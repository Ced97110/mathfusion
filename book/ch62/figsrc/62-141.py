import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, 'où chercher un irréductible', 'encre', 'm')
text(ax, 44, 69.5, 'à racine multiple ?', 'encre', 'm')
rows = [(48, 'fixe', 'caractéristique 0', 'limite', 'parfait :\naucun exemple'),
        (28, 'fixe', 'corps fini', 'limite', 'parfait :\naucun exemple'),
        (4, 'sujet', 'infini, de\ncaractéristique p,\nnon parfait', 'resultat', 'exemple\npossible')]
for y, r1, l1, r2, l2 in rows:
    h = 16 if y == 4 else 14
    box(ax, 2, y, 42, h, r1, label=l1, size='s')
    arrow(ax, (45, y + h / 2), (52, y + h / 2), r2, lw=1.2)
    box(ax, 53, y, 33, h, r2, label=l2, size='s')
save(fig, '62-141')
