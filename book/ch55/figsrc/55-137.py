import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
assert 2 * 2 * 3 == 12
# integers: 12 = 2 x 2 x 3 ; polynomials: x^2 - 1 = (x - 1)(x + 1)
text(ax, 21, 68, 'entier', 'autre', 'm', weight='bold')
text(ax, 65, 68, 'polynôme', 'sujet', 'm', weight='bold')
line(ax, [(44, 16), (44, 66)], 'fixe', dash=True)
box(ax, 11, 50, 20, 9, 'autre', label='12', size='m')
for cx, v in ((9, 2), (21, 2), (33, 3)):
    line(ax, [(21, 50), (cx, 38)], 'fixe')
    disc(ax, cx, 34, 4, 'autre', label=str(v), size='m')
box(ax, 50, 50, 30, 9, 'sujet', label=r'$x^2-1$', size='m')
for cx, lab in ((57, r'$x-1$'), (73, r'$x+1$')):
    line(ax, [(65, 50), (cx, 38)], 'fixe')
    box(ax, cx - 8, 30, 16, 8, 'sujet', label=lab, size='s')
text(ax, 21, 22, 'premiers : plus rien', 'fixe', 's')
text(ax, 21, 17.5, 'à décomposer', 'fixe', 's')
text(ax, 65, 22, 'irréductibles : plus rien', 'fixe', 's')
text(ax, 65, 17.5, 'à décomposer', 'fixe', 's')
box(ax, 8, 4, 72, 9, 'resultat', label='une seule décomposition possible', size='s')
save(fig, '55-137')
