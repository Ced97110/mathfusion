import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 3, 36, 30, 18, 'sujet'); text(ax, 18, 49.5, '4 rotations', 'sujet', 's')
box(ax, 3, 8, 30, 18, 'autre'); text(ax, 18, 21.5, '4 retournements', 'autre', 's')
for k in range(4):
    disc(ax, 8.5 + k*7, 41, 2, 'sujet'); disc(ax, 8.5 + k*7, 13, 2, 'autre')
disc(ax, 72, 45, 7, 'resultat', label='0', size='l'); disc(ax, 72, 17, 7, 'fixe', label='1', size='l')
arrow(ax, (34, 45), (64, 45), 'varie'); arrow(ax, (34, 17), (64, 17), 'varie')
text(ax, 49, 49, r'$f$', 'varie', 'm'); text(ax, 49, 21, r'$f$', 'varie', 'm')
text(ax, 72, 55, 'noyau', 'resultat', 's', weight='bold'); text(ax, 72, 36, 'neutre = 0', 'resultat', 's')
save(fig, '47-207')
