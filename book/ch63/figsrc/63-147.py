import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
text(ax, 44, 48, '(στ)(x) = σ(τ(x))', 'sujet', 'l', weight='bold')
xs = [2, 33, 64]
for x, t, r in zip(xs, ['x = r', 'τ(r) = r', 'σ(r) = jr'], ['sujet', 'fixe', 'resultat']):
    box(ax, x, 24, 22, 11, role=r, label=t)
for i, (l, sub) in enumerate([('τ', '1er'), ('σ', '2e')]):
    arrow(ax, (xs[i] + 22.8, 29.5), (xs[i + 1] - 0.8, 29.5), 'varie')
    text(ax, xs[i] + 22 + 5.1, 33, l, 'varie', 's')
    text(ax, xs[i] + 22 + 5.1, 25.5, sub, 'varie', 's')
text(ax, 44, 14, '(στ)(r) = σ(τ(r)) = jr', 'resultat', 'm', weight='bold')
text(ax, 44, 6, 'on lit de droite à gauche', 'encre', 's')
save(fig, '63-147')
