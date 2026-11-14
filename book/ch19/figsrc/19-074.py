import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
A, C, B = (10, 12), (31, 12), (31, 54)
line(ax, [A, B], 'sujet', lw=1.4)
line(ax, [C, B], 'varie', lw=1.6); line(ax, [A, C], 'autre', lw=1.6)
text(ax, 34.5, 33, '8', 'varie', 'm'); text(ax, 20.5, 8, '4', 'autre', 'm')
# steps in reading order, top to bottom
rows = [(54, '1', 'varie', r'$13-5=8$', 'en haut : vertical'),
        (40, '2', 'autre', r'$6-2=4$', 'en bas : horizontal'),
        (26, '3', 'fixe', 'la barre divise', None)]
for y, n, r, t, sub in rows:
    disc(ax, 46, y, 2.3, r, label=n, size='s')
    text(ax, 51, y, t, r, 'm', ha='left')
    if sub: text(ax, 51, y - 4.8, sub, r, 's', ha='left')
# the fraction, same colours as the steps
text(ax, 62, 15.5, '8', 'varie', 'l'); line(ax, [(57, 11.5), (67, 11.5)], 'fixe', lw=1.2)
text(ax, 62, 7.5, '4', 'autre', 'l'); text(ax, 77, 11.5, r'$=2$', 'resultat', 'l', weight='bold')
save(fig, '19-074')
