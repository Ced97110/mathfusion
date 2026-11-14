import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 44, 46, r'$2\times$ chaque case 0 … 9, reste sur 10', 'sujet', 's')
for k in range(10):
    box(ax, 6 + k * 7.8, 28, 7.6, 8, 'fixe', label=str((2 * k) % 10), size='s')
text(ax, 44, 22, 'toujours pair', 'fixe', 's')
box(ax, 24, 4, 40, 10, 'limite', label='1 : jamais', dash=True)
save(fig, '47-184')
