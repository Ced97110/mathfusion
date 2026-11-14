import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
# chaque ligne de A donne une équation : y_1 = 2 x_1 + 1 x_2, y_2 = 1 x_1 + 3 x_2
cw, ch = 10, 9
text(ax, 15.5, 50, 'le tableau A', 'encre', 's')
rows = [(('2', '1'), 'sujet', r'$y_1 = 2x_1 + 1x_2$', 30), (('1', '3'), 'autre', r'$y_2 = 1x_1 + 3x_2$', 18)]
for (a, b), role, eq, y in rows:
    box(ax, 4, y, cw, ch, role, label=a, size='m', r=0.5)
    box(ax, 15.5, y, cw, ch, role, label=b, size='m', r=0.5)
    arrow(ax, (27, y + ch / 2), (36, y + ch / 2), role, lw=1.2)
    box(ax, 37, y - 0.5, 49, ch + 1, role, label=eq, size='m', r=0.6)
text(ax, 61.5, 50, 'une ligne de A donne\nune case d’arrivée', 'encre', 's')
text(ax, 44, 8, 'même forme qu’un système d’équations', 'encre', 's')
save(fig, '58-207')
