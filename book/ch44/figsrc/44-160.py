import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
bw, bh, x0 = 66, 15, 11
ys = [68, 38, 8]
box(ax, x0, ys[0], bw, bh, 'fixe', label='Entiers : les règles sont vraies')
box(ax, x0, ys[1], bw, bh, 'varie', label='Le reste ne dépend pas\ndu représentant', weight='bold')
box(ax, x0, ys[2], bw, bh, 'resultat', label='Mêmes règles sur les classes')
ax_ = 16
arrow(ax, (ax_, ys[0]), (ax_, ys[1] + bh), 'fixe')
arrow(ax, (ax_, ys[1]), (ax_, ys[2] + bh), 'fixe')
text(ax, 6, ys[0] + 7.5, 'départ', 'fixe', 's', ha='left')
text(ax, 6, ys[2] + 7.5, 'arrivée', 'resultat', 's', ha='left')
text(ax, 56, 59, 'étape qui porte tout', 'varie', 's')
text(ax, 54, 33, r'mod 5 : $7+4=11$, reste 1', 'varie', 's')
text(ax, 54, 27, r'mod 5 : $2+4=6$, reste 1', 'varie', 's')
save(fig, '44-160')
