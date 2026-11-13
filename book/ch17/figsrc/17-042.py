import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, full=True, r=1.7):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))

fig, ax = canvas(72)
cx = (36, 68)
text(ax, cx[0], 62, r'$-5<x$', 'sujet', 'm'); text(ax, cx[1], 62, r'$x>-5$', 'sujet', 'm')
for y, lab, ok in ((46, r'$x=0$', True), (30, r'$x=-7$', False), (14, r'$x=-5$', False)):
    text(ax, 12, y, lab, 'encre', 'm')
    for x in cx: box(ax, x - 14, y - 5, 28, 10, 'resultat' if ok else 'limite', label='vrai' if ok else 'faux')
text(ax, 52, 5, 'mêmes résultats', 'resultat', 's')
save(fig, '17-042')
