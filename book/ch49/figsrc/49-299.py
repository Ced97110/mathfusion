import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 20, 66, 'groupe abstrait', 'sujet', 'm', weight='bold')
for i in range(8):
    r, c = divmod(i, 2)
    disc(ax, 13 + c * 14, 54 - r * 10, 3.4, 'varie' if i == 5 else 'sujet')
text(ax, 20, 8, '8 éléments + produit', 'sujet', 's')
text(ax, 20, 14, 'un élément : $g$', 'varie', 's')
arrow(ax, (36, 38), (47, 38), 'varie')
text(ax, 41.5, 43, 'action', 'varie', 's')
text(ax, 67, 66, 'transformations', 'resultat', 'm', weight='bold')
P = [(57, 28), (77, 28), (77, 48), (57, 48)]
poly(ax, P, 'fixe')
for i, p in enumerate(P):
    disc(ax, p[0], p[1], 3.6, 'sujet', label=str(i + 1))
for i in range(4):
    a, b = P[i], P[(i + 1) % 4]
    d = math.hypot(b[0]-a[0], b[1]-a[1]); u = ((b[0]-a[0])/d, (b[1]-a[1])/d)
    arrow(ax, (a[0]+u[0]*5, a[1]+u[1]*5), (b[0]-u[0]*5, b[1]-u[1]*5), 'varie')
text(ax, 67, 20, 'g : quart de tour', 'varie', 's')
text(ax, 67, 8, '8 symétries du carré', 'resultat', 's')
save(fig, '49-299')
