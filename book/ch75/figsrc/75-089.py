import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
x0, y0, cw, ch = 24, 18, 14, 10
cols = [2, 3, 4, 5]; rows = [2, 4, 6]
bad = {(2, 2), (2, 3), (4, 2)}
text(ax, 44, 62, r'$PSp_{2n}(F)$ : simple ou non', 'encre', 'm')
text(ax, x0 + 2 * cw, y0 + 3 * ch + 8, r'nombre d’éléments de $F$', 'fixe', 's')
for j, c in enumerate(cols): text(ax, x0 + j * cw + cw / 2, y0 + 3 * ch + 3, str(c), 'fixe', 's')
for i, r in enumerate(rows):
    y = y0 + (2 - i) * ch
    text(ax, x0 - 3, y + ch / 2, str(r), 'fixe', 's', ha='right')
    for j, c in enumerate(cols):
        box(ax, x0 + j * cw + 0.6, y + 0.6, cw - 1.2, ch - 1.2, 'limite' if (r, c) in bad else 'resultat')
text(ax, 12, y0 + 3 * ch + 8, r'$2n$', 'fixe', 's')
box(ax, 14, 6, 6, 5, 'resultat'); text(ax, 22, 8.5, 'simple', 'resultat', 's', ha='left')
box(ax, 46, 6, 6, 5, 'limite'); text(ax, 54, 8.5, 'pas simple', 'limite', 's', ha='left')
save(fig, '75-089')
