import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, r=1.1, hollow=False):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc="white" if hollow else COL[role], lw=0.9, zorder=6))

fig, ax = canvas(56)
f = numberline(ax, 6, 70, 26, -6, 4, labels=False)
ax.add_patch(Rectangle((f(-5), 24.2), f(4) + 4 - f(-5), 3.6, fc=FILL['resultat'], ec='none', zorder=1))
dot(ax, f(-5), 26, 'sujet', 1.3); dot(ax, f(-2), 26, 'autre', 1.3)
text(ax, f(-5), 19, r'$a=-5$'.replace('-', '−'), 'sujet', 's')
text(ax, f(-2), 19, r'$b=-2$'.replace('-', '−'), 'autre', 's')
arrow(ax, (f(-5), 29), (f(-2), 29), 'resultat', curve=-0.4)
text(ax, f(-3.5), 37, 'à droite de $a$', 'resultat', 's')
text(ax, 44, 49, r'$b>a$', 'resultat', 'xl', weight='bold')
text(ax, 44, 8, 'plus à droite = plus grand', 'resultat', 's')
save(fig, '12-087')
