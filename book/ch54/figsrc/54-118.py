import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
rows = [(84, r'$R[x_1]$'), (62, r'$R[x_1,x_2]$'), (40, r'$R[x_1,x_2,x_3]$'), (8, r'$R[x_1,\ldots,x_r]$')]
bx, bw, bh = 6, 40, 9
for y, lab in rows:
    box(ax, bx, y, bw, bh, 'sujet', label=lab)
steps = [(84, 62 + bh, r'$+\,x_2$'), (62, 40 + bh, r'$+\,x_3$')]
for ya, yb, lab in steps:
    arrow(ax, (bx + bw / 2, ya), (bx + bw / 2, yb + 0.5), 'varie')
    text(ax, bx + bw / 2 + 12, (ya + yb + bh) / 2, lab, 'varie', 's')
arrow(ax, (bx + bw / 2, 40), (bx + bw / 2, 31), 'varie')
text(ax, bx + bw / 2, 27, '⋮', 'fixe', 'l')
arrow(ax, (bx + bw / 2, 23), (bx + bw / 2, 8 + bh + 0.5), 'varie')
text(ax, bx + bw / 2 + 12, 21.5, r'$+\,x_r$', 'varie', 's')
text(ax, 50, 88.5, 'départ : une indéterminée', 'fixe', 's', ha='left')
text(ax, 50, 51, 'règle de passage :', 'varie', 's', ha='left')
text(ax, 50, 46.5, 'ajouter une lettre', 'varie', 's', ha='left')
save(fig, '54-118')
