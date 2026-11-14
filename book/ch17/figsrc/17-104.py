import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(84)
xc = 26
text(ax, xc, 78, '$3x-5=10$', 'sujet', 'l')
arrow(ax, (xc, 74), (xc, 61), 'varie'); text(ax, xc + 6, 67.5, '$+5$ des deux côtés', 'varie', 's', ha='left')
text(ax, xc, 57, '$3x=15$', 'sujet', 'l')
arrow(ax, (xc, 53), (xc, 40), 'varie'); text(ax, xc + 6, 46.5, r'$\div 3$ des deux côtés', 'varie', 's', ha='left')
text(ax, xc, 36, '$x=5$', 'resultat', 'l', weight='bold')
text(ax, 66, 36, '$3\\times5-5=10$', 'resultat', 's')
y = 16
f = numberline(ax, 10, 66, y, 0, 8, labels=False); tl(f, ax, y, [0, 2, 4, 6, 8])
odot(ax, f(5), y, 'resultat', r=2.0); text(ax, f(5), y + 6, '$x=5$', 'resultat', 's')
arrow(ax, (xc, 32), (f(5) - 2, y + 9), 'resultat')
save(fig, '17-104')
