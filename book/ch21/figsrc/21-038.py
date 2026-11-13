import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 14, 60, 'départ', 'sujet', 's'); text(ax, 44, 60, 'étape décisive', 'varie', 's'); text(ax, 74, 60, 'arrivée', 'resultat', 's')
for i, (s, d, e) in enumerate([(r'$5\times b=0$', 'diviser par 5', r'$b=0$'), (r'$a\times 4=0$', 'diviser par 4', r'$a=0$')]):
    y = 36 - 22 * i
    box(ax, 2, y, 25, 14, 'sujet', label=s)
    box(ax, 32, y, 24, 14, 'varie', label=d, size='s')
    box(ax, 61, y, 25, 14, 'resultat', label=e)
    arrow(ax, (27, y + 7), (32, y + 7), 'fixe'); arrow(ax, (56, y + 7), (61, y + 7), 'varie')
text(ax, 44, 8, r'permis car le nombre divisé $\neq 0$', 'encre', 's')
save(fig, '21-038')
