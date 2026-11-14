import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 9, 65, r'$x$', 'sujet', 'm')
text(ax, 37, 65, 'tripler', 'varie', 's')
text(ax, 37, 60, r'$x\mapsto 0$', 'fixe', 's')
text(ax, 74, 65, 'somme', 'resultat', 'm')
data = [(30, 4, 12, 12), (4, 5, 15, 15)]
for y0, x, a, s in data:
    box(ax, 2, y0 + 6, 14, 10, 'sujet', label=str(x))
    box(ax, 28, y0 + 12, 18, 10, 'varie', label=str(a))
    box(ax, 28, y0, 18, 10, 'fixe', label='0')
    box(ax, 62, y0 + 6, 24, 10, 'resultat', label=str(s))
    arrow(ax, (16.5, y0 + 12), (27.5, y0 + 16), 'varie')
    arrow(ax, (16.5, y0 + 10), (27.5, y0 + 6), 'fixe')
    arrow(ax, (46.5, y0 + 16), (61.5, y0 + 13), 'varie')
    arrow(ax, (46.5, y0 + 6), (61.5, y0 + 9), 'fixe')
text(ax, 44, 1.5, 'la somme redonne « tripler »', 'resultat', 's')
save(fig, '57-049')
