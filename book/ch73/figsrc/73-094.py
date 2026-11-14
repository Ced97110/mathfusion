import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Wedge
fig, ax = canvas(62)
u = 22; O = (30, 32); a, b = 0.6, 0.8
T = (O[0] + a * u, O[1] + b * u)
ax.add_patch(Circle(O, u, ec=COL['fixe'], fc='none', lw=0.6, ls='--', zorder=1))
line(ax, [(O[0] - 24, O[1]), (O[0] + 24, O[1])], 'fixe', lw=0.5); line(ax, [(O[0], O[1] - 24), (O[0], O[1] + 24)], 'fixe', lw=0.5)
ax.add_patch(Wedge(O, 6, 0, math.degrees(math.atan2(b, a)), fc=FILL['varie'], ec=COL['varie'], lw=0.6, zorder=1))
line(ax, [T, (T[0], O[1])], 'resultat', dash=True); line(ax, [T, (O[0], T[1])], 'resultat', dash=True)
arrow(ax, O, T, 'sujet', lw=1.5)
disc(ax, *T, 0.9, 'sujet')
text(ax, T[0], O[1] - 4, r'$a=0{,}6$', 'resultat', 's')
text(ax, O[0] - 2, T[1], r'$b=0{,}8$', 'resultat', 's', ha='right')
text(ax, T[0] + 6, T[1] + 6, r'$Ae_1$', 'sujet')
text(ax, 57, O[1] + 6, r'$\theta\approx 53{,}13°$', 'varie', 's', ha='left')
text(ax, 44, 4, r'sur le cercle : $a^2+b^2=1$', 'resultat', 's')
save(fig, '73-094')
