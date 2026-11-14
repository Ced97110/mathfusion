import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 19, 74, 'algorithme d’Euclide', 'sujet', 'm')
text(ax, 69, 74, 'suite de Sturm', 'autre', 'm')
rows = [(58, r'$x^3-3x+1$', r'$x^3-3x+1$', True),
        (44, r'$3x^2-3$', r'$3x^2-3$', True),
        (30, r'$-2x+1$', r'$2x-1$', False),
        (16, r'$-9/4$', r'$9/4$', False)]
for y, a, b, same in rows:
    box(ax, 4, y, 30, 10, 'fixe' if same else 'sujet', label=a)
    box(ax, 54, y, 30, 10, 'fixe' if same else 'autre', label=b)
    if same:
        text(ax, 44, y + 5, '=', 'encre', 'l')
    else:
        arrow(ax, (34.5, y + 4), (53.5, y + 4), 'varie')
        text(ax, 44, y + 8, r'$\times(-1)$', 'varie', 's')
save(fig, '69-073')
