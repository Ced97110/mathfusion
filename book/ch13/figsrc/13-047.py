import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for x, t in [(14, 'nombre'), (44, 'modèle'), (74, 'distance à 0')]: text(ax, x, 62, t, 'fixe', 's')
for y, a, b in [(42, '8', '8'), (24, '−3', '3'), (6, '0', '0')]:
    box(ax, 4, y, 20, 12, 'varie', label=r'$a=%s$' % a.replace('−', '-'), size='m')
    box(ax, 34, y, 20, 12, 'sujet', label=r'$|a|$', size='l')
    box(ax, 64, y, 20, 12, 'resultat', label=b, size='l')
    arrow(ax, (24, y + 6), (34, y + 6), 'varie'); arrow(ax, (54, y + 6), (64, y + 6), 'varie')
save(fig, '13-047')
