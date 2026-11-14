import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
steps = [
    ('sujet', 'racines de $f$ : 1, 2, 3, 4'),
    ('autre', r'$t_1=14,\ t_2=11,\ t_3=10$'),
    ('resultat', r'$g(x)=(x-14)(x-11)(x-10)$'),
    ('resultat', r'$x^3-35x^2+404x-1540$'),
]
y = 66
for i, (role, lab) in enumerate(steps):
    box(ax, 9, y, 70, 10, role, label=lab, size='s')
    if i < 3:
        arrow(ax, (44, y), (44, y - 6), 'varie')
    y -= 17
text(ax, 44, 3, r'$g$ : degré 3, coefficients dans $F$', 'resultat', 's')
save(fig, '65-087')
