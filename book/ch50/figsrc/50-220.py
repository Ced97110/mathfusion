import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for cx, role in [(31, 'sujet'), (57, 'autre')]:
    ax.add_patch(Circle((cx, 38), 17, ec=COL[role], fc=FILL[role], alpha=0.6, lw=0.9, zorder=1))
text(ax, 22, 59, 'diviseurs de 47', 'sujet', 's')
text(ax, 65, 59, 'diviseurs de 5', 'autre', 's')
text(ax, 23, 38, '47', 'sujet', 'l')
text(ax, 65, 38, '5', 'autre', 'l')
text(ax, 44, 38, '1', 'resultat', 'l', weight='bold')
text(ax, 44, 17, 'seul diviseur commun', 'resultat', 's')
arrow(ax, (44, 19), (44, 34.5), 'resultat')
box(ax, 14, 3, 60, 9, 'resultat', label=r"$|G'|=1$ donc $G'=\{e\}$", size='m')
save(fig, '50-220')
