import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 2, 8, 42, 42, 'fixe', fill=False, dash=True); text(ax, 23, 55, r'$S$ : 12 éléments', 'encre', 'm')
groups = [(4, 'sujet', 'A', 16, 'point'), (5, 'varie', 'B', 15, 'points'), (3, 'resultat', 'C', 3, 'points')]
for gi, (n, rl, lab, _, _) in enumerate(groups):
    for i in range(n): disc(ax, 8 + i * 8, 44 - gi * 12, 2.2, rl)
# fix grouping rows: rows of 4 -> A row0, B spans rows 1-2 (kept by order)
box(ax, 54, 8, 32, 42, 'fixe', fill=False, dash=True); text(ax, 70, 55, r'$S/E$ : 3 éléments', 'encre', 'm')
for i, (n, rl, lab, _, _) in enumerate(groups):
    yy = 38 - i * 13
    box(ax, 57, yy, 26, 10, rl, label=f'{lab} : {n} points', size='s')
arrow(ax, (46, 29), (52, 29), 'varie'); 
save(fig, '43-078')
