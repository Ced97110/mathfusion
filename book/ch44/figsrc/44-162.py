import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
c, x0, y0 = 11, 18, 8
rows = 5
vals = [2, 3, 4, 0, 1]
for r in range(rows):
    for k in range(5):
        y = y0 + (rows - 1 - r) * c
        if r == 2:
            role = 'resultat' if vals[k] == 0 else 'sujet'
            box(ax, x0 + k * c, y, c, c, role, label=str(vals[k]), r=0.3)
        else:
            box(ax, x0 + k * c, y, c, c, 'fixe', r=0.3)
for k in range(5):
    text(ax, x0 + k * c + c / 2, y0 + rows * c + 3, str(k), 'varie' if k == 3 else 'fixe', 'm')
text(ax, 9, y0 + 2 * c + c / 2, 'ligne 2', 'sujet', 's')
text(ax, 44, 3.2, 'le 0 est ici : opposé de 2 = 3', 'resultat', 's')
save(fig, '44-162')
