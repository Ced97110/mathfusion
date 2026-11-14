import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def dot(ax, p, role, r=1.5): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))

fig, ax = canvas(78)
box(ax, 4, 22, 80, 52, 'sujet')
text(ax, 44, 68, 'ensemble de gauche', 'sujet', 's')
box(ax, 9, 26, 42, 32, 'autre')
text(ax, 30, 53, 'ensemble de droite', 'autre', 's')
for x, n in zip((17, 30, 43), (2, 4, 6)):
    text(ax, x, 38, str(n), 'autre', 'l')
for x, n in zip((58, 68, 78), (1, 3, 5)):
    text(ax, x, 38, str(n), 'sujet', 'l')
text(ax, 44, 11, r'$\{1,2,3,4,5,6\}\supset\{2,4,6\}$', 'encre', 'm')
save(fig, '73-208')
