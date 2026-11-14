import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, full=True, r=1.7):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))

fig, ax = canvas(72); y = 36
f = numberline(ax, 8, 70, y, 2, 8, labels=False, arrow_right=False)
disc(ax, f(3), y, 3.0, 'sujet', label=r'$3$', size='m'); disc(ax, f(7), y, 3.0, 'autre', label=r'$7$', size='m')
arrow(ax, (f(3), y + 3.2), (f(7), y + 3.2), 'sujet', curve=-0.5)
arrow(ax, (f(7), y - 3.2), (f(3), y - 3.2), 'autre', curve=-0.5)
text(ax, f(5), y + 20, r'$3<7$', 'sujet', 'l'); text(ax, f(5), y + 27, 'vu depuis 3', 'sujet', 's')
text(ax, f(5), y - 20, r'$7>3$', 'autre', 'l'); text(ax, f(5), y - 27, 'vu depuis 7', 'autre', 's')
save(fig, '17-040')
