import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
assert (3 + 0, 2 - 0) == (3, 2) and ((3 + 6) % 12, (2 - 6) % 12) == (9, 8) and 3 + 2 == 5
text(ax, 22, 52, r'$a$ dans $H\cap K$', 'varie', 'm'); text(ax, 66, 52, 'écritures de 5', 'resultat', 'm')
box(ax, 10, 10, 24, 36, 'varie', fill=False, dash=True)
for y, a, e in [(36, '0', '3 + 2'), (20, '6', '9 + 8')]:
    disc(ax, 22, y, 5, 'varie', label=a, size='l')
    box(ax, 51, y - 5, 30, 10, 'resultat', label=e, size='l')
    arrow(ax, (36, y), (49, y), 'varie')
text(ax, 44, 3.5, r'2 choix = 2 écritures', 'encre', 'm')
save(fig, '50-197')
