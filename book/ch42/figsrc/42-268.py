import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 21, 70, r'$S$', 'sujet', 'l'); text(ax, 66, 70, '{oui, non}', 'encre', 's')
ys = [56, 42, 28]
for y, l in zip(ys, 'abc'): box(ax, 14, y, 14, 9, 'sujet', label=l)
box(ax, 56, 52, 20, 9, 'resultat', label='oui'); box(ax, 56, 32, 20, 9, 'limite', label='non')
for y, ty in zip(ys, (56.5, 36.5, 56.5)): arrow(ax, (28, y + 4.5), (56, ty), 'varie')
text(ax, 44, 18, 'chaque objet : 2 choix', 'varie', 's')
box(ax, 14, 4, 60, 9, 'resultat', label=r'$2 \times 2 \times 2 = 8$ sacs')
save(fig, '42-268')
