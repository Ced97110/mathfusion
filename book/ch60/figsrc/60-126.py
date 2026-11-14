import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 13, 60, 'Judson', 'sujet', 'l', weight='bold')
text(ax, 75, 60, 'lemme', 'autre', 'l', weight='bold')
text(ax, 44, 60, 'même sous-groupe', 'fixe', 's')
rows = [(40, '9', '3', '0, 3, 6, 9'), (14, '4', '4', '0, 4, 8')]
for y, a, b, s in rows:
    box(ax, 3, y, 20, 12, 'sujet', label=a, size='l')
    box(ax, 65, y, 20, 12, 'autre', label=b, size='l')
    box(ax, 29, y, 30, 12, 'resultat', label=s, size='s')
    arrow(ax, (23.4, y + 6), (28.6, y + 6), 'sujet')
    arrow(ax, (64.6, y + 6), (59.4, y + 6), 'autre')
text(ax, 13, 34, 'tué par 4', 'fixe', 's')
text(ax, 75, 34, '3 × 1', 'fixe', 's')
text(ax, 13, 8, 'tué par 3', 'fixe', 's')
text(ax, 75, 8, '4 × 1', 'fixe', 's')
save(fig, '60-126')
