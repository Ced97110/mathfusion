import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
k = 1.1; x0 = 8; y = 22
box(ax, x0, y, 60 * k, 10, 'sujet', label='60 min = 1 h', size='m')
box(ax, x0 + 60 * k, y, 5 * k, 10, 'varie')
text(ax, x0 + 60 * k + 2.75, y - 3.5, '5 min', 'varie', 's')
brace(ax, x0, x0 + 65 * k, y + 10, 'fixe', label='65 min', down=False)
text(ax, 44, 8, '65 = 60 + 5', 'fixe', 'l')
text(ax, 44, 2.5 + 0, '', 'fixe', 's')
save(fig, '11-067')
