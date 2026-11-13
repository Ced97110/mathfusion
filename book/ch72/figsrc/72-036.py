import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
def ax2(cx, cy, r):
    arrow(ax, (cx - r, cy), (cx + r, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy - r), (cx, cy + r), 'fixe', lw=0.6)
cy = 36
line(ax, [(44, 6), (44, 62)], 'fixe', lw=0.6, dash=True)
box(ax, 4, 54, 38, 9, 'sujet', label='plan habituel', size='s')
box(ax, 46, 54, 38, 9, 'autre', label='seconde mesure', size='s')
ax2(23, cy, 17); ax2(65, cy, 17)
disc(ax, 23, cy, 1.8, 'resultat')
text(ax, 23, 14, 'carré 0 : seul (0, 0)', 'resultat', 's')
text(ax, 23, 7, 'aucun vecteur isotrope', 'resultat', 's')
line(ax, [(51, cy - 14), (79, cy + 14)], 'limite', lw=1.6)
line(ax, [(51, cy + 14), (79, cy - 14)], 'limite', lw=1.6)
disc(ax, 72, cy + 7, 1.5, 'limite')
text(ax, 77, cy + 2.5, '(1, 1)', 'limite', 's', ha='center')
text(ax, 65, 14, 'carré 0 : deux droites', 'limite', 's')
text(ax, 65, 7, 'des vecteurs isotropes', 'limite', 's')
save(fig, '72-036')
