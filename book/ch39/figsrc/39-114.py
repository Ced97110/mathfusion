import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

cx, cy = 34, 46
fig, ax = canvas(92)
A = math.degrees(math.pi - math.atan(math.sqrt(7) / 3))  # ≈ 138,59°
R = 6 * A - 720  # ≈ 111,54°
arrow(ax, (cx - 30, cy), (cx + 32, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - 34), (cx, cy + 36), 'fixe', lw=0.6)
L = 26
ex, ey = cx + L * math.cos(math.radians(A)), cy + L * math.sin(math.radians(A))
line(ax, [(cx, cy), (ex, ey)], 'sujet', lw=1.5)
disc(ax, ex, ey, 1.4, 'sujet')
fx, fy = cx + L * math.cos(math.radians(R)), cy + L * math.sin(math.radians(R))
line(ax, [(cx, cy), (fx, fy)], 'resultat', lw=1.5, dash=True)
disc(ax, fx, fy, 1.4, 'resultat')
ax.add_patch(Arc((cx, cy), 12, 12, theta1=0, theta2=A, ec=COL['sujet'], lw=1.1, zorder=3))
ax.add_patch(Arc((cx, cy), 20, 20, theta1=0, theta2=360, ec=COL['varie'], lw=1.0, zorder=3))
ax.add_patch(Arc((cx, cy), 28, 28, theta1=0, theta2=360, ec=COL['varie'], lw=1.0, zorder=3))
ax.add_patch(Arc((cx, cy), 36, 36, theta1=0, theta2=6 * A - 720, ec=COL['resultat'], lw=1.1, zorder=3))
text(ax, ex - 2, ey + 4, r'$-3+\sqrt{7}\,i$', 'sujet', 's', ha='right')
text(ax, cx + 8.5, cy + 3.5, '138,59°', 'sujet', 's', ha='left')
text(ax, fx + 2.5, fy + 2.5, '111,54°', 'resultat', 's', ha='left')
text(ax, 86, 24, r'$6\times 138{,}59°\approx 831{,}54°$', 'varie', 's', ha='right')
text(ax, 86, 17.5, '− 2 tours (720°) = 111,54°', 'varie', 's', ha='right')
text(ax, 86, 10, r'module : $4^6=4\,096$', 'sujet', 's', ha='right')
text(ax, 44, 3, r'$\approx -1\,504{,}0+3\,809{,}9\,i$', 'resultat', 'm')
text(ax, 4, 87, r'$(-3+\sqrt{7}\,i)^6$', 'encre', 'l', ha='left')
save(fig, '39-114')
