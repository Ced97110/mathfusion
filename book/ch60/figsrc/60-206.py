import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, r'$P\,(\lambda1-A)\,Q=$', 'encre', 'm')
text(ax, 44, 72, r'$P,\ Q$ : matrices inversibles', 'encre', 's')
x0, ytop, cw, ch = 11, 66, 22, 9
diag = ['1', 'λ − 1', '(λ − 1)²']
for r in range(3):
    for c in range(3):
        box(ax, x0 + c * cw, ytop - (r + 1) * ch, cw, ch, 'sujet' if r == c else 'fixe',
            label=diag[r] if r == c else '0', size='m')
for sgn, xx in ((-1, x0 - 1.5), (1, x0 + 3 * cw + 1.5)):
    line(ax, [(xx - sgn * 1.5, ytop + 0.5), (xx, ytop + 0.5), (xx, ytop - 3 * ch - 0.5), (xx - sgn * 1.5, ytop - 3 * ch - 0.5)], 'encre', lw=0.9)
# la diagonale lue en ligne : chaque case divise la suivante
yb = 20
for c in range(3):
    xc = x0 + c * cw + cw / 2
    box(ax, xc - 7, yb - 5, 14, 10, 'sujet', label=diag[c], size='s')
for c in range(2):
    xa = x0 + c * cw + cw / 2 + 7.3
    xb = x0 + (c + 1) * cw + cw / 2 - 7.3
    arrow(ax, (xa, yb), (xb, yb), 'varie')
    text(ax, (xa + xb) / 2, yb + 7, "divise", 'varie', 's')
text(ax, 44, 8, 'chaque case divise la suivante', 'varie', 's')
save(fig, '60-206')
