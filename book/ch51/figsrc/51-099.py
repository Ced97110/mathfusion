import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 72, 'Essais', 'fixe', 's')
for i, (s, x) in enumerate([(r'$2 \times 3 = 6$', 16), (r'$5 \times (-4) = -20$', 44), (r'$(-7)(-3) = 21$', 72)]):
    pass
rows = [(r'$2 \times 3 = 6$', 15), (r'$5 \times (-4) = -20$', 44), (r'$(-7) \times (-3) = 21$', 73)]
for s, x in rows:
    box(ax, x - 13.5, 52, 27, 13, 'resultat', label=s, size='s')
text(ax, 44, 47, r'jamais $0$', 'resultat', 's')
line(ax, [(6, 41), (82, 41)], 'fixe', lw=0.5)
text(ax, 44, 36, 'Raison, pour tous les couples', 'fixe', 's')
box(ax, 4, 18, 24, 11, 'sujet', label=r'$|a| \geq 1$', size='m')
box(ax, 32, 18, 24, 11, 'autre', label=r'$|b| \geq 1$', size='m')
text(ax, 30, 23.5, r'$\times$', 'encre', 'm')
arrow(ax, (57, 23.5), (62, 23.5), 'varie')
box(ax, 62.5, 18, 22, 11, 'resultat', label=r'$|ab| \geq 1$', size='m')
text(ax, 73.5, 13.5, r'donc $ab \neq 0$', 'resultat', 's')
text(ax, 16, 13.5, 'entier non nul', 'fixe', 's'); text(ax, 44, 13.5, 'entier non nul', 'fixe', 's')
save(fig, '51-099')
