import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Circle
fig, ax = canvas(84)
text(ax, 44, 79, r'signe de $x^2+y^2-1$', 'encre', 'm')
cx, cy, R = 44, 46, 24
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=1.4, ls='--', zorder=2))
disc(ax, cx, cy, 4, 'sujet', label='−1', size='s')
text(ax, cx + 6, cy - 6, r'$(0,0)$', 'sujet', 's', ha='left')
text(ax, 44, 12, 'cercle : aucun point calculé', 'fixe', 's')
text(ax, 44, 5, r'$0^2+0^2-1=-1$', 'sujet', 'm')
save(fig, '69-141')
