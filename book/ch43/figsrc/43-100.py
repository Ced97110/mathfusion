import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
def panel(yc, title, same, verdict, role):
    box(ax, 3, yc - 17, 82, 34, 'fixe', fill=False)
    text(ax, 44, yc + 13, title, 'encre', 's')
    ys = (yc + 4, yc - 8)
    for y, n in zip(ys, (3, 15)):
        disc(ax, 14, y, 3.8, 'sujet', label=str(n))
    line(ax, [(14, ys[0] - 4), (14, ys[1] + 4)], 'sujet', dash=True)
    text(ax, 20, yc - 2, r'$E$', 'sujet', 's')
    if same:
        disc(ax, 54, yc - 2, 3.8, role, label='3')
        for y in ys: arrow(ax, (18.5, y), (50.5, yc - 2 + (1.5 if y > yc else -1.5)), 'varie')
    else:
        for y, n in zip(ys, (3, 15)):
            disc(ax, 54, y, 3.8, role, label=str(n)); arrow(ax, (18.5, y), (49.5, y), 'varie')
    text(ax, 73, yc - 2, verdict, role, 's')
panel(70, 'f = reste de la division par 12', True, 'compatible', 'resultat')
panel(27, 'f = le nombre lui-même', False, 'pas compatible', 'limite')
save(fig, '43-100')
