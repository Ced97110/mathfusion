import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
w, y0, h = 27, 4, 46
xs = [2.5, 30.5, 58.5]
roles = ['sujet', 'autre', 'fixe']
titles = ['scalaire', 'vecteur', 'point']
caps = ['un seul nombre', 'nombre + direction', 'un endroit']
for x, r, t, c in zip(xs, roles, titles, caps):
    box(ax, x, y0, w, h, r)
    text(ax, x + w / 2, y0 + h - 5, t, r, 'm', weight='bold')
    text(ax, x + w / 2, y0 + 6, c, r, 's')
# scalaire : un nombre seul
text(ax, xs[0] + w / 2, 27, '5 kg', 'sujet', 'xl')
text(ax, xs[0] + w / 2, 18, '20 degrés', 'sujet', 's')
# vecteur : une flèche inclinée (force 50 N à 30°)
O = (xs[1] + 4, 19)
arrow(ax, O, (O[0] + 19 * math.cos(math.radians(30)) + 2, O[1] + 19 * math.sin(math.radians(30)) + 2), 'autre', lw=1.6)
text(ax, xs[1] + w / 2, 33, '50 N, 30°', 'autre', 's')
# point : un endroit
disc(ax, xs[2] + w / 2, 27, 2.2, 'fixe')
save(fig, '41-018')
