import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
x0, y0, c = 22, 18, 11
for col in range(3):
    for row in range(4):
        n = next(k for k in range(12) if k % 3 == col and k % 4 == row)
        box(ax, x0 + c * col, y0 + c * row, c, c, 'sujet', label=str(n))
text(ax, x0 + 1.5 * c, 12, 'reste par 3 : 0, 1, 2', 'varie', 's')
text(ax, 12, y0 + 2 * c, 'reste par 4 : 0, 1, 2, 3', 'varie', 's', rot=90)
save(fig, '52-244')
