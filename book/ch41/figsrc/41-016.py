import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# Deux vecteurs : vent 100 km/h à 60° ; force 50 N à 30°. Échelle 1 mm = 3 (de l'unité).
fig, ax = canvas(70)
text(ax, 44, 66, 'vecteur : une flèche', 'sujet', 'l')
def vec(O, val, ang, unit, name):
    L = val / 3
    E = (O[0] + L * math.cos(math.radians(ang)), O[1] + L * math.sin(math.radians(ang)))
    line(ax, [O, (O[0] + 30, O[1])], 'fixe', lw=0.8, dash=True)
    arrow(ax, O, E, 'sujet', lw=1.6)
    ax.add_patch(Arc(O, 16, 16, theta1=0, theta2=ang, color=COL['varie'], lw=0.9, zorder=3))
    return E
E1 = vec((6, 20), 100, 60, 'km/h', 'vent')
E2 = vec((50, 20), 50, 30, 'N', 'force')
text(ax, 6 + 12, 25, '60°', 'varie', 's', ha='left')
text(ax, 50 + 10, 22.5, '30°', 'varie', 's', ha='left')
text(ax, E1[0] + 2, E1[1] + 1, 'vent 100 km/h', 'sujet', 's', ha='left')
text(ax, 66, 34, 'force 50 N', 'sujet', 's')
text(ax, 30, 56, 'longueur = valeur', 'sujet', 's')
text(ax, 62, 56, 'inclinaison = direction', 'varie', 's')
box(ax, 6, 3, 76, 9, 'fixe', label='scalaire : 5 kg, 20 degrés', size='s')
save(fig, '41-016')
