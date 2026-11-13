import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
sup = '¹²³⁴'
for i in range(4):
    y = 55.5 - 9 * i
    text(ax, 12, y, f'(a+b){sup[i]}', 'fixe', 'm')
labels = ['1, 1', '1, 2, 1', '1, 3, 3, 1', '1, 4, 6, 4, 1']
for i, s in enumerate(labels):
    box(ax, 20, 52 - 9 * i, 14 + 8 * i, 7, 'sujet', label=s, size='m')
text(ax, 12, 16.5, '(a+b)⁵', 'limite', 'm')
box(ax, 20, 13, 46, 7, 'limite', fill=False, dash=True)
text(ax, 43, 16.5, '?', 'limite', 'l')
text(ax, 44, 6, 'ligne suivante : non donnée', 'limite', 's')
line(ax, [(64, 25), (64, 55)], 'limite', dash=True)
text(ax, 66, 60, 'pourquoi ces nombres ?', 'limite', 's')
save(fig, '01-168')
