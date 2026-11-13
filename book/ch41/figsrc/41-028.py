import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# 41-028 : composantes (2 nombres : 50 et 86,6) vs norme (1 nombre : 100) vs angle (direction seule)
fig, ax = canvas(88)
s = 0.3                      # 0,3 mm par unité, même échelle pour toutes les barres
x0 = 30
# ligne 1 : norme
y1 = 74
text(ax, 3, y1 + 4, 'norme', 'varie', 'm', ha='left', weight='bold')
text(ax, 3, y1 - 3, '1 nombre', 'fixe', 's', ha='left')
arrow(ax, (x0, y1), (x0 + 100 * s, y1), 'varie', lw=1.6)
text(ax, x0 + 50 * s * 1 + 0, y1 + 4.5, '100', 'varie', 'm')
# ligne 2 : angle
y2 = 46
text(ax, 3, y2 + 8, 'angle', 'fixe', 'm', ha='left', weight='bold')
text(ax, 3, y2 + 1, 'pas de longueur', 'fixe', 's', ha='left')
line(ax, [(x0, y2), (x0 + 30, y2)], 'fixe', lw=0.9)
arrow(ax, (x0, y2), (x0 + 30 * math.cos(math.radians(60)), y2 + 30 * math.sin(math.radians(60))), 'fixe', lw=0.9)
ax.add_patch(Arc((x0, y2), 18, 18, theta1=0, theta2=60, ec=COL['fixe'], lw=1.0, zorder=3))
text(ax, x0 + 15, y2 + 3.5, '60°', 'fixe', 'm')
# ligne 3 : composantes (mise en avant)
y3 = 17
box(ax, 1.5, y3 - 12, 85, 24, 'sujet', fill=False, dash=True, lw=0.8)
text(ax, 3.5, y3 + 5.5, 'composantes', 'sujet', 'm', ha='left', weight='bold')
text(ax, 3.5, y3 - 3, '2 nombres', 'fixe', 's', ha='left')
a, b = 50 * s, 86.6 * s
ax.add_patch(Rectangle((x0, y3 + 0.5), a, 3.4, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
ax.add_patch(Rectangle((x0 + a, y3 + 0.5), b, 3.4, ec=COL['resultat'], fc=FILL['resultat'], lw=0.8, zorder=2))
text(ax, x0 + a / 2, y3 - 3.5, '50', 'sujet', 'm')
text(ax, x0 + a + b / 2, y3 - 3.5, '86,6', 'resultat', 'm')
save(fig, '41-028')
