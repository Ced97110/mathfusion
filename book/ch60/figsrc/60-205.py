import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, 'faut-il encore réduire ?', 'encre', 'm')
x0, ytop, cw, ch = 18, 60, 26, 12
cells = [['λ − 1', '0'], ['0', '(λ − 1)(λ + 1)']]
for r in range(2):
    for c in range(2):
        box(ax, x0 + c * cw, ytop - (r + 1) * ch, cw, ch, 'sujet' if r == c else 'fixe', label=cells[r][c], size='s' if r == c else 'm')
for sgn, xx in ((-1, x0 - 1.5), (1, x0 + 2 * cw + 1.5)):
    line(ax, [(xx - sgn * 1.5, ytop + 0.5), (xx, ytop + 0.5), (xx, ytop - 2 * ch - 0.5), (xx - sgn * 1.5, ytop - 2 * ch - 0.5)], 'encre', lw=0.9)
for y, s in ((28, '✓ hors diagonale : des 0'), (21, '✓ λ − 1 divise (λ−1)(λ+1)'), (14, '✓ coefficient dominant 1')):
    text(ax, 14, y, s, 'resultat', 's', ha='left')
text(ax, 44, 5, 'arrêt : aucune opération', 'resultat', 'm', weight='bold')
save(fig, '60-205')
