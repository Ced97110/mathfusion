import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
steps = [('sujet', r'écrire $x+y=5$ et $2x+y=8$'), ('varie', r'multiplier par $-1$ : $-x-y=-5$'),
         ('varie', r'additionner : $y$ disparaît'), ('sujet', r'résoudre : $x=3$'),
         ('sujet', r'reporter : $y=2$'), ('resultat', 'vérifier les deux équations')]
for i, (r, lab) in enumerate(steps):
    y = 62 - 11 * i
    disc(ax, 7, y + 4.25, 3.2, r, label=str(i + 1), size='m')
    box(ax, 14, y, 71, 8.5, r, fill=True, label=lab, size='m')
    if i < 5:
        arrow(ax, (7, y + 1.0), (7, y - 11 + 7.5), 'fixe', lw=0.9)
save(fig, '24-058')
