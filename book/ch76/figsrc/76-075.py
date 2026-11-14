import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 22, 48, 'niveau 1', 'encre', 's'); text(ax, 66, 48, 'niveau du haut', 'encre', 's')
o = (6, 14); k = 5
line(ax, [o, (o[0] + 36, o[1])], 'fixe', dash=True)
arrow(ax, o, (o[0] + k, o[1]), 'sujet', lw=1.2)
arrow(ax, o, (o[0] + 2 * k, o[1] + k), 'varie', lw=1.2)
text(ax, o[0] + 3, o[1] - 3.5, '$e_1$', 'sujet', 's'); text(ax, o[0] + 14, o[1] + 6, '$Le_1$', 'varie', 's')
text(ax, 22, 30, 'sort de la droite', 'varie', 's')
s = 4.4
ax.add_patch(Rectangle((47, 24), s, s, ec=COL['sujet'], fc=FILL['sujet'], lw=0.6, zorder=2))
arrow(ax, (53, 26.2), (60, 26.2), 'varie')
for i in range(5): ax.add_patch(Rectangle((62 + i * s, 24), s - 0.4, s, ec=COL['resultat'], fc=FILL['resultat'], lw=0.6, zorder=2))
text(ax, 49, 19, r'$e_{12}$', 'sujet', 's'); text(ax, 74, 19, r'$5\,e_{12}$', 'resultat', 's')
text(ax, 66, 10, r'$\det L=5$', 'resultat', 'm', weight='bold')
save(fig, '76-075')
