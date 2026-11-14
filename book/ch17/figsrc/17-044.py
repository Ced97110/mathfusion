import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, full=True, r=1.7):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))

fig, ax = canvas(60)
text(ax, 20, 52, r'$x+7>4$', 'sujet', 'm')
disc(ax, 14, 28, 5, 'resultat', label='0'); text(ax, 14, 16, 'une solution', 'resultat', 's')
box(ax, 34, 12, 52, 30, 'sujet', dash=True); text(ax, 60, 47, 'ensemble des solutions', 'sujet', 's')
for i, lab in enumerate(('0', '1', '2', '2,5', '10', r'$\ldots$')):
    disc(ax, 44 + (i % 3) * 16, 34 - (i // 3) * 12, 4.5, 'resultat', label=lab, size='s')
arrow(ax, (20, 28), (33, 28), 'varie')
save(fig, '17-044')
