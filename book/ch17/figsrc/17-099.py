import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(58)
y = 34
f = numberline(ax, 12, 66, y, -3, 2, labels=False)
seg(ax, f, -2, 1, y, 'sujet'); odot(ax, f(-2), y, 'limite', False); odot(ax, f(1), y, 'resultat')
odot(ax, f(0), y, 'resultat', r=1.1)
text(ax, 44, 52, r'$-2<x\leq 1$', 'sujet', 'l')
text(ax, f(0), y + 8, '0 : vrai (milieu)', 'resultat', 's')
tl(f, ax, y, [-2, 1])
text(ax, f(-2), 14, '$-2$ : $7<7$ faux', 'limite', 's')
text(ax, f(1) - 1, 6, '$1$ : $-2\\leq -2$ vrai', 'resultat', 's')
arrow(ax, (f(-2), y - 9), (f(-2), 18), 'limite'); arrow(ax, (f(1), y - 9), (f(1), 10), 'resultat')
text(ax, f(-2) - 2.5, 21.5, 'exclu', 'limite', 's', ha='right'); text(ax, f(1) + 2.5, 21.5, 'inclus', 'resultat', 's', ha='left')
save(fig, '17-099')
