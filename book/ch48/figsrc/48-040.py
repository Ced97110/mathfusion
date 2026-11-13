import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(80)
cx, cy, R = 44, 40, 26
ax.add_patch(Circle((cx, cy), R, ec=COL['sujet'], fc=FILL['sujet'], lw=1.3, zorder=2))
arrow(ax, (cx - 34, cy), (cx + 34, cy), 'fixe', lw=0.8); arrow(ax, (cx, cy - 32), (cx, cy + 34), 'fixe', lw=0.8)
line(ax, [(cx, cy), (cx + R, cy)], 'varie', lw=1.2)
text(ax, cx + R / 2, cy - 3.4, '1', 'varie', 's')
disc(ax, cx + R, cy, 1.6, 'resultat'); disc(ax, cx, cy + R, 1.6, 'resultat')
text(ax, cx + R + 4.5, cy + 3.5, '1', 'resultat', 'm')
text(ax, cx + 3.5, cy + R + 3, r'$i$', 'resultat', 'm')
text(ax, cx - 4, cy - 3.4, '0', 'fixe', 's')
text(ax, cx - 19, cy + 21, r'$\mathbb{T}$', 'sujet', 'xl')
text(ax, 44, 5, 'distance 1 de l’origine', 'sujet', 's')
save(fig, '48-040')
