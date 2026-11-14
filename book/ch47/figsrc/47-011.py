import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 14, 52, r'$H$', 'sujet', 'l'); text(ax, 14, 14, r'$2+H$', 'autre', 'l')
for i in range(4):
    x = 26 + i * 15
    box(ax, x - 6, 46, 12, 10, 'sujet', label=str(3 * i), size='l')
    box(ax, x - 6, 8, 12, 10, 'autre', label=str((3 * i + 2) % 12), size='l')
    arrow(ax, (x, 45), (x, 20), 'varie')
text(ax, 33.5, 33, '+ 2', 'varie', 'm')
text(ax, 44, 63, 'Nom : « 2 + H »', 'encre', 'm')
text(ax, 44, 3, r'$5+H$ donne la même ligne', 'resultat', 's')
save(fig, '47-011')
