import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'A = (2 1 ; 0 2),  r = 2,  u = e₂', 'encre', 's')
# T applique a u
box(ax, 2, 40, 18, 12, 'sujet', label='u = e₂', size='s')
arrow(ax, (21, 46), (31, 46), 'varie')
text(ax, 26, 50, 'T', 'varie', 's', weight='bold')
box(ax, 32, 40, 24, 12, 'fixe', label='r·u = 2·e₂', size='s')
text(ax, 59, 46, '+', 'encre', 'm')
box(ax, 62, 40, 24, 12, 'varie', label='(λ − r)u = e₁', size='s')
brace(ax, 34, 84, 39, 'resultat', label='T e₂ = 2·e₂ + e₁', size='s')
# la chaine
text(ax, 44, 27, 'chaîne : e₂ → e₁ → 0', 'encre', 's')
xs = [6, 37, 68]
for x, lab, role in zip(xs, ['e₂', 'e₁', '0'], ['sujet', 'varie', 'resultat']):
    box(ax, x, 6, 14, 10, role, label=lab, size='s')
for i in range(2):
    arrow(ax, (xs[i] + 15, 11), (xs[i + 1] - 1, 11), 'varie')
    text(ax, (xs[i] + xs[i + 1] + 14) / 2, 15.5, '(λ − 2)', 'varie', 's')
save(fig, '60-181')
