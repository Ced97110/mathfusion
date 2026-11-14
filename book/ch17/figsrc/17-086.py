import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
def seg(ax, x0, x1, y, role="sujet", lw=2.6):
    ax.plot([x0, x1], [y, y], color=COL[role], lw=lw, zorder=3, solid_capstyle="butt")
def chev(ax, x, y, left=True, role="encre"):
    d = 1.0 if left else -1.0
    line(ax, [(x + d * 0.9, y + 1.3), (x - d * 0.9, y), (x + d * 0.9, y - 1.3)], role, lw=1.0)

fig, ax = canvas(62)
f = None
for y, role, lab, note in [(44, 'autre', r'demi-droite : $x\geq -1$', 'sans fin à droite'), (14, 'sujet', r'segment : $-1\leq x<4$', 'limité des deux côtés')]:
    f = numberline(ax, 10, 66, y, -2, 6, labels=False, arrow_right=False)
    text(ax, 44, y + 11, lab, role, 'm'); text(ax, 44, y - 6, note, role, 's')
    text(ax, f(-1), y + 4.2, r'$-1$', role, 's')
    seg(ax, f(-1), f(4) if role == 'sujet' else 66, y, role)
    pt(ax, f(-1), y, True, role)
    if role == 'sujet':
        pt(ax, f(4), y, False, role); text(ax, f(4), y + 4.2, '4', role, 's')
    else: arrow(ax, (62, y), (72, y), role)
save(fig, '17-086')
