import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
cols = [3, 30.5, 58]
for x, ch, role, mean in zip(cols, ['p', '4', 'm'], ['sujet', 'varie', 'resultat'],
        ['maille\nsimple', 'ordre de rotation\nle plus grand', 'miroir\n(mirror)']):
    box(ax, x, 66, 27, 13, role, label=ch, size='xl')
    arrow(ax, (x + 13.5, 66), (x + 13.5, 58), role)
    text(ax, x + 13.5, 52, mean, role, 's')
text(ax, 44, 38, 'on peut changer une lettre :', 'fixe', 's')
box(ax, 3, 16, 27, 13, 'autre', label='c', size='xl')
arrow(ax, (16.5, 29), (16.5, 33.5), 'autre')
text(ax, 16.5, 8, 'maille centrée\n(un point au milieu)', 'autre', 's')
box(ax, 58, 16, 27, 13, 'autre', label='g', size='xl')
arrow(ax, (71.5, 29), (71.5, 33.5), 'autre')
text(ax, 71.5, 8, 'symétrie glissée\n(glide)', 'autre', 's')
save(fig, '74-165')
