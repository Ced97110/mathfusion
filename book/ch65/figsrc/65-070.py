import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
steps = [
    ('sujet', r'$x^3 - 3x + 1$'),
    ('resultat', r'$d = 108 - 27 = 81 = 9^2$'),
    ('fixe', r'seules racines possibles : $1$ et $-1$'),
    ('fixe', r'$f(1) = -1$ et $f(-1) = 3$'),
    ('resultat', r'$G_f = A_3$'),
]
y = 76
for i, (role, lab) in enumerate(steps):
    box(ax, 9, y, 70, 9, role, label=lab, size='s' if i not in (0, 4) else 'l')
    if i < len(steps) - 1:
        arrow(ax, (44, y), (44, y - 5), 'varie')
    y -= 14
text(ax, 44, 12, 'ni 1 ni −1 : irréductible', 'fixe', 's')
save(fig, '65-070')
