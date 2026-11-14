import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, r, role, label=None, size='s'):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role], lw=0.8, zorder=4))
    if label is not None: text(ax, x, y, label, role, size)
fig, ax = canvas(66)
y = 30
f = numberline(ax, 6, 78, y, -8, 8, step=4, labels=False, arrow_right=False)
text(ax, f(0), y - 4, '0', 'fixe', 's')
for v in (3, 7): dot(ax, f(v), y, 2.3, 'sujet', label=str(v), size='s')
for v in (-5, -1): dot(ax, f(v), y, 2.3, 'resultat', label=str(v).replace('-', '−'), size='s')
arrow(ax, (f(3) - 1, y + 3), (f(-5) + 1, y + 3), 'varie', curve=0.45)
arrow(ax, (f(7) - 1, y - 3), (f(-1) + 1, y - 3), 'varie', curve=-0.45)
text(ax, f(-1) + 4, y + 17, r'$+(-8)$', 'varie', 's')
text(ax, f(3) + 4, y - 17, r'$+(-8)$', 'varie', 's')
text(ax, f(5), 60, r'$3 < 7$', 'sujet', 'm')
text(ax, f(-3), 60, r'$-5 < -1$', 'resultat', 'm')
save(fig, '17-059')
