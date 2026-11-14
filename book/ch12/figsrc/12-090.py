import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, r=1.1, hollow=False):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc="white" if hollow else COL[role], lw=0.9, zorder=6))

fig, ax = canvas(56)
y = 20
f = numberline(ax, 8, 66, y, -5, 3, labels=True)
line(ax, [(f(-4), y), (f(2), y)], 'sujet', lw=3.2)
dot(ax, f(-4), y, 'sujet', 1.5); dot(ax, f(2), y, 'sujet', 1.5, hollow=True)
text(ax, 44, 48, r'$-4\leq x<2$'.replace('-', '−') if False else '−4 ≤ x < 2', 'sujet', 'xl', weight='bold')
text(ax, f(-4), 33, '−4 inclus', 'sujet', 's')
text(ax, f(2), 33, '2 exclu', 'sujet', 's')
arrow(ax, (f(-4), 31), (f(-4), y + 3), 'fixe'); arrow(ax, (f(2), 31), (f(2), y + 3), 'fixe')
text(ax, 38, 8, 'la zone de tous les x', 'sujet', 's')
save(fig, '12-090')
