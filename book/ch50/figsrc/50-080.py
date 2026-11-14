import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
text(ax, 44, 92, r'$G$ = $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ : 4 éléments', 'encre', 's')
cw = 9; gap = 1.2; x0 = 8
for i, n in enumerate(['$e$', '$a$', '$b$', '$c$']):
    text(ax, x0 + i * (cw + gap) + cw / 2, 85, n, 'encre', 's')
def row(y, members):
    for i in range(4):
        box(ax, x0 + i * (cw + gap), y, cw, 10, 'autre' if i in members else 'fixe', r=0.5)
# P = G : the 2-Sylow (4 = 2^2 elements)
row(71, {0, 1, 2, 3})
text(ax, 52, 76, r'$N(P)=G$', 'resultat', 's', ha='left')
text(ax, 52, 71.5, r'$n_2 = 1$', 'resultat', 's', ha='left')
text(ax, 4, 66, r'$P = G$ : le 2-Sylow', 'resultat', 's', ha='left')
# P of order 2 : not a Sylow subgroup
text(ax, 4, 58, r'$P$ de 2 éléments : pas Sylow', 'limite', 's', ha='left')
for r, k in enumerate((1, 2, 3)):
    y = 42 - r * 14
    row(y, {0, k})
    text(ax, 52, y + 5, r'$N(P)=G$', 'sujet', 's', ha='left')
text(ax, 44, 6, '3 sous-groupes de 2 éléments', 'limite', 's', weight='bold')
save(fig, '50-080')
