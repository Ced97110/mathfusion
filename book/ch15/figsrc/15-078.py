import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 24, 54, 40, 11, 'sujet', label=r'$-7p^{3}$', size='l')
for i, (v, r) in enumerate([(1, '-7'), (2, '-56'), (3, '-189')]):
    y = 36 - i * 14
    box(ax, 6, y, 22, 9, 'varie', label=rf'$p={v}$', size='m')
    arrow(ax, (29, y + 4.5), (52, y + 4.5), 'fixe')
    box(ax, 54, y, 26, 9, 'resultat', label=rf'${r}$', size='m')
arrow(ax, (44, 53), (44, 46), 'sujet')
text(ax, 44, 5, 'une lettre, plusieurs valeurs', 'varie', 's')
save(fig, '15-078')
