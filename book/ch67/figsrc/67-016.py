import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
steps = [r'$\alpha\times\alpha$', r'$\alpha^2$', r'$\alpha+1$']
roles = ['sujet', 'varie', 'resultat']
notes = ['par définition du carré', r'règle 2']
for i in range(3):
    y = 66 - 22 * i
    box(ax, 4, y, 28, 12, roles[i], label=steps[i], size='m')
    if i < 2:
        arrow(ax, (18, y), (18, y - 10), 'varie')
        text(ax, 22, y - 5, notes[i], 'varie', 's', ha='left')
# small grid : position of the case (alpha, alpha)
gx, gy, c = 58, 36, 7
text(ax, 72, 77, 'table du bas', 'encre', 's')
text(ax, gx + 2.5 * c, gy + 4 * c + 4, r'$\alpha$', 'sujet', 's')
text(ax, gx - 3, gy + 1.5 * c, r'$\alpha$', 'sujet', 's')
for i in range(4):
    for j in range(4):
        hit = (i == 2 and j == 2)
        ax.add_patch(Rectangle((gx + c * j, gy + c * (3 - i)), c, c, ec=COL['fixe'], fc=FILL['resultat' if hit else 'fixe'], lw=0.6, zorder=2))
text(ax, gx + 2.5 * c, gy + 1.5 * c, r'$\alpha+1$', 'resultat', 's')
text(ax, 72, 24, 'la case est verte', 'resultat', 's')
save(fig, '67-016')
