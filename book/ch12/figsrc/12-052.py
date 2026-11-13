import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
exprs = ['2{3[4(17 − 11)]}', '2{3[4 · 6]}', '2{3 · 24}', '2 · 72', '144']
calcs = ['17 − 11 = 6', '4 · 6 = 24', '3 · 24 = 72', '2 · 72 = 144']
ys = [55, 43, 31, 19, 7]
for i, (y, s) in enumerate(zip(ys, exprs)):
    role = 'sujet' if i == 0 else 'resultat' if i == 4 else 'fixe'
    box(ax, 3, y, 38, 8, role, label=s, size='m')
    if i < 4: arrow(ax, (22, y - 0.3), (22, y - 3.7), 'fixe')
    if i > 0:
        box(ax, 52, y, 33, 8, 'varie', label=calcs[i - 1], size='m')
        arrow(ax, (51.5, y + 4), (42, y + 4), 'varie')
text(ax, 68, 59, 'd\'abord l\'intérieur', 'varie', 's')
save(fig, '12-052')
