import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(56)
y = 28
arrow(ax, (44, y), (6, y), 'resultat', lw=2.4); arrow(ax, (44, y), (82, y), 'resultat', lw=2.4)
xs = [16, 40, 68]
for x, a, b in zip(xs, ['$x=-10$', '$x=0$', '$x=100$'], ['$-10<-4$', '$0<6$', '$100<106$']):
    odot(ax, x, y, 'resultat', r=1.5); text(ax, x, y + 6, a, 'fixe', 's'); text(ax, x, y - 6, b, 'resultat', 's')
text(ax, 44, 48, '$x<x+6$', 'sujet', 'l'); text(ax, 44, 10, 'vrai pour tous les nombres', 'resultat', 's')
save(fig, '17-111')
