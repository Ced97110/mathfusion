import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
def seg(ax, x0, x1, y, role="sujet", lw=2.6):
    ax.plot([x0, x1], [y, y], color=COL[role], lw=lw, zorder=3, solid_capstyle="butt")
def chev(ax, x, y, left=True, role="encre"):
    d = 1.0 if left else -1.0
    line(ax, [(x + d * 0.9, y + 1.3), (x - d * 0.9, y), (x + d * 0.9, y - 1.3)], role, lw=1.0)

fig, ax = canvas(80)
xs = (8, 74)
rows = [(62, 'sujet', r'$-1<x$ : à droite de $-1$'), (40, 'autre', r'$x<4$ : à gauche de 4'), (18, 'resultat', 'les deux à la fois')]
f = None
for i, (y, role, lab) in enumerate(rows):
    f = numberline(ax, xs[0], xs[1], y, -2, 6, labels=(i == 2), arrow_right=False)
    text(ax, 5, y + 7, lab, role, 's', ha='left')
    if i == 0:
        seg(ax, f(-1), xs[1], y, role); pt(ax, f(-1), y, False, role); arrow(ax, (xs[1] - 3, y), (xs[1] + 4, y), role)
    if i == 1:
        seg(ax, xs[0], f(4), y, role); pt(ax, f(4), y, False, role); arrow(ax, (xs[0] + 3, y), (xs[0] - 4, y), role)
    if i == 2:
        seg(ax, f(-1), f(4), y, role); pt(ax, f(-1), y, False, role); pt(ax, f(4), y, False, role)
line(ax, [(f(5), 10), (f(5), 70)], 'limite', lw=0.9, dash=True)
text(ax, f(5), 74, '5 : refusé', 'limite', 's')
save(fig, '17-083')
