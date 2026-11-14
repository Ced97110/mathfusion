import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 16, 57, 'diviseurs élémentaires', 'sujet', 's')
text(ax, 64, 57, 'forme de Jordan', 'sujet', 's')
for y in (40, 14):
    box(ax, 3, y, 26, 10, 'sujet', label=r'$(\lambda-2)^1$')
c = 14
for i in range(2):
    for j in range(2):
        d = i == j
        box(ax, 50 + j * c, 36 - i * c, c - 0.8, c - 0.8, 'sujet' if d else 'fixe', label='2' if d else '0')
arrow(ax, (30, 45), (49, 43), 'varie')
arrow(ax, (30, 17), (71, 21.5), 'varie', curve=0.0)
text(ax, 64, 15, 'deux blocs de taille 1', 'resultat', 's')
save(fig, '60-250')
