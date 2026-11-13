import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
def seg(ax, x0, x1, y, role="sujet", lw=2.6):
    ax.plot([x0, x1], [y, y], color=COL[role], lw=lw, zorder=3, solid_capstyle="butt")
def chev(ax, x, y, left=True, role="encre"):
    d = 1.0 if left else -1.0
    line(ax, [(x + d * 0.9, y + 1.3), (x - d * 0.9, y), (x + d * 0.9, y - 1.3)], role, lw=1.0)

fig, ax = canvas(72)
rows = [(52, 'autre', 'simple', [r'$d\leq 6$'], '1 symbole'),
        (30, 'autre', 'paire', [r'$d\geq 0$', r'$d\leq 6$'], '2 lignes'),
        (8, 'sujet', 'double', [r'$0\leq d\leq 6$'], '2 symboles, 1 ligne')]
for y, role, lab, ex, note in rows:
    box(ax, 3, y, 82, 18, role, label=None)
    text(ax, 7, y + 9, lab, role, 'm', ha='left', weight='bold')
    if len(ex) == 1: text(ax, 40, y + 9, ex[0], role, 'l')
    else:
        text(ax, 40, y + 13, ex[0], role, 'l'); text(ax, 40, y + 5, ex[1], role, 'l')
    text(ax, 69, y + 9, note, role, 's')
save(fig, '17-081')
