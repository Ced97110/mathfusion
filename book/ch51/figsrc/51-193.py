import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx = [52, 74]
text(ax, cx[0], 56, 'diviser', 'encre', 's'); text(ax, cx[1], 56, 'ordre libre', 'encre', 's')
rows = [('ℚ fractions', 1, 1), ('ℝ réels', 1, 1), ('ℂ complexes', 1, 1), ('ℍ quaternions', 1, 0)]
for i, (nm, d, o) in enumerate(rows):
    y = 44 - i*11
    last = (i == 3)
    box(ax, 2, y - 4.5, 36, 9, 'sujet' if last else 'fixe', label=nm, size='m')
    for x, v in zip(cx, (d, o)):
        text(ax, x, y, '✓' if v else '✗', 'resultat' if v else 'limite', 'l', weight='bold')
    if last: box(ax, 42, y - 5, 44, 10, 'sujet', fill=False, lw=1.2, r=1.5)
text(ax, 44, 2.5, 'deux propriétés indépendantes', 'sujet', 's')
save(fig, '51-193')
