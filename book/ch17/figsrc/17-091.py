import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
def seg(ax, x0, x1, y, role="sujet", lw=2.6):
    ax.plot([x0, x1], [y, y], color=COL[role], lw=lw, zorder=3, solid_capstyle="butt")
def chev(ax, x, y, left=True, role="encre"):
    d = 1.0 if left else -1.0
    line(ax, [(x + d * 0.9, y + 1.3), (x - d * 0.9, y), (x + d * 0.9, y - 1.3)], role, lw=1.0)

fig, ax = canvas(52)
y = 24
f = numberline(ax, 8, 66, y, -3, 2, arrow_right=True)
b = -9 / 8
seg(ax, f(b), 70, y, 'sujet'); arrow(ax, (66, y), (75, y), 'sujet', lw=1.4)
pt(ax, f(b), y, False, 'sujet'); pt(ax, f(-1), y, True, 'resultat', 1.1); pt(ax, f(-2), y, True, 'limite', 1.1)
text(ax, f(b) + 1, y + 11, r'$-\frac{9}{8}=-1{,}125$', 'sujet', 's', ha='right')
line(ax, [(f(b), y + 2), (f(b), y + 8)], 'sujet', lw=0.6)
text(ax, f(-1) + 1, y + 11, r'$-1$ : solution', 'resultat', 's', ha='left')
line(ax, [(f(-1), y + 2), (f(-1), y + 8)], 'resultat', lw=0.6)
text(ax, f(-2), y - 10, r'$-2$ : pas solution', 'limite', 's')
text(ax, 62, 45, r'$x>-\frac{9}{8}$', 'sujet', 'm')
save(fig, '17-091')
