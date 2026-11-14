import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 87, 'Horloge à 4 heures', 'encre', 'm')
xs = [14, 34, 54, 74]
for v, x in enumerate(xs):
    disc(ax, x, 58, 6.5, 'varie' if v == 2 else 'sujet', label=str(v), size='l')
arrow(ax, (54, 64.5), (14, 64.5), 'varie', curve=0.4)
text(ax, 34, 76, r'$2\times2=4=0$', 'varie', 'm')
text(ax, 44, 42, r'Si $2\times b=1$ (inverse $b$)', 'encre', 's')
arrow(ax, (44, 38), (44, 31), 'fixe')
text(ax, 48, 34.5, 'on multiplie par 2', 'fixe', 's', ha='left')
box(ax, 14, 19, 60, 11, 'limite', label=r'on obtient $0=2$ : faux', size='m')
text(ax, 44, 9, r'donc 2 n’a pas d’inverse', 'limite', 'm')
save(fig, '67-002')
