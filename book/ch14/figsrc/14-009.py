import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s, g = 8.5, 4
x0 = (88 - (6 * s + 5 * g)) / 2
for i in range(6):
    x = x0 + i * (s + g)
    box(ax, x, 38, s, s, 'sujet', label='2')
    if i < 5: text(ax, x + s + g / 2, 42.25, '×', 'fixe', 'm')
brace(ax, x0, x0 + 6 * s + 5 * g, 36, 'varie', 'on compte : 6 facteurs 2')
arrow(ax, (44, 22), (44, 14), 'fixe')
text(ax, 44, 8, r'$2^{6}$', 'sujet', 'xl')
text(ax, 72, 10, 'exposant = 6', 'varie', 'm')
arrow(ax, (60, 10), (52.5, 10.5), 'varie')
save(fig, '14-009')
