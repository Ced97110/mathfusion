import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(54)
box(ax, 2, 42, 36, 9, 'sujet', label='Addition', size='m')
box(ax, 50, 42, 36, 9, 'autre', label='Multiplication', size='m')
L = [r"$2+2+2=6$", 'coefficient 3', r"coefficient $-1$"]
R = [r"$5\times5\times5=5^3$", 'exposant 3', r"inverse : $1/5$"]
for i in range(3):
    y = 28 - 13 * i
    box(ax, 2, y, 36, 10, 'sujet', label=L[i], size='s')
    box(ax, 50, y, 36, 10, 'autre', label=R[i], size='s')
    arrow(ax, (38, y + 5), (50, y + 5), 'varie')
save(fig, '80-410')
