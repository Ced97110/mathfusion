import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
def seg(ax, x0, x1, y, role="sujet", lw=2.6):
    ax.plot([x0, x1], [y, y], color=COL[role], lw=lw, zorder=3, solid_capstyle="butt")
def chev(ax, x, y, left=True, role="encre"):
    d = 1.0 if left else -1.0
    line(ax, [(x + d * 0.9, y + 1.3), (x - d * 0.9, y), (x + d * 0.9, y - 1.3)], role, lw=1.0)

fig, ax = canvas(66)
text(ax, 44, 61, '« $x$ est entre 2 et 5 »', 'encre', 'l')
for y, full, ex, note in [(40, False, r'$2<x<5$', '2 et 5 refusés'), (12, True, r'$2\leq x\leq 5$', '2 et 5 acceptés')]:
    f = numberline(ax, 10, 66, y, 0, 7, labels=False, arrow_right=True)
    seg(ax, f(2), f(5), y, 'sujet')
    pt(ax, f(2), y, full, 'sujet'); pt(ax, f(5), y, full, 'sujet')
    text(ax, f(2), y - 4, '2', 'sujet', 's'); text(ax, f(5), y - 4, '5', 'sujet', 's')
    text(ax, 20, y + 9, ex, 'sujet', 'm'); text(ax, 62, y + 9, note, 'sujet', 's')
save(fig, '17-084')
