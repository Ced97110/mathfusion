import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(66)
y = 46
f = numberline(ax, 10, 70, y, -4, 4, labels=False, arrow_right=False)
seg(ax, f, -4, -0.4, y, 'autre'); seg(ax, f, 0.4, 4, y, 'sujet')
odot(ax, f(0), y, 'limite', False, r=1.9)
text(ax, 22, y + 8, 'règle 3 : $c<0$', 'autre', 's'); text(ax, 58, y + 8, 'règle 2 : $c>0$', 'sujet', 's')
text(ax, f(0), y - 6, '$c=0$', 'limite', 'm')
box(ax, 3, 6, 39, 12, 'limite', label='règle 3 : $0>0$ faux', size='s')
box(ax, 46, 6, 39, 12, 'limite', label='règle 2 : $0<0$ faux', size='s')
arrow(ax, (f(0) - 3, y - 10), (22, 20), 'limite'); arrow(ax, (f(0) + 3, y - 10), (66, 20), 'limite')
text(ax, 44, 30, 'avec 3 < 7', 'fixe', 's')
save(fig, '17-108')
