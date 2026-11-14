import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(80)
box(ax, 2, 12, 84, 62, 'fixe', fill=False, dash=True)
text(ax, 44, 69, 'cases inversibles de ℤ/55ℤ', 'fixe', 's')
# ligne du haut : 3 × 4 = 12
tops = [(8, '3'), (36, '4'), (64, '12')]
for x, s in tops:
    box(ax, x, 46, 16, 11, 'sujet', label=s)
text(ax, 28, 51.5, '×', 'encre', 'l'); text(ax, 56, 51.5, '=', 'encre', 'l')
# ligne du bas : leurs inverses
bots = [(8, '37'), (36, '14'), (64, '23')]
for x, s in bots:
    box(ax, x, 22, 16, 11, 'autre', label=s)
text(ax, 28, 27.5, '×', 'encre', 'l'); text(ax, 56, 27.5, '=', 'encre', 'l')
for x, _ in tops:
    arrow(ax, (x + 8, 45.5), (x + 8, 33.5), 'varie')
text(ax, 22, 39.5, 'inverse', 'varie', 's')
text(ax, 44, 16, r'$37\times14=518=9\times55+23$', 'autre', 's')
save(fig, '53-123')
