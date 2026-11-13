import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 14, 60, 'avant', 'sujet', 'm'); text(ax, 74, 60, 'après', 'autre', 'm')
text(ax, 44, 60, r'$Sp_{2}$ agit', 'varie', 'm')
names = ['droite 1', 'droite 2', 'droite 3']
img = [1, 2, 0]
for i, n in enumerate(names):
    y = 44 - i*17
    disc(ax, 14, y, 5, 'sujet'); text(ax, 14, y, str(i+1), 'sujet', 'm')
    disc(ax, 74, y, 5, 'autre'); text(ax, 74, y, str(i+1), 'autre', 'm')
for i, j in enumerate(img):
    y0 = 44 - i*17; y1 = 44 - j*17
    arrow(ax, (19.5, y0 - (0.8 if y1 < y0 else -0.8 if y1 > y0 else 0)), (68.5, y1), 'varie')
text(ax, 44, 6, '3 droites, 3 droites', 'fixe', 's')
save(fig, '75-180')
