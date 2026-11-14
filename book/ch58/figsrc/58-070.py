import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, rows, roles=None, hw=7.5, dy=7.0):
    h = len(rows) * dy / 2
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.6, cy + h), (x, cy + h), (x, cy - h), (x - s * 1.6, cy - h)], 'fixe', lw=0.9)
    for i, r in enumerate(rows):
        text(ax, cx, cy + h - dy / 2 - i * dy, r, roles[i] if roles else 'encre', 'm')

fig, ax = canvas(72)
mat(ax, 14, 56, ['3   1'], ['sujet'])
text(ax, 14, 47, 'lot (3, 1)', 'sujet', 's')
arrow(ax, (25, 56), (39, 56), 'varie')
text(ax, 32, 63, '+ ligne de zéros', 'varie', 's')
mat(ax, 50, 56, ['3   1', '0   0'], ['sujet', 'varie'])
text(ax, 75, 56, 'det(A) = 0', 'varie', 's')
text(ax, 8, 28, 'BA =', 'encre', 'm', ha='left')
mat(ax, 33, 28, ['1   0', '0   1'], ['resultat', 'resultat'])
text(ax, 61, 28, 'det = 1', 'resultat', 'm')
box(ax, 18, 4, 52, 10, 'limite', label='impossible : 0 = 1', size='m')
save(fig, '58-070')
