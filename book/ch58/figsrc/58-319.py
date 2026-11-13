import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# un couple d'entiers (x1, x2), multiplié par 3 donne (0, 0)
text(ax, 44, 66, 'dans ℤ², si 3 × (x₁, x₂) = (0, 0)', 'encre', 's')
xs = (20, 52)
box(ax, xs[0] - 12, 48, 24, 10, 'sujet', label='x₁', size='m')
box(ax, xs[1] - 12, 48, 24, 10, 'sujet', label='x₂', size='m')
for x in xs:
    arrow(ax, (x, 48), (x, 39), 'varie')
    text(ax, x + 3, 43.5, '× 3', 'varie', 's', ha='left')
box(ax, xs[0] - 12, 29, 24, 10, 'varie', label='3x₁ = 0', size='m')
box(ax, xs[1] - 12, 29, 24, 10, 'varie', label='3x₂ = 0', size='m')
for x in xs:
    arrow(ax, (x, 29), (x, 20), 'resultat')
text(ax, 44, 24.5, '3 ≠ 0 donc :', 'fixe', 's')
box(ax, xs[0] - 12, 10, 24, 10, 'resultat', label='x₁ = 0', size='m')
box(ax, xs[1] - 12, 10, 24, 10, 'resultat', label='x₂ = 0', size='m')
text(ax, 44, 4.5, 'le couple est (0, 0) : pas de torsion', 'resultat', 's')
save(fig, '58-319')
