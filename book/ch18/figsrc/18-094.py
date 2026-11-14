import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
box(ax, 26, 84, 36, 10, 'sujet', label=r'$x^2+1$')
for i, a in enumerate(['facteur commun', 'différence de carrés', 'trinôme']):
    y = 62 - i * 15
    box(ax, 8, y, 54, 10, 'fixe', label=a, size='s')
    arrow(ax, (62, y + 5), (68, y + 5), 'limite'); text(ax, 74, y + 5, 'échec', 'limite', 's')
arrow(ax, (35, 84), (35, 73), 'fixe')
box(ax, 6, 6, 76, 12, 'resultat', label='ne se factorise pas (réels)', size='s')
arrow(ax, (44, 32), (44, 19), 'resultat')
save(fig, '18-094')
