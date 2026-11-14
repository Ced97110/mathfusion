import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
rows = [
    ('sujet', r'Départ : (3) ⊆ ($a$), idéal contenant (3)'),
    ('varie', r'dictionnaire : (3) ⊆ ($a$) ⇔ $a$ ∣ 3'),
    ('fixe', r'$a = ±1$ ou $a = ±3$'),
    ('resultat', r'Arrivée : ($a$) = ℤ ou ($a$) = (3)'),
]
ys = [82 - 22 * i for i in range(4)]
for (role, lab), y in zip(rows, ys):
    box(ax, 6, y, 76, 12, role, label=lab, size='s')
for y0, y1 in zip(ys[:-1], ys[1:]):
    arrow(ax, (44, y0), (44, y1 + 12), 'fixe')
save(fig, '56-113')
