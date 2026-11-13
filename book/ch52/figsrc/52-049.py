import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
rows = [('départ : un idéal I', 'sujet', 'I = (12, 18)'),
        ('k : plus petit positif', 'sujet', 'k = 6'),
        ('étape clé : n = qk + r', 'varie', r'$n = 18 = 3 \times 6 + 0$'),
        ('arrivée : r = 0', 'resultat', 'I = 6ℤ')]
for i, (lab, role, ex) in enumerate(rows):
    y = 62 - i * 20
    box(ax, 3, y, 42, 11, role, label=lab, size='s')
    text(ax, 66, y + 5.5, ex, 'fixe', 's')
    if i < 3: arrow(ax, (24, y), (24, y - 9), 'fixe')
text(ax, 66, 74, 'avec 12 et 18', 'fixe', 's')
save(fig, '52-049')
