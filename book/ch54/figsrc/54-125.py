import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
w, u = 8, 5
def rect(x, y0, a, role):
    h = a * u
    ax.add_patch(Rectangle((x - w / 2, min(y0, y0 + h)), w, abs(h), ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
# ligne 1 : x - 1 (unitaire)
b1 = 66
text(ax, 22, 82, r'$x-1$ : dominant 1', 'sujet', 'm')
line(ax, [(6, b1), (40, b1)], 'fixe')
rect(14, b1, -1, 'sujet'); rect(28, b1, 1, 'sujet')
text(ax, 14, b1 - 8.5, r'$-1$', 'sujet', 's'); text(ax, 28, b1 + 8, '1', 'sujet', 's')
arrow(ax, (42, b1), (47, b1), 'varie')
text(ax, 50, b1 + 1.5, r'multiplier par $x$', 'varie', 's', ha='left')
text(ax, 50, b1 - 4.5, 'reste entier', 'resultat', 's', ha='left')
# ligne 2 : 2x - 1 (non unitaire)
b2 = 28
text(ax, 22, 46, r'$2x-1$ : dominant 2', 'autre', 'm')
line(ax, [(6, b2), (40, b2)], 'fixe')
rect(14, b2, -1, 'autre'); rect(28, b2, 2, 'autre')
text(ax, 14, b2 - 8.5, r'$-1$', 'autre', 's'); text(ax, 28, b2 + 13, '2', 'autre', 's')
arrow(ax, (42, b2), (47, b2), 'varie')
text(ax, 50, b2 + 1.5, r'multiplier par $\frac{1}{2}x$', 'varie', 's', ha='left')
text(ax, 50, b2 - 4.5, 'pas entier', 'limite', 's', ha='left')
save(fig, '54-125')
