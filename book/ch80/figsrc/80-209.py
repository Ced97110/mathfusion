import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
x0, y0, c = 28, 14, 14
text(ax, x0 + c, 58, r'$b$', 'autre', 'm')
text(ax, 16, y0 + c, r'$a$', 'sujet', 'm')
for j, bv in enumerate((0, 1)):
    text(ax, x0 + j * c * 1.0 + c / 2 - 0, 50, str(bv), 'autre', 'm') if False else None
for i, av in enumerate((0, 1)):
    for j, bv in enumerate((0, 1)):
        p = av * bv
        box(ax, x0 + j * c, y0 + (1 - i) * c, c - 1, c - 1, 'resultat' if p else 'fixe', label=f'{av}·{bv}={p}' if False else str(p), size='l')
text(ax, x0 + c / 2, y0 + 2 * c + 3, '0', 'autre', 's'); text(ax, x0 + c * 1.5, y0 + 2 * c + 3, '1', 'autre', 's')
text(ax, x0 - 4, y0 + 1.5 * c, '0', 'sujet', 's'); text(ax, x0 - 4, y0 + c / 2, '1', 'sujet', 's')
text(ax, 72, y0 + 1.5 * c, r'$ab$', 'resultat', 'm')
text(ax, 44, 5, '1 seulement si les deux valent 1', 'resultat', 's')
save(fig, '80-209')
