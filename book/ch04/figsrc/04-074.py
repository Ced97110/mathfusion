import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(54)
for cx, lab, role in [(10.5, '7³', 'sujet'), (33, '7²', 'sujet'), (55.5, '7¹', 'sujet'), (78, '7⁰', 'resultat')]:
    text(ax, cx, 44, lab, role, 'm')
for x0, lab in [(4, '343'), (26.5, '49'), (49, '7')]:
    box(ax, x0, 28, 13, 10, 'sujet', fill=False, label=lab, size='l')
arrow(ax, (17, 33), (26.5, 33), 'varie')
arrow(ax, (39.5, 33), (49, 33), 'varie')
text(ax, 21.75, 37, '÷ 7', 'varie', 's')
text(ax, 44.25, 37, '÷ 7', 'varie', 's')
ax.add_patch(FancyArrowPatch((62, 33), (71.5, 33), arrowstyle='-|>', mutation_scale=7, lw=1.0,
             color=COL['varie'], linestyle='--', shrinkA=0, shrinkB=0, zorder=4))
text(ax, 66.5, 41, '7 ÷ 7 = 1', 'varie', 's')
box(ax, 71.5, 28, 13, 10, 'resultat', fill=False, dash=True, label='1', size='l')
text(ax, 78, 21, 'on pose', 'resultat', 's')
brace(ax, 4, 62, 25, 'fixe', label='donnés par la répétition', down=True, size='s')
brace(ax, 4, 84.5, 13, 'varie', label='même pas ÷ 7 jusqu’à 7⁰', down=True, size='s')
save(fig, '04-074')
