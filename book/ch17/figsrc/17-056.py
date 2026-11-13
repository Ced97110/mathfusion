import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, r, role, label=None, size='s'):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role], lw=0.8, zorder=4))
    if label is not None: text(ax, x, y, label, role, size)
fig, ax = canvas(100)
def row(y, pts, role):
    f = numberline(ax, 8, 68, y, 0, 16, step=16, labels=False, arrow_right=False)
    for v, s in pts: dot(ax, f(v), y, 2.3, role, label=s, size='s')
    return f
f = row(92, [(3, '3'), (7, '7')], 'sujet')
row(66, [(11, '11'), (15, '15')], 'resultat')
for a, b in [(3, 11), (7, 15)]: arrow(ax, (f(a), 89), (f(b), 69), 'varie')
text(ax, 22, 79, '+ 8', 'varie', 'm')
text(ax, 78, 66, '11 < 15', 'resultat', 's')
row(38, [(3, '3'), (7, '7')], 'sujet')
row(10, [(11, '11'), (9, '9')], 'limite')
for a, b in [(3, 11), (7, 9)]: arrow(ax, (f(a), 35), (f(b), 13), 'limite')
text(ax, 20, 25, '+ 8', 'limite', 'm')
text(ax, 54, 25, '+ 2', 'limite', 'm')
text(ax, 78, 10, '11 > 9', 'limite', 's')
save(fig, '17-056')
