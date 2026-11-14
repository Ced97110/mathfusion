import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def venn(ax, cx, cy, r, d, fills, outs):
    a = Circle((cx - d, cy), r, fc=FILL[fills[0]], ec="none", zorder=2)
    b = Circle((cx + d, cy), r, fc=FILL[fills[1]], ec="none", zorder=2)
    ax.add_patch(a); ax.add_patch(b)
    l = Circle((cx + d, cy), r, fc=FILL[fills[2]], ec="none", zorder=2.1)
    ax.add_patch(l); l.set_clip_path(Circle((cx - d, cy), r, transform=ax.transData))
    ax.add_patch(Circle((cx - d, cy), r, fc="none", ec=COL[outs[0]], lw=1.0, zorder=3))
    ax.add_patch(Circle((cx + d, cy), r, fc="none", ec=COL[outs[1]], lw=1.0, zorder=3))

fig, ax = canvas(66)
cx, cy, r, d = 44, 36, 18, 10
venn(ax, cx, cy, r, d, ('resultat','resultat','limite'), ('sujet','autre'))
text(ax, cx - d, cy + r + 4, r'$A$', 'sujet', 'm')
text(ax, cx + d, cy + r + 4, r'$B$', 'autre', 'm')
text(ax, cx - d - 8.5, cy, '1', 'resultat', 'l')
text(ax, cx, cy, '2', 'limite', 'l')
text(ax, cx + d + 8.5, cy, '3', 'resultat', 'l')
text(ax, 24, 11, 'garde 1 et 3', 'resultat', 'm')
text(ax, 64, 11, 'écarte 2', 'limite', 'm')
save(fig, '80-205')
