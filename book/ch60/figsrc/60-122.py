import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'Six rangements de trois objets', 'encre', 'm', weight='bold')
text(ax, 44, 54, 'éléments d’ordre 1 ou 2', 'sujet', 's')
labels = ['identité', '(1 2)', '(1 3)', '(2 3)']
bw, gap = 17, 2.5
x0 = 44 - (4 * bw + 3 * gap) / 2
cx = []
for i, l in enumerate(labels):
    box(ax, x0 + i * (bw + gap), 40, bw, 9, 'sujet', label=l, size='s')
    cx.append(x0 + i * (bw + gap) + bw / 2)
# products of two exchanges
arrow(ax, (cx[1], 39), (40, 28.5), 'varie')
arrow(ax, (cx[2], 39), (48, 28.5), 'varie')
text(ax, 21, 33, 'produit de deux', 'varie', 's')
text(ax, 21, 29.5, 'échanges', 'varie', 's')
box(ax, 22, 15, 44, 12, 'limite', label='ordre 3', size='m')
text(ax, 44, 9, 'hors de l’ensemble :', 'limite', 's')
text(ax, 44, 4.5, 'il n’est pas stable', 'limite', 's')
save(fig, '60-122')
