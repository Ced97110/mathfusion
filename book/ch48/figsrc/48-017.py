import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [22 + i * 15.5 for i in range(4)]
for i, x in enumerate(xs):
    box(ax, x, 40, 12, 9, 'sujet', label=str(4 * i))
    box(ax, x, 14, 12, 9, 'varie', label=str(3 + 4 * i))
    arrow(ax, (x + 6, 39), (x + 6, 24), 'fixe', both=True)
text(ax, 11, 48, 'noyau', 'sujet'); text(ax, 11, 43, '4ℤ', 'sujet')
text(ax, 11, 19, 'fibre', 'varie'); text(ax, 11, 14, '3 + 4ℤ', 'varie')
text(ax, 11, 32, '+ 3 / − 3', 'fixe', 's')
save(fig, '48-017')
