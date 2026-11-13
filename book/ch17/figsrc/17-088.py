import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
def seg(ax, x0, x1, y, role="sujet", lw=2.6):
    ax.plot([x0, x1], [y, y], color=COL[role], lw=lw, zorder=3, solid_capstyle="butt")
def chev(ax, x, y, left=True, role="encre"):
    d = 1.0 if left else -1.0
    line(ax, [(x + d * 0.9, y + 1.3), (x - d * 0.9, y), (x + d * 0.9, y - 1.3)], role, lw=1.0)

fig, ax = canvas(80)
cols = [18, 44, 70]
rows = [(['1', r'$2x+3$', '9'], 66), (['$-2$', r'$2x$', '6'], 38), (['$-1$', r'$x$', '3'], 10)]
for parts, y in rows:
    for j, (p, x) in enumerate(zip(parts, cols)):
        role = 'sujet' if j == 1 else 'fixe'
        box(ax, x - 10, y - 5, 20, 10, role, label=p, size='m')
    for x in (31, 57): chev(ax, x, y, True)
for (ya, yb), lab in zip([(61, 43), (33, 15)], ['retirer 3 aux trois parties', 'diviser les trois par 2']):
    for x in cols: arrow(ax, (x, ya), (x, yb), 'varie')
    text(ax, 44, (ya + yb) / 2, lab, 'varie', 's').set_bbox(dict(fc='white', ec='none', pad=1.5))
save(fig, '17-088')
