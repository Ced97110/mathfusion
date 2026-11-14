import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
text(ax, 44, 66, 'f sans racine multiple', 'fixe', 's')
# row 1 : irreducible <-> one orbit
box(ax, 2, 38, 34, 18, 'sujet', label=r'$x^3-2$' + '\nirréductible', size='s')
text(ax, 42, 47, r'$\Leftrightarrow$', 'resultat', 'l')
box(ax, 48, 38, 38, 18, 'resultat', dash=True, fill=False)
for k, x in enumerate((57, 67, 77)):
    disc(ax, x, 47, 3.8, 'resultat', label=r'$r_%d$' % (k + 1), size='s')
text(ax, 67, 33, '1 orbite : transitif', 'resultat', 's')
# row 2 : reducible <-> several orbits
box(ax, 2, 8, 34, 18, 'autre', label=r'$x^3-x$' + '\nse décompose', size='s')
text(ax, 42, 17, r'$\Leftrightarrow$', 'resultat', 'l')
for k, (x, v) in enumerate(((54, '0'), (67, '1'), (80, '−1'))):
    box(ax, x - 6, 11, 12, 12, 'autre', dash=True, fill=False)
    disc(ax, x, 17, 3.6, 'autre', label=v, size='s')
text(ax, 67, 3.5, '3 orbites : pas transitif', 'autre', 's')
save(fig, '65-059')
