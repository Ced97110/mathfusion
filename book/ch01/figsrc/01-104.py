import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xs = [14, 30, 46, 62]; names = ['milliers', 'centaines', 'dizaines', 'unités']
top = ['4', '3', '2', '9']; bot = ['4', '4', '0', '0']
for x, n in zip(xs, names):
    text(ax, x + 7, 59, n, 'fixe', 's')
for i, x in enumerate(xs):
    for y, d in ((40, top[i]), (26, bot[i])):
        if i == 0:
            box(ax, x, y, 14, 9, 'fixe', label=d)
        elif i == 1:
            box(ax, x, y, 14, 9, 'sujet', label=d, lw=1.4)
        else:
            box(ax, x, y, 14, 9, 'fixe', fill=False, dash=True)
            t = text(ax, x + 7, y + 4.5, d, 'fixe', 'm'); t.set_alpha(0.45)
line(ax, [(19, 36.8), (23, 36.8)], 'fixe', lw=0.9)
line(ax, [(19, 38.2), (23, 38.2)], 'fixe', lw=0.9)
text(ax, 37, 19, '3 plus petit que 4 : arrêt', 'sujet', 's')
arrow(ax, (14, 53.5), (40, 53.5), 'varie')
text(ax, 44, 10, '4 329 plus petit que 4 400', 'resultat', 'm')
save(fig, '01-104')
