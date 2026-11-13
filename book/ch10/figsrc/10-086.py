import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for i in range(10):
    x = 4 + 8 * i
    box(ax, x, 12, 7, 14, 'sujet', r=0.3)
    box(ax, x, 26, 7, 6, 'varie', label='2', size='s', r=0.3)
brace(ax, 4, 83, 34, 'varie', 'restes perdus : 10 × 2 = 20', down=False)
text(ax, 44, 6, 'dizaines gardées : 550 (vraie : 570)', 'sujet', 's')
save(fig, '10-086')
