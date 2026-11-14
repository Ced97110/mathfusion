import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, r, role, label=None, size='s'):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role], lw=0.8, zorder=4))
    if label is not None: text(ax, x, y, label, role, size)
fig, ax = canvas(90)
f = lambda v: 6 + (v + 60) / 70 * 72
def row(y, pts, role):
    line(ax, [(6, y), (78, y)], 'fixe')
    text(ax, f(0), y - 4.5, '0', 'fixe', 's')
    ax.plot([f(0)] * 2, [y - 1.2, y + 1.2], color=COL['fixe'], lw=0.8, zorder=3)
    for v, s in pts: dot(ax, f(v), y, 2.6 if len(s) > 2 else 1.7, role, label=s)
row(76, [(3, '3'), (7, '7')], 'sujet')
row(20, [(-24, '−24'), (-56, '−56')], 'resultat')
arrow(ax, (f(3), 73), (f(-24), 23.5), 'varie')
arrow(ax, (f(7), 73), (f(-56), 23.5), 'varie')
text(ax, 22, 62, r'$\times (-8)$', 'varie', 'm')
text(ax, 66, 85, r'$3 < 7$', 'sujet', 'm')
text(ax, 44, 6, r'$-24 > -56$ : le sens se renverse', 'resultat', 's')
save(fig, '17-063')
