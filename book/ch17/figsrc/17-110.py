import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(72)
y = 58
f = numberline(ax, 10, 66, y, 0, 8, labels=False)
arrow(ax, (f(5), y), (f(8) + 5, y), 'sujet', lw=2.4); odot(ax, f(5), y, 'sujet', False)
odot(ax, f(6), y, 'resultat', r=1.4)
text(ax, 18, y + 8, '$x>5$', 'sujet', 'm'); text(ax, f(5), y - 5, '$5$', 'sujet', 's'); text(ax, f(6) + 2, y - 5, '6 convient', 'resultat', 's', ha='left')
arrow(ax, (44, 46), (44, 33), 'varie'); text(ax, 48, 39.5, r'$\times 0$ des deux côtés', 'varie', 's', ha='left')
box(ax, 14, 18, 60, 11, 'limite', label='$0>0$ : faux', size='m')
text(ax, 44, 8, 'la solution 6 disparaît', 'limite', 's')
save(fig, '17-110')
