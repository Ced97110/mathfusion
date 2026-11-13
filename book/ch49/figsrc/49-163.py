import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 20, 88, '4 classes', 'varie', 's'); text(ax, 68, 88, 'orbite : 4 points', 'resultat', 's')
for i, n in enumerate('ABCD'):
    yc = 76 - i * 18
    box(ax, 6, yc - 6, 28, 12, 'varie')
    disc(ax, 14, yc, 2.6, 'sujet'); disc(ax, 26, yc, 2.6, 'sujet')
    arrow(ax, (36, yc), (61, yc), 'varie')
    disc(ax, 68, yc, 4.5, 'resultat', label=n, size='m')
save(fig, '49-163')
