import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
m, n, s, x0, y0 = 2, 3, 12.0, 30.0, 18.0
for k in range(6):
    i, j = k % m, k % n
    hl = (k == 5)
    box(ax, x0 + j * s, y0 + (m - 1 - i) * s, s, s, 'varie' if hl else 'sujet', label=str(k), size='m', r=0.6, weight='bold' if hl else 'normal')
for i in range(m): text(ax, x0 - 2, y0 + (m - 1 - i) * s + s / 2, f'mod 2 = {i}', 'sujet', 's', ha='right')
for j in range(n): text(ax, x0 + j * s + s / 2, y0 + m * s + 3, f'{j}', 'autre', 'm')
text(ax, x0 - 2, y0 + m * s + 3, 'par 2 ↓', 'fixe', 's', ha='right') if False else None
text(ax, x0 + 18, y0 + m * s + 8, 'mod 3', 'autre', 's')
text(ax, 44, 59, r'$k\mapsto(k\ \mathrm{mod}\ 2,\ k\ \mathrm{mod}\ 3)$', 'encre', 'm')
text(ax, 44, 10, 'le nombre 5 va en (1, 2)', 'varie', 'm')
save(fig, '45-198')
