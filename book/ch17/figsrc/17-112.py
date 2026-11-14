import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(80)
u = 32
def bar(x, y, w, role, lab=None):
    box(ax, x, y, w, 7, role, label=lab, size='s')
text(ax, 44, 76, '$x<x+6$', 'sujet', 'l')
text(ax, 5, 66, 'gauche', 'fixe', 's', ha='left'); bar(26, 62.5, u, 'sujet', '$x$')
text(ax, 5, 56, 'droite', 'fixe', 's', ha='left'); bar(26, 52.5, u, 'sujet', '$x$'); bar(26 + u, 52.5, 14, 'resultat', '$6$')
line(ax, [(26 + u, 72), (26 + u, 50)], 'varie', lw=0.6, dash=True)
arrow(ax, (44, 48), (44, 36), 'varie'); text(ax, 48, 42, 'retirer $x$', 'varie', 's', ha='left')
text(ax, 5, 30, 'gauche', 'fixe', 's', ha='left'); text(ax, 26, 30, '$0$', 'fixe', 'm', ha='left')
text(ax, 5, 18, 'droite', 'fixe', 's', ha='left'); bar(26, 14.5, 14, 'resultat', '$6$')
text(ax, 66, 22, '$0<6$ : vrai', 'resultat', 'm')
save(fig, '17-112')
