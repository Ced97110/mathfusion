import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 80, r'$n=5$, $p=2$ : modulo 2', 'sujet', 'm')
steps = [
    ('sujet', r'$x^5-1$ devient $x^5+1$'),
    ('varie', r'dérivée : $5x^4\equiv x^4$'),
    ('fixe', r'$x^4$ : seule racine 0'),
    ('limite', r'$x^5+1$ en 0 vaut 1, pas 0'),
]
for i, (role, lab) in enumerate(steps):
    y = 62 - i * 17
    box(ax, 10, y, 68, 11, role, label=lab)
    if i < 3: arrow(ax, (44, y), (44, y - 6), 'fixe')
text(ax, 44, 5, 'pas de racine double : contradiction', 'limite', 's')
save(fig, '66-057')
