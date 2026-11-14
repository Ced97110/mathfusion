import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, r=1.1, hollow=False):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc="white" if hollow else COL[role], lw=0.9, zorder=6))

fig, ax = canvas(50)
box(ax, 2, 8, 42, 36, 'sujet'); text(ax, 23, 38, 'naturels', 'sujet', 'm', weight='bold')
disc(ax, 13, 22, 6, 'sujet', label='8', size='l'); disc(ax, 33, 22, 6, 'sujet', label='8', size='l')
arrow(ax, (46, 22), (62, 22), 'limite')
text(ax, 54, 29, '8 − 8', 'varie', 'm')
disc(ax, 74, 22, 7, 'limite', label='0', size='l')
text(ax, 74, 9, 'pas un naturel', 'limite', 's')
save(fig, '12-094')
