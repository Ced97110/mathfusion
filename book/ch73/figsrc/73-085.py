import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
w, h = 12, 10
inv = [['1', '−1'], ['0', '1']]; tr = [['1', '0'], ['1', '1']]
for i in range(2):
    for j in range(2):
        diff = inv[i][j] != tr[i][j]
        y = 36 - i * h
        box(ax, 8 + j * w, y, w, h, 'limite' if diff else 'sujet', label=inv[i][j])
        box(ax, 56 + j * w, y, w, h, 'limite' if diff else 'autre', label=tr[i][j])
text(ax, 20, 51, 'inverse', 'sujet'); text(ax, 68, 51, 'transposée', 'autre')
text(ax, 44, 36, '≠', 'limite', 'xl', weight='bold')
text(ax, 44, 19, '(0, 1) devient (1, 1)', 'encre', 's')
text(ax, 44, 14, 'longueur 1 → plus de 1', 'limite', 's')
save(fig, '73-085')
