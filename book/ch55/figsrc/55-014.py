import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
xs = [34, 52, 70]
for i, x in enumerate(xs):
    text(ax, x + 8, 47, f'$s={i}$', 'fixe', 's')
    box(ax, x, 28, 16, 12, 'resultat', label='0')
    box(ax, x, 8, 16, 12, 'resultat', label='0')
box(ax, 4, 28, 26, 12, 'sujet', label=r'$f$ sur l’horloge', size='s')
box(ax, 4, 8, 26, 12, 'autre', label='fonction nulle', size='s')
text(ax, 17, 24, '=', 'resultat', 'l')
save(fig, '55-014')
