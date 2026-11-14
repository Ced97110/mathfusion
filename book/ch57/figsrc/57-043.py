import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 9, 65, r'$x$', 'sujet', 'm')
text(ax, 37, 65, r'$\eta$ : doubler', 'varie', 's')
text(ax, 37, 60, r'$\zeta$ : tripler', 'varie', 's')
text(ax, 74, 65, r'$\eta+\zeta$', 'resultat', 'm')
data = [(30, 4, 8, 12, 20), (4, 5, 10, 15, 25)]
for y0, x, a, b, s in data:
    box(ax, 2, y0 + 6, 14, 10, 'sujet', label=str(x))
    box(ax, 28, y0 + 12, 18, 10, 'varie', label=str(a))
    box(ax, 28, y0, 18, 10, 'varie', label=str(b))
    box(ax, 62, y0 + 6, 24, 10, 'resultat', label=str(s))
    arrow(ax, (16.5, y0 + 12), (27.5, y0 + 16), 'varie')
    arrow(ax, (16.5, y0 + 10), (27.5, y0 + 6), 'varie')
    arrow(ax, (46.5, y0 + 16), (61.5, y0 + 13), 'resultat')
    arrow(ax, (46.5, y0 + 6), (61.5, y0 + 9), 'resultat')
text(ax, 44, 1.5, 'les deux images, puis la somme', 'resultat', 's')
save(fig, '57-043')
