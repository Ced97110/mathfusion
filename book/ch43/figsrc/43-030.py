import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
parts = [(10, '109', 'sujet', 'un nombre'), (29, r'$\equiv$', 'varie', 'même position'),
         (49, '1', 'sujet', 'un nombre'), (72, r'$(\mathrm{mod}\ 12)$', 'autre', 'horloge à 12')]
for x, big, role, lab in parts:
    text(ax, x, 33, big, role, 'xl')
    line(ax, [(x, 28.5), (x, 24)], role)
    text(ax, x, 20, lab, role, 's')
text(ax, 44, 7, '109 et 1 ne sont pas égaux', 'fixe', 's')
save(fig, '43-030')
