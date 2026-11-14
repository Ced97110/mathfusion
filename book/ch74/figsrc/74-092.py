import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
s = 11
A = [['0', '−1'], ['1', '0']]
T = [['0', '1'], ['−1', '0']]
ax0, tx0, y0 = 20, 58, 14
for r in range(2):
    for c in range(2):
        box(ax, ax0 + c*s, y0 + (1 - r)*s, s, s, 'varie' if r == 0 else 'sujet', label=A[r][c])
        box(ax, tx0 + c*s, y0 + (1 - r)*s, s, s, 'varie' if c == 0 else 'sujet', label=T[r][c])
text(ax, 11, y0 + 1.5*s, 'ligne 1', 'varie', 's')
text(ax, 11, y0 + 0.5*s, 'ligne 2', 'sujet', 's')
text(ax, tx0 + 0.5*s, y0 + 2*s + 3, 'col. 1', 'varie', 's')
text(ax, tx0 + 1.5*s, y0 + 2*s + 3, 'col. 2', 'sujet', 's')
text(ax, ax0 + s, y0 - 4, r'$A$', 'encre', 'l')
text(ax, tx0 + s, y0 - 4, r'$A^t$', 'encre', 'l')
arrow(ax, (ax0 + 2*s + 3, y0 + s), (tx0 - 3, y0 + s), 'varie', lw=1.3)
text(ax, 49, y0 + s + 3.5, 'lignes', 'varie', 's')
text(ax, 49, y0 + s - 4, 'colonnes', 'varie', 's')
save(fig, '74-092')
