import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, 'A = 2·I', 'sujet', 'm', weight='bold')
text(ax, 44, 65, r'case $(i,j)$ : $\min(n_i, n_j)$', 'encre', 's')
x0, cw, ch, ytop = 40, 22, 12, 56
# degrés en haut et à gauche
for c in range(2):
    text(ax, x0 + c * cw + cw / 2, ytop + 3, rf'$n_{c + 1}=1$', 'sujet', 'm', weight='bold')
    text(ax, x0 - 3, ytop - c * ch - ch / 2, rf'$n_{c + 1}=1$', 'sujet', 'm', weight='bold', ha='right')
for r in range(2):
    for c in range(2):
        box(ax, x0 + c * cw, ytop - (r + 1) * ch, cw, ch, 'resultat',
            label=rf'$\min(n_{r + 1},n_{c + 1})=1$', size='s')
text(ax, 44, 20, '1 + 1 + 1 + 1 = 4', 'resultat', 'l', weight='bold')
text(ax, 44, 11, '= toutes les matrices 2 × 2', 'resultat', 's')
save(fig, '60-201')
