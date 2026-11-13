import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
def seg(ax, x0, x1, y, role="sujet", lw=2.6):
    ax.plot([x0, x1], [y, y], color=COL[role], lw=lw, zorder=3, solid_capstyle="butt")
def chev(ax, x, y, left=True, role="encre"):
    d = 1.0 if left else -1.0
    line(ax, [(x + d * 0.9, y + 1.3), (x - d * 0.9, y), (x + d * 0.9, y - 1.3)], role, lw=1.0)

fig, ax = canvas(66)
box(ax, 24, 50, 40, 12, 'encre', label=r'$-8x+5<14$', size='m')
box(ax, 3, 6, 38, 24, 'sujet')
text(ax, 22, 24, r'$\div(-8)$', 'sujet', 'm'); text(ax, 22, 12, 'symbole retourné', 'sujet', 's')
box(ax, 47, 6, 38, 24, 'autre')
text(ax, 66, 24, r'$+8x$ puis $\div 8$', 'autre', 'm'); text(ax, 66, 12, 'rien à retourner', 'autre', 's')
arrow(ax, (34, 50), (22, 31), 'sujet'); arrow(ax, (54, 50), (66, 31), 'autre')
text(ax, 44, 39, 'ou', 'fixe', 's')
save(fig, '17-094')
