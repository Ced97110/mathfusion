import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def row(y, head, a, b, na, nb, op):
    text(ax, 44, y + 14, head, 'varie', 'm')
    box(ax, 3, y, 25, 9, 'sujet', label=a)
    box(ax, 60, y, 25, 9, 'resultat', label=b)
    arrow(ax, (29, y + 4.5), (59, y + 4.5), 'varie')
    text(ax, 44, y + 8.5, op, 'varie', 's')
    text(ax, 15.5, y - 4, na, 'sujet', 's')
    text(ax, 72.5, y - 4, nb, 'resultat', 's')
row(40, 'couper un cycle', '(1 2 3 4)', '(1)(2 3 4)', '$N=3$', '$N=2$', r'$\times$ (1 2)')
row(16, 'souder deux cycles', '(1 2)(3 4)', '(1 2 3 4)', '$N=2$', '$N=3$', r'$\times$ (1 3)')
text(ax, 44, 3, 'chaque échange change $N$ de 1', 'fixe', 's')
save(fig, '46-208')
