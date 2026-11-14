import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# chaine
xs = [8, 37, 66]
for x, lab, role in zip(xs, ['e₂', 'e₁', '0'], ['sujet', 'varie', 'resultat']):
    box(ax, x, 52, 16, 11, role, label=lab, size='m')
for i in range(2):
    arrow(ax, (xs[i] + 17, 57.5), (xs[i + 1] - 1, 57.5), 'varie')
    text(ax, (xs[i] + xs[i + 1] + 16) / 2, 62, 'T − 2', 'varie', 's')
text(ax, 44, 44, '2 vecteurs → un bloc 2 × 2', 'encre', 's')
# matrice A
text(ax, 8, 24, 'A =', 'encre', 'm')
x0, ytop, cw, ch = 16, 36, 11, 9
rows = [[2, 1], [0, 2]]
for r in range(2):
    for c in range(2):
        role = 'sujet' if r == c else 'varie' if c == 1 else 'fixe'
        box(ax, x0 + c * cw, ytop - (r + 1) * ch, cw, ch, role, label=str(rows[r][c]), size='m')
for sgn, xx in ((-1, x0 - 1.5), (1, x0 + 2 * cw + 1.5)):
    line(ax, [(xx - sgn * 1.5, ytop + 0.5), (xx, ytop + 0.5), (xx, ytop - 2 * ch - 0.5), (xx - sgn * 1.5, ytop - 2 * ch - 0.5)], 'encre', lw=0.9)
text(ax, 44, 29.5, 'T e₁ = 2·e₁', 'sujet', 's', ha='left')
text(ax, 44, 24, 'T e₂ = e₁ + 2·e₂', 'varie', 's', ha='left')
save(fig, '60-185')
