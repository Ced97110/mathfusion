import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# z = 2 cis 30°, w = √2 cis 45° : modules multipliés, arguments additionnés
fig, ax = canvas(56)
text(ax, 44, 51, 'zw = rs cis(θ + φ)', 'resultat', 'l', weight='bold')
xs = [16, 41, 66]
for x, s, role in zip(xs, ['z', 'w', 'zw'], ['sujet', 'autre', 'resultat']):
    text(ax, x + 9.5, 43, s, role, 'm', weight='bold')
text(ax, 8.5, 31, 'module', 'fixe', 's')
text(ax, 8.5, 14, 'argument', 'fixe', 's')
rows = [(26, ['r = 2', 's = √2', 'rs ≈ 2,83'], '×'), (9, ['θ = 30°', 'φ = 45°', 'θ + φ = 75°'], '+')]
for y, labels, op in rows:
    for x, s, role in zip(xs, labels, ['sujet', 'autre', 'resultat']):
        box(ax, x, y, 19, 10, role, label=s, size='s')
    text(ax, 38, y + 5, op, 'varie', 'l', weight='bold')
    arrow(ax, (60, y + 5), (65.6, y + 5), 'varie', lw=0.9)
save(fig, '39-065')
