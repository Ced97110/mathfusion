import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def row(y, right, lab):
    f = numberline(ax, 8, 70, y, 0, 4, arrow_right=False, labels=(not right))
    if right: arrow(ax, (f(2) + 1.8, y), (80, y), 'varie', lw=2.4)
    else: arrow(ax, (f(2) - 1.8, y), (3, y), 'varie', lw=2.4)
    ax.add_patch(Circle((f(2), y), 1.8, ec=COL['fixe'], fc=FILL['encre'], lw=1.3, zorder=3))
    text(ax, 6, y + 9, lab, 'varie', 'l', ha='left')
    text(ax, 56 if right else 30, y + 5.5, 'à droite' if right else 'à gauche', 'varie', 's')
    return f
row(54, True, r'$x > 2$')
f = row(26, False, r'$x < 2$')
text(ax, f(2) + 20, 41, 'même point en 2', 'fixe', 's')
line(ax, [(f(2), 52 - 0.5 - 6), (f(2), 29.5 + 6)], 'fixe', dash=True)
text(ax, 44, 13, 'le point reste, la flèche change', 'varie', 's')
save(fig, '17-053')
