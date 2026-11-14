import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# Échelle 1 mm = 1 N. Force 50 N à 30° : 43,30 N le long du sol, 25 N vers le haut (43,30² + 25² = 2 500).
fig, ax = canvas(66)
O = (8, 12)
c, s = 50 * math.cos(math.radians(30)), 50 * math.sin(math.radians(30))   # 43,30 ; 25,00
line(ax, [O, (80, 12)], 'fixe', lw=0.8)
arrow(ax, (O[0], O[1] - 1.8), (O[0] + c, O[1] - 1.8), 'resultat', lw=1.3)
line(ax, [(O[0] + c, O[1]), (O[0] + c, O[1] + s)], 'varie', lw=1.3, dash=True)
arrow(ax, O, (O[0] + c, O[1] + s), 'sujet', lw=1.4)
ax.add_patch(Arc(O, 16, 16, theta1=0, theta2=30, color=COL['fixe'], lw=0.8, zorder=3))
text(ax, 19, 15.2, '30°', 'fixe', 's')
text(ax, 22, 29, '50 N', 'sujet', 's')
text(ax, O[0] + c / 2, 4.5, '43,30 N : fait avancer', 'resultat', 's')
text(ax, O[0] + c + 2, 12 + s / 2, '25 N : soulève', 'varie', 's', ha='left')
text(ax, 44, 58, '43,30² + 25² ≈ 50²', 'resultat', 'm')
text(ax, 44, 51, '43,30 + 25 ≠ 50', 'encre', 'm')
save(fig, '41-006')
