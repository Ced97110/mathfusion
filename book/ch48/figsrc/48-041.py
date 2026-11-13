import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 4, 72, r'$\times 3$ : images toutes différentes', 'resultat', 's', ha='left')
for y, a, b in ((62, '2', '6'), (50, '5', '15')):
    disc(ax, 16, y, 4.5, 'sujet', label=a, size='m')
    arrow(ax, (21, y), (61, y), 'resultat', lw=1.1)
    disc(ax, 68, y, 5, 'resultat', label=b, size='m')
text(ax, 41, 65.5, r'$\times 3$', 'resultat', 's')
line(ax, [(4, 40), (84, 40)], 'fixe', lw=0.5, dash=True)
text(ax, 4, 35, 'bouton : même position', 'limite', 's', ha='left')
for y, a in ((25, '1'), (11, '5')):
    disc(ax, 16, y, 4.5, 'sujet', label=a, size='m')
arrow(ax, (21, 25), (62, 19.5), 'limite', lw=1.1)
arrow(ax, (21, 11), (62, 16.5), 'limite', lw=1.1)
disc(ax, 68, 18, 5, 'limite', label='1', size='m')
save(fig, '48-041')
