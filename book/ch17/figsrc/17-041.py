import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, full=True, r=1.7):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))

fig, ax = canvas(82)
text(ax, 44, 78, r'pour $x=0$', 'encre', 'm')
box(ax, 26, 58, 36, 12, 'sujet', label=r'$-5<x$ : vrai')
box(ax, 2, 20, 38, 12, 'limite', label=r'$x<-5$ : faux')
box(ax, 48, 20, 38, 12, 'resultat', label=r'$x>-5$ : vrai')
arrow(ax, (36, 57), (21, 34), 'varie'); arrow(ax, (52, 57), (67, 34), 'varie')
text(ax, 12, 47, 'échanger', 'varie', 's'); text(ax, 74, 47, 'échange + retourne', 'varie', 's')
save(fig, '17-041')
