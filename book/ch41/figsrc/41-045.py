import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# 41-045 : méthode v/‖v‖ : v = ⟨5 ; −12⟩ de norme 13 -> on divise par 13 -> norme 1 (13 cases de 4 mm, puis 1 case)
fig, ax = canvas(92)
c = 4.0
x0 = 18
box(ax, 14, 76, 60, 12, 'sujet', label=r'$v = \langle$5 ; −12$\rangle$', size='m')
# 1) la norme : 13 cases
yb = 56
for k in range(13):
    ax.add_patch(Rectangle((x0 + k * c, yb), c, 6, ec=COL['sujet'], fc=FILL['sujet'], lw=0.6, zorder=2))
brace(ax, x0, x0 + 13 * c, yb + 7, 'sujet', label='norme 13', down=False)
arrow(ax, (44, 75.4), (44, 70.6), 'fixe', lw=0.9)
# 2) diviser par 13 : il reste une case
arrow(ax, (x0 + 2, 53), (x0 + 2, 40), 'varie', lw=1.6)
text(ax, x0 + 5, 47, '÷ 13', 'varie', 'l', ha='left', weight='bold')
text(ax, x0 + 28, 47, 'chaque composante', 'varie', 's', ha='left')
ax.add_patch(Rectangle((x0, 30), c, 6, ec=COL['resultat'], fc=FILL['resultat'], lw=0.8, zorder=2))
text(ax, x0 + c + 3, 33, 'norme 1', 'resultat', 'm', ha='left')
# 3) résultat
arrow(ax, (44, 27.5), (44, 22.5), 'fixe', lw=0.9)
box(ax, 8, 8, 72, 13, 'resultat', label=r'$v/\|v\| = \langle$5/13 ; −12/13$\rangle$', size='m')
save(fig, '41-045')
