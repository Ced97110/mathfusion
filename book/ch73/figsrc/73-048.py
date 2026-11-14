import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 8, 36, 72, 10, 'sujet', label=r'on multiplie à gauche par $T_{21}(-3)$', size='s')
text(ax, 44, 51, 'lignes (1, 0) et (−3, 1)', 'sujet', 's')
text(ax, 21, 29, 'avant', 'fixe', 'm'); text(ax, 69, 29, 'après', 'resultat', 'm')
rows = [('1', '(1, 2)', '(1, 2)', 'fixe'), ('2', '(3, 4)', '(0, −2)', 'varie')]
for k, (n, a, b, role) in enumerate(rows):
    y = 16 - k*12 + 6
    text(ax, 6, y, f'L{n}', 'encre', 's')
    box(ax, 12, y-4.5, 20, 9, 'fixe' if k == 0 else 'sujet', label=a)
    box(ax, 60, y-4.5, 20, 9, 'fixe' if k == 0 else 'resultat', label=b)
    arrow(ax, (33, y), (59, y), 'fixe' if k == 0 else 'varie')
text(ax, 46, 13.8, r'$L_2 - 3 \times L_1$', 'varie', 's')
save(fig, '73-048')
