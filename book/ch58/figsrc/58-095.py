import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 38, 52, 'additionner', 'sujet', 's', weight='bold')
text(ax, 60, 52, r'$\times$ un nombre', 'varie', 's', weight='bold')
for y, name in [(38, 'flèches'), (24, 'polynômes'), (10, 'fonctions')]:
    text(ax, 3, y + 4.5, name, 'encre', 's', ha='left')
    box(ax, 28, y, 20, 9, 'sujet', label=r'$u+v$', size='s')
    box(ax, 50, y, 20, 9, 'varie', label=r'$\alpha\,u$', size='s')
box(ax, 73, 10, 13, 37, 'fixe', dash=True)
text(ax, 79.5, 28.5, r'$u\times v$' + '\nrien', 'fixe', 's')
save(fig, '58-095')
