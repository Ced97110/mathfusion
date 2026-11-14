import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(48)
y = 18
f = numberline(ax, 10, 66, y, 0, 8, labels=False)
tl(f, ax, y, [0, 2, 4, 5, 6, 8][:0] + [0, 1, 2, 3, 4, 6, 7, 8], 'fixe')
odot(ax, f(5), y, 'resultat', r=2.0); text(ax, f(5), y - 4, '$5$', 'resultat', 'm', weight='bold')
text(ax, 44, 42, '$3x-5=10$', 'sujet', 'l')
arrow(ax, (44, 38), (f(5), y + 5), 'varie'); text(ax, f(5) + 10, 30, '$x=5$', 'resultat', 'm')
text(ax, 77, y + 4, '$x$', 'sujet', 'm')
text(ax, 16, 30, 'une lettre : 1 axe', 'fixe', 's', ha='left')
save(fig, '17-100')
