import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
rows = [(8, 1, '8 ≤ 8 : vrai', True), (8, 0, '8 ≤ 3 : faux', False), (2, 0, '2 ≤ 3 : vrai', True)]
text(ax, 44, 61, r'$x \leq 5y + 3$', 'sujet', 'l', weight='bold')
brace(ax, 2, 50, 47, 'fixe', label='un couple : deux nombres', down=False)
for i, (x, y, res, ok) in enumerate(rows):
    yy = 32 - 14 * i + 4
    role = 'resultat' if ok else 'limite'
    box(ax, 2, yy, 22, 10, 'sujet', label=f'$x = {x}$')
    box(ax, 28, yy, 22, 10, 'autre', label=f'$y = {y}$')
    arrow(ax, (50, yy + 5), (56, yy + 5), 'fixe')
    box(ax, 56, yy, 30, 10, role, label=res, size='s')
save(fig, '17-031')
