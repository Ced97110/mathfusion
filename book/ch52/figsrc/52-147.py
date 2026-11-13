import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0, y0, d = 18, 14, 9
for a in range(5):
    for b in range(5):
        r = 'sujet' if a == b else 'fixe'
        disc(ax, x0 + a * d, y0 + b * d, 1.3, r)
disc(ax, x0 + 3 * d, y0 + 0 * d, 1.5, 'limite')
arrow(ax, (x0 + 3 * d, y0 + 3 * d - 2), (x0 + 3 * d, y0 + 2), 'varie')
text(ax, x0 + 3 * d + 9, y0 + 1.5 * d, r'$\times\,(1,\,0)$', 'varie', 's')
text(ax, 62, 55, 'noyau : (a, a)', 'sujet', 's'); text(ax, x0 + 3 * d - 7, y0 + 3 * d + 4, '(3, 3)', 'sujet', 's')
text(ax, x0 + 3 * d, y0 - 5, '(3, 0) hors noyau', 'limite', 's')
text(ax, x0 + 2 * d, y0 - 10, 'pas un idéal', 'limite', 's')
text(ax, 5, 66, r'$b$', 'fixe'); text(ax, 84, 5, r'$a$', 'fixe')
save(fig, '52-147')
