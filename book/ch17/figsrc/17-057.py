import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, r, role, label=None, size='s'):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role], lw=0.8, zorder=4))
    if label is not None: text(ax, x, y, label, role, size)
fig, ax = canvas(82)
def row(y, pts, role):
    f = numberline(ax, 8, 68, y, 0, 16, step=16, labels=False, arrow_right=False)
    for v, s in pts: dot(ax, f(v), y, 2.3 if role == 'sujet' else 4.2, role, label=s, size='s')
    return f
f = row(70, [(3, r'$a$'), (7, r'$b$')], 'sujet')
row(14, [(11, r'$a+c$'), (15, r'$b+c$')], 'resultat')
for a, b in [(3, 11), (7, 15)]: arrow(ax, (f(a), 67), (f(b), 19), 'varie')
text(ax, 20, 40, 'déplacés de', 'varie', 's'); text(ax, 20, 35.5, 'la même longueur', 'varie', 's')
brace(ax, f(3), f(7), 74, 'sujet', 'écart', down=False)
brace(ax, f(11), f(15), 10, 'resultat', 'même écart', down=True)
text(ax, 78, 70, 'départ', 'sujet', 's'); text(ax, 80, 14, 'arrivée', 'resultat', 's')
save(fig, '17-057')
