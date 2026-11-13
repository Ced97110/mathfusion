import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 59, 'x = 90° : cos = 0, sin = 1', 'encre', 's')
box(ax, 2, 6, 40, 44, 'resultat')
box(ax, 46, 6, 40, 44, 'limite')
for x0, role, rows in ((22, 'resultat', ['équation de départ', 'cos x + 2 cos x sin x', '= 0 + 2 × 0 × 1', '= 0 : vrai']),
                       (66, 'limite', ['après ÷ cos x', '1 + 2 sin x', '= 1 + 2 × 1 = 3', '3 ≠ 0 : faux'])):
    for i, s in enumerate(rows):
        text(ax, x0, 43 - i * 10, s, role, 's', weight='bold' if i in (0, 3) else 'normal')
save(fig, '32-123')
