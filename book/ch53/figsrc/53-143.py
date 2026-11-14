import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(78)
box(ax, 2, 62, 12, 10, 'sujet', label='22')
box(ax, 36, 62, 12, 10, 'varie', label='33')
box(ax, 72, 62, 12, 10, 'resultat', label='22')
arrow(ax, (14.5, 67), (35.5, 67), 'varie'); arrow(ax, (48.5, 67), (71.5, 67), 'varie')
text(ax, 25, 71.5, 'puissance 3', 'varie', 's')
text(ax, 60, 71.5, 'puissance 27', 'varie', 's')
text(ax, 44, 55, 'reste par 55 à chaque fois', 'fixe', 's')
# 22, 33 et 55 sont des multiples de 11
for y, n, lab in [(38, 2, '22 = 2 × 11'), (24, 3, '33 = 3 × 11'), (10, 5, '55 = 5 × 11')]:
    for k in range(n):
        ax.add_patch(Rectangle((2 + 16.5 * k, y), 16.5, 6, ec=COL['autre'], fc=FILL['autre'], lw=0.8, zorder=2))
    text(ax, 2, y + 9.5, lab, 'autre', 's', ha='left')
# le bloc de 11 commun à 33 et 55 est entouré
for y in (24, 10):
    ax.add_patch(Rectangle((2, y), 16.5, 6, ec=COL['encre'], fc='none', lw=1.8, zorder=3))
text(ax, 68, 27, 'diviseur commun : 11', 'encre', 's')
text(ax, 68, 20, 'facteur de 55 : 11', 'autre', 's')
save(fig, '53-143')
