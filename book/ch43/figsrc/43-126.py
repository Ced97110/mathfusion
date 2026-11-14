import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u, x0, y = 0.8, 4, 28
for i in range(8):
    box(ax, x0 + 12 * u * i, y, 12 * u, 9, 'sujet', label='12', size='s', r=0.4)
xr = x0 + 96 * u
box(ax, xr, y, 4 * u, 9, 'varie', r=0.4)
text(ax, xr + 2 * u, y + 4.5, '4', 'varie', 's')
brace(ax, x0, xr + 4 * u, y + 9, 'encre', label='100', down=False)
brace(ax, x0, xr - 0.3, y, 'sujet', label='8 retraits de 12', down=True)
arrow(ax, (xr + 2 * u, 10), (xr + 2 * u, y - 7), 'varie')
text(ax, xr + 2 * u - 2, 6, 'reste 4 : représentant', 'varie', 's', ha='right')
save(fig, '43-126')
