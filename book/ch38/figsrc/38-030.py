import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

def arc(x, y, r, a, b, role, lw=1.1):
    ax.add_patch(Arc((x, y), 2 * r, 2 * r, theta1=a, theta2=b, color=COL[role], lw=lw, zorder=3))

fig, ax = canvas(58)
g = 20.0
B = (44.0, g)
beta = 21.25
L = 36.0
S = (B[0] + L * math.cos(math.radians(beta)), g + L * math.sin(math.radians(beta)))
line(ax, [(5, g), (83, g)], 'fixe')
line(ax, [B, S], 'sujet', lw=1.3)
arc(B[0], B[1], 12, 0, beta, 'varie')
arc(B[0], B[1], 7, beta, 180, 'resultat')
disc(ax, B[0], B[1], 1.1, 'encre')
text(ax, B[0], g - 3.5, 'B', 'encre', 's')
text(ax, S[0] + 1, S[1] + 3, 'S', 'sujet', 's')
text(ax, 10, g + 3, 'A', 'fixe', 's')
text(ax, 66, g + 3.2, '21,25°', 'varie', 's', weight='bold')
text(ax, 38, g + 18, '158,75°', 'resultat', 's', weight='bold')
text(ax, 44, g + 28, '180° − β', 'resultat', 'm', weight='bold')
text(ax, 44, 11, '21,25° + 158,75° = 180°', 'encre', 's')
text(ax, 44, 4.5, 'avec β = 30° : 150°', 'fixe', 's')
save(fig, '38-030')
