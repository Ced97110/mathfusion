import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(80)
y0, y1, y2 = 62, 28, 12
f = numberline(ax, 12, 64, y0, 0, 8, labels=False); g = numberline(ax, 12, 64, y1, 0, 8, labels=False); h = numberline(ax, 12, 64, y2, 0, 8, labels=False)
text(ax, 44, 76, '1 lettre $d$ : 1 axe', 'sujet', 'm')
odot(ax, f(4), y0, 'sujet', r=1.9); text(ax, f(4), y0 - 5, '$d=4$', 'sujet', 's'); text(ax, 77, y0 + 4, '$d$', 'sujet', 'm')
text(ax, 44, 44, '2 lettres : 2 axes', 'autre', 'm')
odot(ax, g(3), y1, 'autre', r=1.9); text(ax, g(3), y1 - 5, '$x=3$', 'autre', 's'); text(ax, 77, y1 + 4, '$x$', 'autre', 'm')
odot(ax, h(1), y2, 'autre', r=1.9); text(ax, h(1), y2 - 5, '$y=1$', 'autre', 's'); text(ax, 77, y2 + 4, '$y$', 'autre', 'm')
save(fig, '17-102')
