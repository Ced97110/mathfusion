import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def dot(x, y, role, full=True, r=1.6):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL["encre"], lw=0.9, zorder=4))
f = numberline(ax, 10, 70, 30, -4, 4)
for v, role in ((1, 'sujet'), (3, 'autre'), (-1, 'sujet'), (-3, 'autre')):
    dot(f(v), 30, role, r=2)
arrow(ax, (f(3), 34), (f(-3), 34), 'varie', curve=0.5)
arrow(ax, (f(1), 34), (f(-1), 34), 'varie', curve=0.5)
text(ax, f(0), 54, r'$\times (-1)$', 'varie', 'l', weight='bold')
text(ax, f(2), 14, r'$1 < 3$', 'encre', 'm')
text(ax, f(-2), 14, r'$-1 > -3$', 'resultat', 'm')
save(fig, '17-023')
