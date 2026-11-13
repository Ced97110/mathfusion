import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, 'même nombre', 'fixe', 's')
box(ax, 4, 52, 18, 10, 'autre', label='6/8', size='m')
box(ax, 36, 52, 18, 10, 'sujet', label='3/4', size='m')
arrow(ax, (22, 57), (36, 57), 'varie'); text(ax, 29, 61, r'$\div$ 2', 'varie', 's')
text(ax, 70, 57, 'irréductible', 'sujet', 's')
x0, y0, d = 30, 6, 5
for m in range(6):
    for n in range(5):
        disc(ax, x0 + m * d, y0 + n * d, 0.7, 'fixe')
disc(ax, x0 + 3 * d, y0 + 4 * d, 1.5, 'resultat')
arrow(ax, (45, 51), (45, y0 + 4 * d + 2.5), 'sujet')
text(ax, x0 + 5 * d + 3, y0 + 4 * d, r'(3 ; 4)', 'resultat', 's', ha='left')
text(ax, 20, 14, r'$m$ (haut)', 'fixe', 's')
text(ax, 20, 8, r'$n$ (bas)', 'fixe', 's')
save(fig, '43-134')
