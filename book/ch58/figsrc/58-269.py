import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ox, oy, u = 7, 12, 9
P = lambda a, b: (ox + a * u, oy + b * u)
# images de eta : couples (a, b) avec b - 3a multiple de 5
for a in range(6):
    for b in range(6):
        if (b - 3 * a) % 5 == 0:
            disc(ax, *P(a, b), 1.5, 'sujet')
        elif (a, b) == (1, 0):
            disc(ax, *P(a, b), 1.5, 'limite')
        else:
            disc(ax, *P(a, b), 1.2, 'fixe', fill=False)
text(ax, P(2, 1)[0], P(2, 1)[1] - 4.5, '(2, 1)', 'sujet', 's')
text(ax, P(1, 3)[0], P(1, 3)[1] - 4.5, '(1, 3)', 'sujet', 's')
text(ax, P(1, 0)[0], P(1, 0)[1] - 4.5, '(1, 0)', 'limite', 's', weight='bold')
disc(ax, 60, 52, 1.5, 'sujet'); text(ax, 63.5, 52, 'dans l’image', 'sujet', 's', ha='left')
disc(ax, 60, 44, 1.2, 'fixe', fill=False); text(ax, 63.5, 44, 'hors de l’image', 'fixe', 's', ha='left')
disc(ax, 60, 36, 1.5, 'limite'); text(ax, 63.5, 36, '(1, 0)', 'limite', 's', ha='left')
text(ax, 71, 24, 'une case sur cinq :', 'encre', 's')
text(ax, 71, 19, 'indice 5', 'encre', 'm', weight='bold')
save(fig, '58-269')
