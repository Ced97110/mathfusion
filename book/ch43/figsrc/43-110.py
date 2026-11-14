import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
ly = lambda j: 42 + (4 - j) * 6.4
text(ax, 34, 76, 'pion 1 : 3 choix', 'varie', 's'); text(ax, 68, 76, 'pion 2 : 3 choix', 'varie', 's')
disc(ax, 8, 42, 1.8, 'fixe')
for i in range(3):
    y1 = ly(3 * i + 1)
    line(ax, [(9.8, 42), (30.8, y1)], 'fixe')
    disc(ax, 34, y1, 3.2, 'varie', label=str(i + 1))
    for j in range(3):
        line(ax, [(37.2, y1), (66.5, ly(3 * i + j))], 'fixe', lw=0.6)
        disc(ax, 68, ly(3 * i + j), 1.5, 'resultat')
text(ax, 44, 8, '3 × 3 = 9 applications', 'resultat', 'm')
text(ax, 78, 42, '1 point = 1 application', 'resultat', 's', rot=90)
save(fig, '43-110')
