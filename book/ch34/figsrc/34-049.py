import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
f = lambda v: 14 + 60 * v
def row(y, title, s2, x2, lab2, cap2, w3, lab3):
    text(ax, 4, y + 12, title, 'encre', 's', ha='left')
    box(ax, f(0), y, 45, 6, 'fixe', label='cos A cos B = 0,75', size='s')
    box(ax, x2, y - 8, 15, 6, 'varie', label=lab2, size='s')
    text(ax, x2 - 2, y - 5, cap2, 'varie', 's', ha='right')
    box(ax, f(0), y - 16, w3, 6, 'resultat', label=lab3, size='s')
row(72, 'A = 30°, B = 30° : A + B = 60°', 0, f(.5), '− 0,25', 'sin A sin B = 0,25', 30, 'cos 60° = 0,5')
row(38, 'A = −30°, B = 30° : A + B = 0°', 0, f(.75), '+ 0,25', 'sin A sin B = −0,25', 60, 'cos 0° = 1')
numberline(ax, 14, 74, 8, 0, 1, 0.25, every=2)
save(fig, '34-049')
