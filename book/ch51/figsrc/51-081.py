import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'couples $(2,\ 3)$ et $(4,\ 5)$', 'sujet', 'm')
cols = [(14, 47, 'première place'), (52, 85, 'seconde place')]
for x0, x1, t in cols:
    text(ax, (x0 + x1) / 2, 58, t, 'fixe', 's')
line(ax, [(49.5, 24), (49.5, 62)], 'fixe', dash=True)
rows = [(44, 'somme', ['2 + 4 = 6', '3 + 5 = 8']), (28, 'produit', [r'2 $\times$ 4 = 8', r'3 $\times$ 5 = 15'])]
for y, name, cells in rows:
    text(ax, 2, y + 5, name, 'varie', 's', ha='left')
    for (x0, x1, _t), c in zip(cols, cells):
        box(ax, x0, y, x1 - x0, 10, 'resultat', label=c)
text(ax, 44, 17, r'somme $(6,\ 8)$ ; produit $(8,\ 15)$', 'resultat', 'm')
text(ax, 44, 8, 'chaque place se calcule seule', 'fixe', 's')
save(fig, '51-081')
