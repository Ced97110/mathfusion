import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cols = [(20, 36, 'sujet'), (42, 58, 'varie'), (62, 78, 'autre')]
row1 = [r'$a$', r'$b$', r'$i$']
row2 = ['2', '3', r'$i$']
for y, labs in ((46, row1), (28, row2)):
    text(ax, 10, y + 6, r'$z =$', 'encre', 'm')
    text(ax, 39, y + 6, '+', 'encre', 'm')
    for (x0, x1, role), lab in zip(cols, labs):
        box(ax, x0, y, x1 - x0, 12, role, label=lab, size='l')
for x0, x1, role in cols:
    arrow(ax, ((x0 + x1) / 2, 46), ((x0 + x1) / 2, 41), 'fixe', lw=0.8)
text(ax, 28, 22, 'réel', 'sujet', 's')
text(ax, 50, 22, 'réel', 'varie', 's')
text(ax, 70, 22, r'$i^2 = -1$', 'autre', 's')
text(ax, 44, 10, '2 + 3 i : un nombre complexe', 'resultat', 's')
save(fig, '39-040')
