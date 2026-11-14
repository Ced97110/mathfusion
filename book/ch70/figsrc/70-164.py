import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
rows = [(46, 'f ='), (32, r'$\partial f/\partial y=$'), (18, 'PGCD ='), (4, 'f ÷ PGCD =')]
for y, s in rows: text(ax, 2, y + 4.5, s, 'encre', 's', ha='left')
box(ax, 24, 46, 16, 9, 'varie', label=r'$y-1$', size='s'); text(ax, 42, 50.5, '×', 'encre', 's')
box(ax, 44, 46, 16, 9, 'varie', label=r'$y-1$', size='s')
box(ax, 24, 32, 16, 9, 'fixe', label='2', size='s'); box(ax, 44, 32, 16, 9, 'varie', label=r'$y-1$', size='s')
box(ax, 44, 18, 16, 9, 'varie', label=r'$y-1$', size='s')
box(ax, 44, 4, 16, 9, 'resultat', label=r'$y-1$', size='s')
arrow(ax, (52, 32), (52, 27.8), 'fixe'); arrow(ax, (52, 18), (52, 13.8), 'fixe')
# the line y = 1 is the same before and after
line(ax, [(66, 10), (86, 10)], 'fixe', lw=0.7); line(ax, [(70, 10), (70, 34)], 'fixe', lw=0.7)
line(ax, [(70, 18), (86, 18)], 'sujet', lw=1.8)
text(ax, 79, 22.5, 'y = 1', 'sujet', 's')
text(ax, 77, 40, 'même droite', 'resultat', 's')
save(fig, '70-164')
