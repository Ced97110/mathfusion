import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(86)
# 40 cases = 13 groupes de 3 + 1 case
c = 2.1
for g in range(13):
    x = 2 + g * 3 * c
    ax.add_patch(Rectangle((x, 62), 3 * c, 8, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
    for k in (1, 2):
        ax.plot([x + k * c] * 2, [62, 70], color=COL['sujet'], lw=0.3, zorder=3)
xl = 2 + 39 * c
ax.add_patch(Rectangle((xl, 62), c, 8, ec=COL['resultat'], fc=FILL['resultat'], lw=0.8, zorder=2))
brace(ax, 2, xl, 70, 'sujet', label='13 groupes de 3', down=False)
text(ax, 77, 79, 'reste 1', 'resultat', 's')
arrow(ax, (80, 77), (xl + c / 2, 71), 'resultat')
text(ax, 44, 56, '40 = 13 × 3 + 1', 'sujet', 'm')
# suite du calcul
box(ax, 14, 38, 60, 9, 'sujet', label='1 = 40 − 13 × 3')
arrow(ax, (44, 37.5), (44, 34), 'varie')
box(ax, 14, 25, 60, 9, 'varie', label='−13 + 40 = 27')
arrow(ax, (44, 24.5), (44, 21), 'varie')
box(ax, 9, 12, 70, 9, 'resultat', label='3 × 27 = 81 = 2 × 40 + 1')
save(fig, '53-129')
