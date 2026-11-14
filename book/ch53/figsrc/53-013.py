import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'table connue de tous', 'encre', 'm')
top = ['A\n0', 'B\n1', 'C\n2', None, 'Z\n25']
for k, lab in enumerate(top):
    x = 6 + k * 16.5
    if lab is None: text(ax, x + 6.5, 45.5, '…', 'fixe', 'l')
    else: box(ax, x, 40, 13, 11, 'fixe', label=lab)
word = [('A', 0), ('L', 11), ('G', 6), ('E', 4), ('B', 1), ('R', 17), ('E', 4)]
for k, (ch, nb) in enumerate(word):
    box(ax, 3.6 + k * 11.8, 8, 10, 12, 'sujet', label=f'{ch}\n{nb}')
arrow(ax, (44, 38), (44, 23), 'varie', lw=1.3)
text(ax, 62, 31, 'ALGEBRE s’écrit :', 'encre', 's')
save(fig, '53-013')
