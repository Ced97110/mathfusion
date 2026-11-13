import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, r = 28, 28, 20
ax.add_patch(Circle((cx, cy), r, ec=COL['sujet'], fc=FILL['sujet'], lw=0.9, zorder=2))
text(ax, cx - 10, cy + 8, 'rayon 1', 'sujet', 'm')
line(ax, [(cx, cy + r), (62, cy + r)], 'fixe', dash=True)
line(ax, [(cx, cy), (cx, cy + r)], 'sujet', lw=1.2)
line(ax, [(62, cy), (62, cy + r)], 'resultat', lw=2.2)
line(ax, [(62, cy + r), (62, cy + 1.2071*r)], 'limite', lw=2.2)
text(ax, 65, cy + r/2, 'hauteur 1', 'resultat', 'm', ha='left')
text(ax, 62, cy + 1.2071*r + 5, '1,2071 : trop haut', 'limite', 'm')
save(fig, '34-003')
