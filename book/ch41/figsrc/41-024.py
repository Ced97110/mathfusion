import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# Le signe découpé : ‖ v ‖ = 100. Flèche du vent : 100 km/h à 60° (échelle 1 mm = 3 km/h).
fig, ax = canvas(72)
y = 62
text(ax, 14, y, r'$\|$', 'sujet', 'xl')
text(ax, 21, y, r'$v$', 'sujet', 'xl')
text(ax, 28, y, r'$\|$', 'sujet', 'xl')
text(ax, 44, y, '=', 'encre', 'xl')
text(ax, 58, y, '100', 'resultat', 'xl')
brace(ax, 11, 31, 55, 'sujet', label='longueur de $v$')
brace(ax, 52, 65, 55, 'resultat', label='en km/h')
# la flèche : seule sa longueur est écrite
O = (12, 6)
L = 100 / 3.0
E = (O[0] + L * math.cos(math.radians(60)), O[1] + L * math.sin(math.radians(60)))
line(ax, [O, (O[0] + 30, O[1])], 'fixe', lw=0.8, dash=True)
arrow(ax, O, E, 'sujet', lw=1.8)
ax.add_patch(Arc(O, 16, 16, theta1=0, theta2=60, color=COL['fixe'], lw=0.8, zorder=3))
text(ax, E[0] + 3, E[1] - 3, 'longueur 100', 'sujet', 's', ha='left')
text(ax, 62, 16, 'direction : pas écrite', 'fixe', 's')
save(fig, '41-024')
