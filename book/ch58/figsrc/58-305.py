import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 7.0; O = (26, 28)
for d in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
    arrow(ax, O, iso(d[0] * 2.4, d[1] * 2.4, d[2] * 2.4, O, u), 'fixe', lw=0.7)
disc(ax, O[0], O[1], 2.0, 'sujet')
text(ax, O[0] + 5, O[1] - 4, 'O', 'sujet', 'm', weight='bold')
text(ax, 26, 51, 'l’espace (en gris)', 'fixe', 's')
x0 = 50
text(ax, x0, 47, 'W = {0} : le seul point O', 'sujet', 's', ha='left')
box(ax, x0, 31, 36, 10, 'fixe', label='base : ( ) vide', size='s')
text(ax, x0, 25, '0 ajout : rien hors de', 'varie', 's', ha='left')
text(ax, x0, 21, 'l’espace engendré par ( )', 'varie', 's', ha='left')
box(ax, x0, 5, 36, 10, 'resultat', label='dim W = 0', size='m', weight='bold')
save(fig, '58-305')
