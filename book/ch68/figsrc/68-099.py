import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'erreurs en moyenne par bloc', 'encre', 'm')
f = numberline(ax, 8, 80, 14, 0, 3, arrow_right=False, size='s')
for y, cap, v, role in [(42, '7 bits : 0,07 erreur', 0.07, 'sujet'), (26, '500 bits : 2,5 erreurs', 2.5, 'varie')]:
    text(ax, 8, y + 6, cap, role, 'm', ha='left')
    ax.add_patch(Rectangle((f(0), y - 2), f(v) - f(0), 5, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
text(ax, 44, 3, 'on découpe en blocs courts', 'resultat', 'm')
save(fig, '68-099')
