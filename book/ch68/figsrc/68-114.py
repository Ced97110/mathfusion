import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
X = [38 + 10 * i for i in range(5)]
text(ax, 4, 40, 'position', 'fixe', 's', ha='left')
for i, x in enumerate(X):
    text(ax, x, 40, str(i + 1), 'fixe', 's')
for y, lab, w, pos in [(28, r'$e_1$', '10000', 1), (14, r'$e_3$', '00100', 3)]:
    text(ax, 4, y, lab, 'sujet', 'm', ha='left')
    text(ax, 18, y, w, 'sujet', 'm', ha='left')
    for i, x in enumerate(X):
        disc(ax, x, y, 3, 'sujet', fill=(i + 1 == pos))
text(ax, 44, 4, 'un seul 1 : plein = 1', 'sujet', 's')
save(fig, '68-114')
