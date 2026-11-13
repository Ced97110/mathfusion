import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
NB = ' '
fig, ax = canvas(78)
xs = [4, 26, 48, 70]
text(ax, 4, 72, 'base dix (chiffres 0 à 9)', 'sujet', 'm', ha='left', weight='bold')
for x, lab in zip(xs, ['1' + NB + '000', '100', '10', '1']):
    box(ax, x, 52, 16, 12, 'sujet', label=lab, size='m')
for x in (70, 48, 26):
    arrow(ax, (x, 58), (x - 6, 58), 'varie')
text(ax, 45, 46, "× 10 d'une case à l'autre", 'varie', 's', weight='bold')
line(ax, [(4, 40), (84, 40)], 'fixe', dash=True)
text(ax, 4, 34, 'base deux (chiffres 0 et 1)', 'autre', 'm', ha='left', weight='bold')
for x, lab in zip(xs, ['8', '4', '2', '1']):
    box(ax, x, 14, 16, 12, 'autre', label=lab, size='m')
for x in (70, 48, 26):
    arrow(ax, (x, 20), (x - 6, 20), 'varie')
text(ax, 45, 8, "× 2 d'une case à l'autre", 'varie', 's', weight='bold')
save(fig, '01-074')
