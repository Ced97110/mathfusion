import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
xs = [3, 33, 63]
w, h = 22, 10
text(ax, xs[0] + w / 2, 60, 'produit', 'sujet', 'm', weight='bold')
text(ax, xs[1] + w / 2, 60, 'plus haut\n$(k_1,\\,k_2)$', 'autre', 'm', weight='bold')
text(ax, xs[2] + w / 2, 60, 'on retrouve\n$(d_1,\\,d_2)$', 'resultat', 'm', weight='bold')
rows = [(40, r'$e_1^2$', '(2, 0)', '(2, 0)'),
        (26, r'$e_2$', '(1, 1)', '(0, 1)'),
        (12, r'$e_1e_2$', '(2, 1)', '(1, 1)')]
for y, p, k, d in rows:
    box(ax, xs[0], y, w, h, 'sujet', label=p)
    box(ax, xs[1], y, w, h, 'autre', label=k)
    box(ax, xs[2], y, w, h, 'resultat', label=d)
    arrow(ax, (xs[0] + w + 1, y + h / 2), (xs[1] - 1, y + h / 2), 'varie')
    arrow(ax, (xs[1] + w + 1, y + h / 2), (xs[2] - 1, y + h / 2), 'varie')
text(ax, 44, 3.5, r'$d_2=k_2$ ,   $d_1=k_1-k_2$', 'varie', 'm')
save(fig, '55-102')
