import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 12, 62, r'$H$', 'sujet', 'l'); text(ax, 12, 34, r'$3+H=H$', 'resultat', 'm')
for i in range(4):
    x = 30 + i * 15
    box(ax, x - 6, 57, 12, 10, 'sujet', label=str(3 * i), size='l')
    box(ax, x - 6, 29, 12, 10, 'resultat', label=str((3 * i + 3) % 12), size='l')
    arrow(ax, (x, 56), (x, 41), 'varie')
text(ax, 37.5, 48.5, '+ 3', 'varie', 'm'); text(ax, 80, 24.5, r'$12 = 0$', 'fixe', 's')
brace(ax, 24, 84 - 9, 27, 'resultat', label='mêmes 4 nombres', size='s')
text(ax, 44, 14, '3 lignes distinctes seulement', 'resultat', 'm')
save(fig, '47-015')
