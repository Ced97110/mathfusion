import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [8, 37, 66]
for x, lab, role in zip(xs, ['e₂', 'e₁', '0'], ['sujet', 'sujet', 'resultat']):
    box(ax, x, 42, 16, 11, role, label=lab, size='m')
for i in range(2):
    arrow(ax, (xs[i] + 17, 47.5), (xs[i + 1] - 1, 47.5), 'varie')
    text(ax, (xs[i] + xs[i + 1] + 16) / 2, 56.5, str(i + 1), 'varie', 'm', weight='bold')
brace(ax, xs[0] + 8, xs[2] + 8, 40, 'varie', label='une chaîne : 2 flèches', size='s')
arrow(ax, (26, 30), (18, 25), 'fixe')
arrow(ax, (62, 30), (70, 25), 'fixe')
box(ax, 3, 6, 38, 18, 'sujet', label='diviseur élémentaire\n(λ − 2)²', size='s')
text(ax, 44, 15, '=', 'resultat', 'l', weight='bold')
box(ax, 47, 6, 38, 18, 'autre', label='polynôme minimal\n(λ − 2)²', size='s')
save(fig, '60-186')
