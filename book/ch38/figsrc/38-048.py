import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

def arc(x, y, r, a, b, role, lw=1.0):
    ax.add_patch(Arc((x, y), 2 * r, 2 * r, theta1=a, theta2=b, color=COL[role], lw=lw, zorder=3))

fig, ax = canvas(64)
g = 14.0
line(ax, [(44, 6), (44, 58)], 'fixe', dash=True, lw=0.6)
# Gauche : la rivière, vue de dessus, angles horizontaux (échelle 0,25 mm par mètre)
k = 0.25
al, be = 51.33, 69.20
ta, tb = math.tan(math.radians(al)), math.tan(math.radians(be))
w = 150 * ta * tb / (ta + tb)
A = (3.0, g); B = (A[0] + 150 * k, g); P = (A[0] + w / ta * k, g + w * k)
poly(ax, [A, B, P], 'sujet')
arc(A[0], A[1], 5, 0, al, 'sujet'); arc(B[0], B[1], 5, 180 - be, 180, 'sujet')
text(ax, A[0] + 9, g + 2.6, 'α', 'sujet', 's', weight='bold')
text(ax, B[0] - 8, g + 3.4, 'β', 'sujet', 's', weight='bold')
text(ax, 22, 58, 'Rivière', 'sujet', 'm', weight='bold')
text(ax, 22, 54, 'vue de dessus', 'sujet', 's')
text(ax, 22, 6, 'cercle horizontal', 'sujet', 's')
# Droite : la montagne, vue de côté, angles d'élévation (hauteur 12 mm)
h = 12.0
xs = 84.0
A2 = (xs - h / math.tan(math.radians(18)), g)
B2 = (xs - h / math.tan(math.radians(21.25)), g)
S = (xs, g + h)
poly(ax, [A2, B2, S], 'autre')
line(ax, [(A2[0] - 3, g), (xs + 2, g)], 'fixe', lw=0.7)
line(ax, [S, (xs, g)], 'fixe', dash=True, lw=0.7)
arc(A2[0], g, 5, 0, 18, 'autre'); arc(B2[0], g, 4, 0, 21.25, 'autre')
text(ax, A2[0] - 1, g - 3.5, 'α', 'autre', 's', weight='bold')
text(ax, B2[0] + 3, g - 3.5, 'β', 'autre', 's', weight='bold')
text(ax, 65, 58, 'Montagne', 'autre', 'm', weight='bold')
text(ax, 65, 54, 'vue de côté', 'autre', 's')
text(ax, 65, 6, 'cercle vertical', 'autre', 's')
save(fig, '38-048')
