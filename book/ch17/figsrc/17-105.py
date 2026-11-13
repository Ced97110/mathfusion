import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(64)
text(ax, 18, 58, '$4x\\geq 12$', 'sujet', 'l'); arrow(ax, (30, 58), (50, 58), 'varie'); text(ax, 40, 62, r'$\div 4$', 'varie', 's'); text(ax, 66, 58, r'$x\geq 3$', 'resultat', 'l')
y = 28
f = numberline(ax, 8, 70, y, 0, 10, labels=False); tl(f, ax, y, [0, 3, 10])
arrow(ax, (f(3), y), (f(10) + 5, y), 'resultat', lw=2.6); odot(ax, f(3), y, 'resultat')
odot(ax, f(10), y, 'autre', r=1.4)
text(ax, f(3), y + 6, 'bord inclus', 'resultat', 's')
text(ax, f(10), y + 6, 'test : 40', 'autre', 's')
text(ax, 44, 8, '3 est le départ, côté droit', 'resultat', 's')
save(fig, '17-105')
