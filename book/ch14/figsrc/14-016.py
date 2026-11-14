import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s, g = 4, 1.2
for y, n in [(42, 3), (30, 4), (18, 10)]:
    text(ax, 8, y + 2, '2', 'fixe', 'l'); text(ax, 12.5, y + 5, str(n), 'varie', 'm')
    for i in range(n): box(ax, 22 + i * (s + g), y, s, s + 0, 'sujet', r=0.4)
box(ax, 30, 3, 28, 9, 'varie', label=r'$2^{n}$', size='l')
text(ax, 70, 7.5, 'n = 3, 4 ou 10', 'varie', 's') if False else text(ax, 74, 7.5, 'n : libre', 'varie', 's')
text(ax, 15, 7.5, '2 : fixe', 'fixe', 's')
save(fig, '14-016')
