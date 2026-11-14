import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 30, 56, '1re case', 'fixe', 's'); text(ax, 58, 56, '2e case', 'fixe', 's')
for y, b in [(40, '5'), (28, '8'), (16, '13')]:
    box(ax, 20, y, 20, 9, 'fixe', label='0', size='m', dash=True)
    box(ax, 48, y, 20, 9, 'sujet', label=b, size='m')
text(ax, 44, 8, r'$d=0$ : on n’ajoute rien à la base', 'varie', 's')
text(ax, 8, 44.5, '(0, 5)', 'fixe', 's', ha='left')
text(ax, 8, 32.5, '(0, 8)', 'fixe', 's', ha='left')
text(ax, 8, 20.5, 'somme', 'fixe', 's', ha='left')
save(fig, '59-029')
