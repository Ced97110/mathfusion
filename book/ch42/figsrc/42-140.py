import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
for cx, role, nom, n in [(22, 'sujet', r'$A$ : pairs', '4'), (66, 'autre', r'$B$ : impairs', '7')]:
    ax.add_patch(Circle((cx, 40), 15, ec=COL[role], fc=FILL[role], lw=1.0, zorder=2))
    text(ax, cx, 59, nom, role, 'm')
    text(ax, cx - 4, 40, n, role, 'l', weight='bold')
    text(ax, cx + 6, 40, r'$\cdots$', role, 'l')
text(ax, 44, 17, 'aucun élément commun', 'encre', 'm')
text(ax, 44, 8, r'$A \cap B = \varnothing$', 'resultat', 'l')
save(fig, '42-140')
