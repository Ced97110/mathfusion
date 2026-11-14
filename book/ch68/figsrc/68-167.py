import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(74)
text(ax, 44, 70, '4 classes, 4 étiquettes', 'encre', 'm')
classes = [('100', '011', '10'), ('010', '101', '11'), ('001', '110', '01'), ('000', '111', '00')]
for k, (a, b, s) in enumerate(classes):
    x = 3 + (k % 2) * 42
    y = 36 - (k // 2) * 31
    box(ax, x, y, 40, 27, 'sujet', fill=False)
    box(ax, x + 4, y + 13, 14, 8, 'fixe', label=a)
    box(ax, x + 22, y + 13, 14, 8, 'fixe', label=b)
    text(ax, x + 20, y + 6, f'syndrome {s}', 'resultat', 's')
save(fig, '68-167')
