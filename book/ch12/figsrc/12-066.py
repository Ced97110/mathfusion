import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rings = [('fixe', 'ℝ'), ('autre', 'ℚ'), ('varie', 'ℤ'), ('sujet', 'ℕ')]
for k, (role, s) in enumerate(rings):
    x = 2 + 8 * k; w = 84 - 16 * k; y = 4 + 4 * k; top = 60 - 8 * k
    box(ax, x, y, w, top - y, role, r=1.2)
    text(ax, x + 3, top - 4, f'3 ∈ {s}', role, 's', ha='left')
line(ax, [(44, 27), (44, 58)], 'resultat', dash=True)
disc(ax, 44, 23, 4, 'resultat', label='3')
save(fig, '12-066')
