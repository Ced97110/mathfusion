import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 44, 45, 'les quatre sommes possibles de deux bits', 'encre', 'm')
box(ax, 24, 28, 26, 8, 'fixe', label='0 : pair', size='m')
box(ax, 52, 28, 26, 8, 'fixe', label='1 : impair', size='m')
box(ax, 6, 16, 16, 9, 'fixe', label='0 : pair', size='s')
box(ax, 6, 5, 16, 9, 'fixe', label='1 : impair', size='s')
cells = [('0 + 0 = 0', 24, 16, 'sujet'), ('0 + 1 = 1', 52, 16, 'sujet'),
         ('1 + 0 = 1', 24, 5, 'sujet'), ('1 + 1 = 0', 52, 5, 'varie')]
for s, x, y, r in cells:
    box(ax, x, y, 26, 9, r, label=s, size='m')
save(fig, '68-023')
