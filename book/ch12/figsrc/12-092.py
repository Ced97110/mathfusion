import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, r=1.1, hollow=False):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc="white" if hollow else COL[role], lw=0.9, zorder=6))

fig, ax = canvas(64)
box(ax, 2, 28, 38, 30, 'sujet'); text(ax, 21, 53, 'naturels', 'sujet', 'm', weight='bold')
text(ax, 21, 43, '3 + 4 = 7', 'encre', 'm'); text(ax, 21, 34, '4 + 3 = 7', 'encre', 'm')
box(ax, 48, 28, 38, 30, 'autre'); text(ax, 67, 53, 'réels', 'autre', 'm', weight='bold')
text(ax, 67, 43, '3 + 4 = 7', 'encre', 'm'); text(ax, 67, 34, '4 + 3 = 7', 'encre', 'm')
arrow(ax, (21, 26), (36, 14), 'resultat'); arrow(ax, (67, 26), (52, 14), 'resultat')
box(ax, 14, 2, 60, 12, 'resultat', label='même propriété vraie', size='m')
text(ax, 44, 61, 'même constat dans les deux', 'fixe', 's') if False else None
save(fig, '12-092')
