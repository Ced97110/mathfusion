import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
xs = [16, 44, 72]
text(ax, 44, 56, 'premier nombre', 'varie', 's')
for x, a in zip(xs, ['1', '0', '−1']):
    box(ax, x - 8, 41, 16, 9, 'varie', label=a)
for i in range(2):
    arrow(ax, (xs[i] + 9, 45.5), (xs[i + 1] - 9, 45.5), 'varie')
    text(ax, (xs[i] + xs[i + 1]) / 2, 49, '−1', 'varie', 's')
for x, a, r in zip(xs, ['−2', '0', '2'], ['sujet', 'resultat', 'sujet']):
    arrow(ax, (x, 40), (x, 28), 'fixe')
    box(ax, x - 8, 18, 16, 9, r, label=a)
text(ax, 44, 12, 'produits par −2', 'sujet', 's')
text(ax, 44, 6, 'le produit passe par 0', 'resultat', 's')
save(fig, '13-129')
