import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
def seg(ax, x0, x1, y, role="sujet", lw=2.6):
    ax.plot([x0, x1], [y, y], color=COL[role], lw=lw, zorder=3, solid_capstyle="butt")
def chev(ax, x, y, left=True, role="encre"):
    d = 1.0 if left else -1.0
    line(ax, [(x + d * 0.9, y + 1.3), (x - d * 0.9, y), (x + d * 0.9, y - 1.3)], role, lw=1.0)

fig, ax = canvas(78)
cols = [14, 30, 44, 58, 74]
def row(y, items, role, symrole):
    for i, (t, x) in enumerate(zip(items, cols)):
        text(ax, x, y, t, symrole if i % 2 else role, 'l')
row(66, ['6', r'$<$', r'$-2x$', r'$\leq$', '10'], 'sujet', 'sujet')
arrow(ax, (44, 60), (44, 44), 'varie'); text(ax, 62, 52, r'$\div(-2)$', 'varie', 'm')
row(36, [r'$-3$', r'$>$', r'$x$', r'$\geq$', r'$-5$'], 'resultat', 'varie')
text(ax, 44, 28, 'les deux symboles retournés', 'varie', 's')
text(ax, 20, 14, 'sans retourner :', 'limite', 's')
text(ax, 62, 14, r'$-3<x\leq -5$ : impossible', 'limite', 's')
save(fig, '17-089')
