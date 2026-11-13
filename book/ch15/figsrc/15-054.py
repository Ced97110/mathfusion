import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 3, 66, 40, 7, 'resultat', label='aucune lettre en bas', size='s')
box(ax, 46, 66, 39, 7, 'resultat', label='exposants entiers ≥ 0', size='s')
# (y, height, expression, terms, letters, which counter differs)
rows = [(46, 10, r'$3x^4$', '1 terme', '1 lettre', None),
        (26, 14, r'$\frac{2}{5}x^2y^6$', '1 terme', '2 lettres', 1),
        (6, 10, r'$5x^3 + 3x^2 - 2x + 1$', '4 termes', '1 lettre', 0)]
for y, h, e, t, l, d in rows:
    arrow(ax, (24, 65), (24, y + h + 1), 'resultat', lw=0.4) if False else None
    text(ax, 4.5, y + h / 2, '✓', 'resultat', 'l', weight='bold')
    box(ax, 8, y, 48, h, 'sujet', label=e, size='s')
    ym = y + h / 2 - 4
    box(ax, 58, ym, 13, 8, 'varie' if d == 0 else 'fixe', label=t, size='s')
    box(ax, 72, ym, 14, 8, 'varie' if d == 1 else 'fixe', label=l, size='s')
save(fig, '15-054')
