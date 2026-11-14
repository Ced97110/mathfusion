import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

s = 20.0
ox, oy = 8, 16
fig, ax = canvas(80)
r3 = math.sqrt(3)
zw = (ox + (r3 - 1) * s, oy + (r3 + 1) * s)
arrow(ax, (ox - 2, oy), (ox + 34, oy), 'fixe', lw=0.6)
arrow(ax, (ox, oy - 2), (ox, oy + 62), 'fixe', lw=0.6)
line(ax, [(ox, oy), zw], 'resultat', lw=1.1)
line(ax, [zw, (zw[0], oy)], 'fixe', lw=0.8, dash=True)
line(ax, [(ox, oy), (zw[0], oy)], 'sujet', lw=2.2)
disc(ax, zw[0], zw[1], 1.4, 'resultat')
ax.add_patch(Arc((ox, oy), 56, 56, theta1=0, theta2=75, ec=COL['resultat'], lw=1.0, zorder=3))
text(ax, ox + 10.5, oy + 16, '75°', 'resultat', 's')
text(ax, ox + 3, oy + 33, r'$2\sqrt{2}$', 'resultat', 's', ha='left', rot=75)
brace(ax, ox, zw[0], oy - 2.5, 'sujet', label='partie réelle', down=True, size='s')
box(ax, 42, 56, 44, 11, 'sujet', label=r'$2\sqrt{2}\,\cos 75°=\sqrt{3}-1$', size='s')
arrow(ax, (64, 56), (64, 46), 'varie', lw=1.0)
text(ax, 77, 51, r'$\div\,2\sqrt{2}$', 'varie', 's')
box(ax, 42, 34, 44, 11, 'fixe', label=r'$\cos 75°=\frac{\sqrt{3}-1}{2\sqrt{2}}$', size='s')
arrow(ax, (64, 34), (64, 24), 'varie', lw=1.0)
text(ax, 77, 29, r'$\times\,\sqrt{2}$ haut, bas', 'varie', 's')
box(ax, 42, 12, 44, 11, 'resultat', label=r'$\cos 75°=\frac{\sqrt{6}-\sqrt{2}}{4}$', size='s')
text(ax, 64, 7, r'$\approx 0{,}2588$ (contrôle)', 'resultat', 's')
save(fig, '39-112')
