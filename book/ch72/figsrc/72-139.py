import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
rows = [(r'dimension $n$', 62, 'sujet'), (r'$n-1$', 46, 'sujet'), (r'$n-2$', 30, 'sujet'), ('0', 10, 'resultat')]
ys = [70, 52, 34, 14]
for (lab, w, role), y in zip(rows, ys):
    box(ax, 4, y, w, 10, role, label=lab, size='m')
for y0, y1 in zip(ys[:-1], ys[1:]):
    arrow(ax, (16, y0 - 0.5), (16, y1 + 10.5), 'varie')
text(ax, 20, 64, '1 réflexion en moins', 'varie', 's', ha='left')
text(ax, 20, 46, '1 réflexion en moins', 'varie', 's', ha='left')
text(ax, 20, 28, '… jusqu’à la dimension 0', 'varie', 's', ha='left')
text(ax, 26, 9, '0 réflexion : ne rien faire', 'resultat', 's', ha='left') if False else None
text(ax, 24, 19, 'ne rien faire', 'resultat', 's', ha='left')
text(ax, 24, 8, '= produit de 0 réflexion', 'resultat', 's', ha='left')
save(fig, '72-139')
