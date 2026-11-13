import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, r=1.1, hollow=False):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc="white" if hollow else COL[role], lw=0.9, zorder=6))

fig, ax = canvas(62)
box(ax, 14, 46, 60, 12, 'limite', dash=True, label='aucune opération', size='m')
line(ax, [(14, 46), (74, 58)], 'limite', lw=1.2)
text(ax, 6, 31.5, '1', 'encre', 'l')
f = numberline(ax, 14, 70, 28, -6, 0, labels=False, arrow_right=False)
dot(ax, f(-5), 28, 'sujet', 1.3); dot(ax, f(-2), 28, 'autre', 1.3)
text(ax, f(-5), 21.5, '−5', 'sujet', 'm'); text(ax, f(-2), 21.5, '−2', 'autre', 'm')
text(ax, 44, 38, 'place les deux points', 'fixe', 's')
text(ax, 6, 8, '2', 'encre', 'l')
arrow(ax, (f(-2) - 1.5, 9), (f(-5) + 1.5, 9), 'varie')
text(ax, 44, 4, 'lequel est à gauche ?', 'varie', 's', ha='left') if False else None
text(ax, 50, 14, '−5 à gauche : le plus petit', 'resultat', 's')
save(fig, '12-088')
