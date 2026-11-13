import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 24, 64, 'couples, produit 12', 'sujet', 's')
text(ax, 58, 64, 'somme', 'varie', 's')
rows = [('1 et 12', '13', 'limite'), ('2 et 6', '8', 'limite'), ('3 et 4', r'$7 = b$', 'resultat')]
for k, (c, s, r) in enumerate(rows):
    y = 46 - 14 * k
    box(ax, 8, y, 32, 10, 'sujet', label=c)
    arrow(ax, (40, y + 5), (47, y + 5), 'varie')
    box(ax, 47, y, 22, 10, r, label=s)
arrow(ax, (58, 18), (58, 12.5), 'resultat')
box(ax, 22, 2, 44, 10, 'resultat', label=r'$(x+3)(x+4)$')
save(fig, '18-068')
