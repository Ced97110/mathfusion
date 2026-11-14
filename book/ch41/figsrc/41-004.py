import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# Trois poignées, même force (50 N, longueur 22 mm), angles 0°, 30°, 90°.
fig, ax = canvas(58)
L = 22
cases = [(4, 0, '0° : tout avance'), (33, 30, '30° : une partie'), (64, 90, '90° : rien n’avance')]
y0 = 24
for x0, ang, cap in cases:
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    line(ax, [(x0, y0), (x0 + 23, y0)], 'fixe', lw=0.9)
    ex, ey = x0 + L * c, y0 + L * s
    if ang == 30:
        arrow(ax, (x0, y0 - 1.6), (ex, y0 - 1.6), 'resultat', lw=1.2)
        line(ax, [(ex, y0), (ex, ey)], 'varie', lw=1.2, dash=True)
        text(ax, ex + 1.5, y0 + 5.5, 'soulève', 'varie', 's', ha='left')
    arrow(ax, (x0, y0), (ex, ey), 'sujet', lw=1.3)
    if ang == 0:
        arrow(ax, (x0, y0 - 1.6), (ex, y0 - 1.6), 'resultat', lw=1.2)
    text(ax, x0 + 12, y0 - 7, cap, 'resultat' if ang < 90 else 'limite', 's')
    if ang:
        ax.add_patch(Arc((x0, y0), 12, 12, theta1=0, theta2=ang, color=COL['fixe'], lw=0.8, zorder=3))
text(ax, 16, y0 + 3.5, '50 N', 'sujet', 's')
text(ax, 36, y0 + 11, '50 N', 'sujet', 's')
text(ax, 64, y0 + 12, '50 N', 'sujet', 's', ha='left')
text(ax, 44, 52, 'valise tirée avec 50 N', 'encre', 'm')
save(fig, '41-004')
