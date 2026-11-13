import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def dot(x, y, role, full=True, r=1.6):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL["encre"], lw=0.9, zorder=4))
f = numberline(ax, 8, 70, 20, 0, 6)
dot(f(5), 20, 'sujet', r=2); dot(f(1), 20, 'autre', r=2)
arrow(ax, (f(1), 24), (f(5), 24), 'limite', curve=-0.4)
text(ax, f(3), 35, '5 est à droite de 1', 'limite', 'm')
text(ax, f(3), 44, r'$5 < 1$ : faux', 'limite', 'l', weight='bold')
save(fig, '17-021')
