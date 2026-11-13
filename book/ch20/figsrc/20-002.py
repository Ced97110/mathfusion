import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(56)
x = 6
for i in range(3): box(ax, x, 26, 9, 9, 'sujet'); x += 11
x = 44
for i in range(2): box(ax, x, 26, 9, 9, 'varie'); x += 11
text(ax, 21.5, 40, '3 pains', 'sujet', 's'); text(ax, 54, 40, '2 gâteaux', 'varie', 's')
brace(ax, 6, 37, 24, 'sujet'); brace(ax, 44, 64, 24, 'varie')
text(ax, 21.5, 17, '$x$', 'sujet', 'xl', weight='bold'); text(ax, 54, 17, '$y$', 'varie', 'xl', weight='bold')
text(ax, 21.5, 11, 'nombre de pains', 'sujet', 's'); text(ax, 54, 11, 'nombre de gâteaux', 'varie', 's')
text(ax, 44, 3.5, r'couple $(x,\,y)=(3,\,2)$', 'encre', 'm')
save(fig, '20-002')
