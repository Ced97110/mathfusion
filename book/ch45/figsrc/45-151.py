import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 23, 59, 'interrupteur', 'sujet', 'm')
text(ax, 66, 59, 'cadran', 'autre', 'm')
cw = 10
for i in range(2): box(ax, 12 + i * (cw + 1), 40, cw, 12, 'sujet' if i == 1 else 'fixe', label=str(i), size='l')
for i in range(3): box(ax, 50 + i * (cw + 1), 40, cw, 12, 'autre' if i == 2 else 'fixe', label=str(i), size='l')
arrow(ax, (12 + cw + 1 + cw / 2, 39), (38, 25), 'sujet')
arrow(ax, (50 + 2 * (cw + 1) + cw / 2, 39), (50, 25), 'autre')
box(ax, 32, 12, 24, 13, 'resultat', label='(1, 2)', size='l')
text(ax, 44, 5, 'un état = un couple', 'resultat', 's')
save(fig, '45-151')
