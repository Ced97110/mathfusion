import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# 41-046 : ⟨5 ; −12⟩ : 25 + 144 = 169 (carrés de côtés 5, 12, 13 à 1,4 mm par unité), norme 13, vecteur unitaire de norme 1
fig, ax = canvas(80)
k = 1.4
yb = 52
sq = [(4, 5, 'fixe', '25', '5²'), (22, 12, 'fixe', '144', '12²'), (52, 13, 'resultat', '169', '13²')]
for x, n, role, area, name in sq:
    ax.add_patch(Rectangle((x, yb), n * k, n * k, ec=COL[role], fc=FILL[role], lw=0.9, zorder=2))
    text(ax, x + n * k / 2, yb + n * k / 2, area, role, 's')
    text(ax, x + n * k / 2, yb - 3.5, name, role, 's')
text(ax, 15.5, yb + 3.5, '+', 'encre', 'l')
text(ax, 43, yb + 3.5, '=', 'encre', 'l')
box(ax, 8, 28, 72, 11, 'sujet', label='norme = √169 = 13', size='m')
box(ax, 8, 14, 72, 11, 'resultat', label=r'$\langle$5/13 ; −12/13$\rangle$', size='m')
text(ax, 44, 6, 'norme : 13 ÷ 13 = 1', 'resultat', 's')
arrow(ax, (44, 42), (44, 39.8), 'fixe', lw=0.9)
arrow(ax, (44, 27.5), (44, 25.3), 'fixe', lw=0.9)
save(fig, '41-046')
