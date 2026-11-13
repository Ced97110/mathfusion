import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cs = [18, 44, 70]
for c, n in zip(cs, (1, 4, 5)):
    box(ax, c - 11, 62, 22, 11, 'sujet', label=rf'$x-{n}$')
box(ax, 8, 38, 44, 11, 'varie', label=r'$x^2-5x+4$')
arrow(ax, (18, 62), (24, 49), 'varie'); arrow(ax, (44, 62), (38, 49), 'varie')
text(ax, 61, 44, 'étape 1', 'varie', 's')
text(ax, 50, 30, 'étape 2', 'varie', 's')
box(ax, 4, 8, 80, 13, 'resultat', label=r'$x^3-10x^2+29x-20$', size='l')
arrow(ax, (30, 38), (30, 21), 'varie'); arrow(ax, (70, 62 - 0.0), (70, 21), 'varie')
text(ax, 44, 3, 'coefficients : 1, −10, 29, −20', 'fixe', 's')
save(fig, '55-069')
