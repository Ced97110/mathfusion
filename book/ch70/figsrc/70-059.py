import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 28, 48, 'Res', 'sujet', 'xl', weight='bold')
text(ax, 34.6, 45.5, r'$y$', 'varie', 'l', weight='bold')
text(ax, 48, 48, r'$(f,\ g)$', 'autre', 'xl', weight='bold')
for x, xl, role, s in [(28, 16, 'sujet', 'résultant'), (34.6, 44, 'varie', 'inconnue éliminée'), (48, 72, 'autre', 'les deux polynômes')]:
    arrow(ax, (x, 41), (xl, 32), role)
    text(ax, xl, 29, s, role, 's')
box(ax, 2, 6, 38, 9, 'fixe', label=r'$f$ et $g$ contiennent $x$ et $y$', size='s')
arrow(ax, (41, 10.5), (47, 10.5), 'fixe')
box(ax, 48, 6, 38, 9, 'resultat', label=r'reste : polynôme en $x$', size='s')
save(fig, '70-059')
