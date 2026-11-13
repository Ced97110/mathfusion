import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
x0, x1, y = 8, 78, 26
f = numberline(ax, x0, x1, y, 800, 1600, step=100, every=2, arrow_right=False)
bands = [(800, 900, 'sujet', 'savants arabes\n' + r'IX$^{e}$ siècle', f(850) + 2),
         (1400, 1500, 'varie', 'Alberti\n' + r'XV$^{e}$ siècle', f(1450) - 7),
         (1500, 1600, 'autre', 'Viète\n' + r'XVI$^{e}$ siècle', f(1550) + 6)]
for a, b, role, lab, lx in bands:
    box(ax, f(a), y + 2, f(b) - f(a), 8, role)
    line(ax, [((f(a) + f(b)) / 2, y + 10), (lx, 44)], role, lw=0.7)
    text(ax, lx, 49, lab, role, 's')
text(ax, 44, 7, 'une méthode au crayon,\nvieille de plus de 1 000 ans', 'fixe', 's')
save(fig, '53-066')
