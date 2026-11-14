import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
s = 3.4; x0, y0 = 22, 20; w, h = 12 * s, 8 * s
ax.add_patch(Rectangle((x0, y0), w, h, fc=FILL['fixe'], ec=COL['sujet'], lw=2.6, zorder=2))
text(ax, x0 + w / 2, y0 + h + 3.5, '12 m', 'fixe', 's'); text(ax, x0 - 2, y0 + h / 2, '8 m', 'fixe', 's', ha='right')
text(ax, x0 + w / 2, y0 + h / 2, 'jardin', 'fixe', 's')
text(ax, 44, 62, r'$P$ = longueur du tour', 'sujet', 'm', weight='bold')
text(ax, 44, 12, r'$P = 2\times12 + 2\times8$', 'sujet', 'm')
text(ax, 44, 4.5, r'$P$ = 40 m', 'resultat', 'm', weight='bold')
save(fig, '11-080')
