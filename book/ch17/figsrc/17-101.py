import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(52)
y = 24
f = numberline(ax, 10, 68, y, 0, 6, labels=True, size='s')
text(ax, 80, y + 4, '$x$', 'sujet', 'l')
text(ax, 44, 46, 'axe = droite graduée', 'sujet', 'l')
odot(ax, f(4), y, 'varie', r=1.9)
text(ax, f(4), y + 9, 'une valeur de $x$', 'varie', 's'); arrow(ax, (f(4), y + 6.5), (f(4), y + 2.6), 'varie')
text(ax, f(2), y + 12, 'graduations', 'fixe', 's'); arrow(ax, (f(2) - 3, y + 9.5), (f(1), y + 1.8), 'fixe'); arrow(ax, (f(2) + 3, y + 9.5), (f(3), y + 1.8), 'fixe')
text(ax, f(5.5), 8, 'la droite', 'sujet', 's'); arrow(ax, (f(5.5), 11.5), (f(5.5), y - 1), 'sujet')
save(fig, '17-101')
