import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, r=1.1, hollow=False):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc="white" if hollow else COL[role], lw=0.9, zorder=6))

fig, ax = canvas(54)
y = 24
f = numberline(ax, 8, 66, y, -5, 3, labels=True)
line(ax, [(f(-4), y), (f(2), y)], 'sujet', lw=2.4)
for v in range(-4, 2): dot(ax, f(v), y, 'resultat', 1.4)
dot(ax, f(2), y, 'sujet', 1.4, hollow=True)
text(ax, 44, 46, '−4 ≤ x < 2, x entier relatif', 'sujet', 'm')
brace(ax, f(-4), f(1), y + 6, 'resultat', '6 valeurs entières', down=False)
text(ax, f(2), 33, '2 exclu', 'sujet', 's')
save(fig, '12-091')
