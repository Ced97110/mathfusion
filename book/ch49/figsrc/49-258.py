import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 34, 10, 24, 40, 'sujet', label='circuit', size='l')
for k, v in enumerate(['1', '0', '1']):
    y = 42 - 12 * k
    line(ax, [(14, y), (34, y)], 'fixe', lw=1.0)
    disc(ax, 10, y, 3.6, 'varie', label=v, size='l')
arrow(ax, (58, 30), (74, 30), 'resultat', lw=1.2)
box(ax, 74, 25, 12, 10, 'resultat', label='0/1', size='m')
text(ax, 12, 54, '3 entrées', 'varie', 'm')
text(ax, 76, 40, 'sortie', 'resultat', 'm', ha='left')
text(ax, 44, 4, r'$n$ fils, un 0 ou un 1 sur chacun', 'encre', 's')
save(fig, '49-258')
