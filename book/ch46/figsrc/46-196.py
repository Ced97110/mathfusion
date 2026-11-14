import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 56, 'le cycle commence par 5', 'sujet', 's')
for x, n in zip([20, 36, 52, 68], [5, 8, 2, 6]):
    box(ax, x - 6, 40, 12, 10, 'sujet' if n == 5 else 'varie', label=str(n), size='l')
for i in range(3):
    arrow(ax, (20 + 16 * i + 6.5, 45), (20 + 16 * (i + 1) - 6.5, 45), 'fixe', lw=0.7)
pairs = [(6, 24), (2, 44), (8, 64)]
for b, x in pairs:
    box(ax, x - 9, 16, 18, 10, 'varie')
    text(ax, x - 3.5, 21, '5', 'sujet', 'm')
    text(ax, x + 3.5, 21, str(b), 'varie', 'm')
    arrow(ax, (x, 39), (x, 27.5), 'fixe', lw=0.7)
arrow(ax, (72, 7), (16, 7), 'fixe', lw=0.9)
text(ax, 44, 2.5, 'on fait de droite à gauche', 'fixe', 's')
save(fig, '46-196')
