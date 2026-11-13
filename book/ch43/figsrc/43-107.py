import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
xs = [14, 34, 54, 74]
text(ax, 2, 72, r'$S$ : 4 pions', 'sujet', 's', ha='left')
for i, x in enumerate(xs):
    disc(ax, x, 58, 4.5, 'sujet')
    box(ax, x - 6, 22, 12, 10, 'autre', label=str(i))
    arrow(ax, (x, 53.2), (x, 33), 'varie')
brace(ax, xs[0] - 6, xs[-1] + 6, 20, 'autre', label=r'$n = 4$ numéros : de 0 à $n - 1$', depth=2.2)
text(ax, 44, 5, r'$|S| = 4$', 'resultat', 'l')
save(fig, '43-107')
