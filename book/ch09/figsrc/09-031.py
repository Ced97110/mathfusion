import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
x0, k = 22, 63 / 36
brace(ax, x0, x0 + 36 * k, 54, 'fixe', label='36', down=False)
for i in range(9):
    box(ax, x0 + i * 4 * k, 38, 4 * k, 9, 'sujet', r=0.3, lw=0.7)
for i in range(4):
    box(ax, x0 + i * 9 * k, 14, 9 * k, 9, 'varie', r=0.3, lw=0.7)
text(ax, 10, 42.5, r'$b = 4$', 'sujet', 'm'); text(ax, 10, 18.5, r'$b = 9$', 'varie', 'm')
text(ax, 54, 33, '9 paquets', 'sujet', 's'); text(ax, 54, 9, '4 paquets', 'varie', 's')
save(fig, '09-031')
