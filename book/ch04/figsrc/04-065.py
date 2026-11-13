import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 78, '10 − 4 − 3', 'encre', 'l', weight='bold')
# de gauche à droite : retirer 4, puis 3, il reste 3
text(ax, 44, 70, 'gauche à droite : 6, puis 3', 'resultat', 's')
for i in range(10):
    disc(ax, 17 + 6 * i, 62, 2.2, 'resultat' if i <= 2 else 'varie')
brace(ax, 50.8, 73.2, 58.5, 'varie', label='− 4', down=True, size='s')
brace(ax, 32.8, 49.2, 58.5, 'varie', label='− 3', down=True, size='s')
text(ax, 80, 62, '= 3', 'resultat', 'm', weight='bold')
# regroupement du camarade : 10 − (4 − 3), on retire 1
text(ax, 44, 46, '10 − (4 − 3) : retire 1', 'limite', 's')
for i in range(10):
    disc(ax, 17 + 6 * i, 38, 2.2, 'limite' if i <= 8 else 'varie')
brace(ax, 68.8, 73.2, 34.5, 'varie', label='− 1', down=True, size='s')
text(ax, 80, 38, '= 9', 'limite', 'm', weight='bold')
# l'addition : les deux regroupements donnent le même total
text(ax, 44, 20, '(10 + 4) + 3 = 17', 'autre', 'm')
text(ax, 44, 13, '10 + (4 + 3) = 17', 'autre', 'm')
text(ax, 44, 5.5, '3 − 4 : pas de réponse', 'limite', 's')
save(fig, '04-065')
