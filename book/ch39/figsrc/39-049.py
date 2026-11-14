import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# (2 + 3i)(1 - 2i) : quatre produits, puis regroupement
fig, ax = canvas(72)
x0, cw, ch = 20, 31, 12
cols = [x0, x0 + cw + 3]
rows = [44, 30]
text(ax, 8, 61, '×', 'fixe', 'm')
for cx, s, role in zip(cols, ['1', '−2i'], ['sujet', 'varie']):
    text(ax, cx + cw / 2, 61, s, role, 'l')
for ry, s, role in zip(rows, ['2', '3i'], ['sujet', 'varie']):
    text(ax, 12, ry + ch / 2, s, role, 'l')
cells = [(0, 0, '2 × 1 = 2', 'sujet'), (1, 0, '2 × (−2i) = −4i', 'varie'),
         (0, 1, '3i × 1 = 3i', 'varie'), (1, 1, '3i × (−2i) = −6i²\n= +6', 'sujet')]
for c, r, s, role in cells:
    box(ax, cols[c], rows[r], cw, ch, role, label=s, size='s')
box(ax, 4, 10, 38, 9, 'sujet', label='réel : 2 + 6 = 8', size='s')
box(ax, 46, 10, 38, 9, 'varie', label='en i : −4i + 3i = −i', size='s')
text(ax, 44, 3.5, '(2 + 3i)(1 − 2i) = 8 − i', 'resultat', 'm', weight='bold')
save(fig, '39-049')
