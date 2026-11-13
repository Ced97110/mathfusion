import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'décomposition unique ?', 'encre', 'm')
rows = [('entiers ℤ', '12 = 2 × 2 × 3', 'oui', 'resultat'),
        ('polynômes', 'x + 1  et  2x + 2', '?', 'fixe'),
        ('matrices', '', '?', 'fixe'),
        ('entiers modulo n', '', '?', 'fixe')]
for i, (name, ex, v, role) in enumerate(rows):
    y = 40 - i * 12
    box(ax, 3, y, 34, 9, 'sujet', label=name)
    if ex:
        box(ax, 40, y, 34, 9, 'fixe', label=ex, size='s')
    box(ax, 77, y, 9, 9, role, label=v, dash=(role == 'fixe'))
save(fig, '56-002')
