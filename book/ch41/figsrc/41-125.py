import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(52)
k = 8.0                      # mm par unité
O = (34, 6)
phi = math.degrees(math.acos(12 / (math.sqrt(11) * 4)))   # 25,2°
n_tip = (O[0], O[1] + 4 * k)
lu = math.sqrt(11) * k
u_tip = (O[0] + lu * math.sin(math.radians(phi)), O[1] + lu * math.cos(math.radians(phi)))
foot = (O[0], u_tip[1])
arrow(ax, O, n_tip, 'autre', lw=1.4)
arrow(ax, O, u_tip, 'sujet', lw=1.4)
line(ax, [u_tip, foot], 'resultat', dash=True)
ax.add_patch(Arc(O, 24, 24, theta1=90 - phi, theta2=90, color=COL['varie'], lw=1.2, zorder=3))
text(ax, O[0] + 3.2, O[1] + 14.5, r'$\varphi$', 'varie', 'l')
line(ax, [(O[0] - 4, O[1]), (O[0] - 4, foot[1])], 'resultat', lw=1.2)
text(ax, O[0] - 11, (O[1] + foot[1]) / 2, r'$\approx 3$', 'resultat', 'm')
text(ax, O[0], n_tip[1] + 4.5, r'$v\times w$ (longueur 4)', 'autre', 's')
text(ax, u_tip[0] + 8, u_tip[1] + 2.5, r'$u$ (≈ 3,317)', 'sujet', 's')
box(ax, 58, 8, 28, 9, 'varie', label=r'$\varphi\approx 25{,}2°$', size='m')
save(fig, '41-125')
