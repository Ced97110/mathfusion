import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(48)
names = ['0 objet', '1 objet', '2 objets', '3 objets']
for i, (n, c) in enumerate(zip(names, [1, 3, 3, 1])):
    x = 7 + i * 20
    text(ax, x + 7, 40, n, 'fixe', 's')
    box(ax, x, 24, 14, 11, 'sujet', label=str(c), size='l', weight='bold')
    if i < 3: text(ax, x + 17, 29.5, '+', 'varie', 'l', weight='bold')
brace(ax, 7, 81, 21, 'resultat', None, depth=3)
text(ax, 44, 9, '= 8 sacs en tout', 'resultat', 'l', weight='bold')
save(fig, '42-002')
