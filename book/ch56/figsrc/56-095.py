import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
rows = [
    ('sujet', r'Départ : ($a$) = ($b$), $a \neq 0$', '(3) = (−3)'),
    ('fixe', r'$a = bx$', r'$3 = (-3)\times(-1)$'),
    ('fixe', r'$b = ay$', r'$-3 = 3\times(-1)$'),
    ('fixe', r'$a = ayx$', r'$3 = 3\times(-1)\times(-1)$'),
    ('varie', r'on barre $a$ ($\neq 0$)', 'on barre 3'),
    ('resultat', r'Arrivée : $xy = 1$', r'$(-1)\times(-1) = 1$'),
]
H, G = 10, 5
ys = [84 - (H + G) * i for i in range(len(rows))]
for (role, left, right), y in zip(rows, ys):
    box(ax, 2, y, 38, H, role, label=left, size='s')
    box(ax, 46, y, 40, H, role, label=right, size='s')
for y0, y1 in zip(ys[:-1], ys[1:]):
    arrow(ax, (21, y0), (21, y1 + H), 'fixe')
    arrow(ax, (66, y0), (66, y1 + H), 'fixe')
save(fig, '56-095')
