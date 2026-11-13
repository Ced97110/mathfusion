import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

def arc(x, y, r, a, b, role, lw=1.0):
    ax.add_patch(Arc((x, y), 2 * r, 2 * r, theta1=a, theta2=b, color=COL[role], lw=lw, zorder=3))

fig, ax = canvas(72)
g = 40.0
# triangle ABS à l'échelle : AB = 10 mm (1 000 m), angles 18° en A et 21,25° en B (extérieur)
A = (4.0, g); B = (14.0, g)
bs = 5450.73 * 0.01
S = (B[0] + bs * math.cos(math.radians(21.25)), g + bs * math.sin(math.radians(21.25)))
poly(ax, [A, B, S], 'autre')
line(ax, [(2, g), (S[0] + 6, g)], 'fixe', lw=0.7)
arc(A[0], A[1], 6, 0, 18, 'autre')
arc(B[0], B[1], 4, 21.25, 180, 'resultat')
text(ax, 17, g + 11, '158,75°', 'resultat', 's', weight='bold')
text(ax, 6, g - 3.5, '18°', 'autre', 's')
text(ax, S[0] - 9, S[1] + 4, '3,25°', 'varie', 's', weight='bold')
text(ax, S[0], S[1] + 3, 'S', 'sujet', 's')
text(ax, 44, 26, '180 − 18 − 158,75 = 3,25', 'encre', 's')
text(ax, 44, 17, 'β − α = 21,25 − 18 = 3,25', 'varie', 's', weight='bold')
text(ax, 44, 7, 'même résultat : β − α', 'resultat', 's')
save(fig, '38-031')
