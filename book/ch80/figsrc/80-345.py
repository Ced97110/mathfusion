import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
w, g = 9, 1.5
text(ax, 44, 57, 'diviseurs de 30 : 8', 'fixe', 'm')
for i in range(8):
    box(ax, 2.75 + (w + g) * i, 44, w, 9, 'fixe')
text(ax, 44, 35, 'diviseurs de 12 : 6', 'sujet', 'm')
for i, d in enumerate([1, 2, 3, 4, 6, 12]):
    box(ax, 2.75 + (w + g) * i, 22, w, 9, 'sujet', label=str(d))
for i in (6, 7):
    box(ax, 2.75 + (w + g) * i, 22, w, 9, 'limite', fill=False, dash=True)
text(ax, 44, 12, 'deux cases vides en moins', 'limite', 's')
save(fig, '80-345')
