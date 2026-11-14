import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
def add(a, b):
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
code = ['00000', '01101', '10011', '11110']
w, gap, x0 = 16, 2, 14
text(ax, 44, 57, 'ligne 000 : le code C', 'encre', 's')
text(ax, 44, 3, 'ligne de syndrome 010', 'encre', 's')
for k, c in enumerate(code):
    x = x0 + k * (w + gap)
    box(ax, x, 40, w, 8, 'fixe', label=c, size='s')
    box(ax, x, 10, w, 8, 'sujet', label=add(c, '00010'), size='s')
    arrow(ax, (x + w / 2, 39), (x + w / 2, 19.5), 'varie')
text(ax, 7, 29, '+ 00010', 'varie', 's')
save(fig, '68-170')
