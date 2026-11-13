import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
def seg(ax, x0, x1, y, role="sujet", lw=2.6):
    ax.plot([x0, x1], [y, y], color=COL[role], lw=lw, zorder=3, solid_capstyle="butt")
def chev(ax, x, y, left=True, role="encre"):
    d = 1.0 if left else -1.0
    line(ax, [(x + d * 0.9, y + 1.3), (x - d * 0.9, y), (x + d * 0.9, y - 1.3)], role, lw=1.0)

fig, ax = canvas(70)
text(ax, 20, 66, r'$-1$ et 4 : chaque bord seul', 'fixe', 's', ha='left')
combos = [(r'$-1\leq x<4$', True, False), (r'$-1<x\leq 4$', False, True), (r'$-1\leq x\leq 4$', True, True), (r'$-1<x<4$', False, False)]
for i, (lab, a, b) in enumerate(combos):
    y = 52 - i * 14
    text(ax, 3, y, lab, 'sujet', 's', ha='left')
    f = numberline(ax, 36, 72, y, -2, 5, labels=False, arrow_right=False)
    seg(ax, f(-1), f(4), y, 'sujet'); pt(ax, f(-1), y, a, 'sujet'); pt(ax, f(4), y, b, 'sujet')
text(ax, 36 + 34 / 7, 60, '', 'fixe', 's')
save(fig, '17-087')
