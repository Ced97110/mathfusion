import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 4, 62, 'même position ⇒ différence sur 0', 'encre', 's', ha='left')
for y, a, b, p, d in ((44, '1', '5', '1', r'$5 - 1 = 4$'), (16, '3', '11', '3', r'$11 - 3 = 8$')):
    disc(ax, 9, y + 6, 4, 'sujet', label=a, size='s'); disc(ax, 9, y - 6, 4, 'sujet', label=b, size='s')
    arrow(ax, (13.2, y + 6), (22, y + 1.5), 'fixe', lw=0.8); arrow(ax, (13.2, y - 6), (22, y - 1.5), 'fixe', lw=0.8)
    disc(ax, 27, y, 4.5, 'fixe', label=p, size='m')
    box(ax, 38, y - 5.5, 28, 11, 'varie', label=d, size='s')
    arrow(ax, (32, y), (37, y), 'varie', lw=1.0)
    arrow(ax, (66.5, y), (72, y), 'varie', lw=1.0)
    disc(ax, 79, y, 5, 'resultat', label='0', size='m')
text(ax, 79, 30, 'noyau', 'resultat', 's')
save(fig, '48-048')
