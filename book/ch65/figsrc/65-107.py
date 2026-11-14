import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, r'quotients abéliens : $S_3$ et $S_4$ résolubles', 'resultat', 's')
# S3 : 6 -> 3 -> 1 (marches 2, 3)
names3 = [(r'$S_3$', 6), (r'$A_3$', 3), (r'$1$', 1)]
steps3 = [6 // 3, 3 // 1]
for i, (n, o) in enumerate(names3):
    box(ax, 4 + i * 30, 38, 20, 14, 'sujet', label=n + '\n' + str(o), size='s')
for i, s in enumerate(steps3):
    arrow(ax, (24 + i * 30, 45), (34 + i * 30, 45), 'varie')
    text(ax, 29 + i * 30, 49, str(s), 'varie', 's')
# S4 : 24 -> 12 -> 4 -> 1 (marches 2, 3, 4)
names4 = [(r'$S_4$', 24), (r'$A_4$', 12), (r'$V$', 4), (r'$1$', 1)]
steps4 = [24 // 12, 12 // 4, 4 // 1]
for i, (n, o) in enumerate(names4):
    box(ax, 3 + i * 22, 14, 16, 14, 'sujet', label=n + '\n' + str(o), size='s')
for i, s in enumerate(steps4):
    arrow(ax, (19 + i * 22, 21), (25 + i * 22, 21), 'varie')
    text(ax, 22 + i * 22, 25.5, str(s), 'varie', 's')
text(ax, 44, 5, "sous le nom : nombre d’éléments\nsur la flèche : taille de la marche", 'fixe', 's')
save(fig, '65-107')
