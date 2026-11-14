import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cell = 1.4
bx, by = 30, 14
line(ax, [(8, by), (80, by)], 'fixe', lw=0.8)
for i in range(30):
    ax.add_patch(Rectangle((bx, by + i * cell), cell, cell, ec=COL['varie'], fc=FILL['varie'], lw=0.4, zorder=2))
ax.add_patch(Rectangle((bx + cell, by), cell, cell, ec=COL['sujet'], fc=FILL['sujet'], lw=0.4, zorder=2))
text(ax, bx - 3, by + 15 * cell, 'montée\n30 cases\n1,75 mm', 'varie', 's', ha='right')
text(ax, bx + 6, by + 15 * cell, 'avance : 1 case\n0,06 mm', 'sujet', 's', ha='left')
line(ax, [(bx + 1.5 * cell + 0.3, by + 0.7), (bx + 5.5, by + 15 * cell - 4)], 'sujet', lw=0.5)
text(ax, 44, 70, r'valve à $t=0{,}1$ : $a=0{,}35$ m', 'encre', 'm')
text(ax, 44, 63.5, 'elle quitte le sol presque droit', 'varie', 's')
text(ax, 44, 7, 'le vélo : 35 mm, 600 fois plus', 'fixe', 's')
save(fig, '40-117')
