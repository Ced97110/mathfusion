import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
for x, s, r in ((10, '3', 'sujet'), (28, '5', 'sujet'), (60, '10', 'autre'), (78, '12', 'autre')):
    box(ax, x - 7, 40, 14, 9, r, label=s)
arrow(ax, (10, 50), (78, 50), 'varie', curve=-0.3)
arrow(ax, (28, 50), (60, 50), 'resultat', curve=-0.45)
text(ax, 19, 36, '(3, 5)', 'sujet', 's'); text(ax, 69, 36, '(10, 12)', 'autre', 's')
text(ax, 22, 26, '3 + 12 = 15', 'varie', 'm')
text(ax, 66, 26, '5 + 10 = 15', 'resultat', 'm')
text(ax, 44, 26, '=', 'encre', 'm')
text(ax, 44, 12, 'mêmes totaux : équivalents', 'resultat', 'm')
save(fig, '13-094')
