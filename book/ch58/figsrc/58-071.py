import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, rows, role='encre', hw=7.5, dy=7.0):
    h = len(rows) * dy / 2
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.6, cy + h), (x, cy + h), (x, cy - h), (x - s * 1.6, cy - h)], 'fixe', lw=0.9)
    for i, r in enumerate(rows):
        text(ax, cx, cy + h - dy / 2 - i * dy, r, role, 'm')

fig, ax = canvas(46)
mat(ax, 14, 30, ['1   0', '1   1'], 'sujet')
mat(ax, 44, 30, ['2   1', '1   3'], 'autre')
mat(ax, 74, 30, ['2   1', '3   4'], 'resultat')
text(ax, 29, 30, '×', 'encre', 'l'); text(ax, 59, 30, '=', 'encre', 'l')
text(ax, 14, 16, 'B : det = 1', 'sujet', 's')
text(ax, 44, 16, 'A : det = 5', 'autre', 's')
text(ax, 74, 16, 'BA : det = 5', 'resultat', 's')
text(ax, 44, 6, '5 = 1 × 5', 'resultat', 'm')
save(fig, '58-071')
