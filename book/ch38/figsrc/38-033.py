import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

fig, ax = canvas(66)
k = 0.0101                                  # mm par mètre : BS = 5 451 m -> 55 mm
beta = math.radians(21.25)
bs = 5450.73 * k
B = (6.0, 26.0)
H = (B[0] + bs * math.cos(beta), B[1])
S = (H[0], B[1] + bs * math.sin(beta))
poly(ax, [B, H, S], 'sujet')
line(ax, [B, S], 'varie', lw=1.4)
line(ax, [S, H], 'resultat', lw=1.6)
line(ax, [(H[0] - 2.2, B[1]), (H[0] - 2.2, B[1] + 2.2), (H[0], B[1] + 2.2)], 'fixe', lw=0.7)
ax.add_patch(Arc(B, 2 * 13, 2 * 13, theta1=0, theta2=21.25, color=COL['varie'], lw=1.0, zorder=3))
text(ax, B[0] + 19, B[1] + 2.8, '21,25°', 'varie', 's', weight='bold')
text(ax, B[0] + 17, B[1] + 18, 'BS ≈ 5 451 m', 'varie', 's', weight='bold')
text(ax, H[0] + 2, (B[1] + S[1]) / 2, 'h ≈ 1 976 m', 'resultat', 's', ha='left', weight='bold')
text(ax, B[0], B[1] - 3.5, 'B', 'sujet', 's')
text(ax, H[0], B[1] - 3.5, 'H', 'sujet', 's')
text(ax, S[0] - 1, S[1] + 3, 'S', 'sujet', 's')
box(ax, 2, 3, 84, 9, 'sujet', label=r'$\sin\beta = h\,/\,BS$  →  $h = BS\,\sin\beta$', size='s')
text(ax, 44, 17.5, 'h = 5 451 × 0,36244 ≈ 1 976 m', 'resultat', 's')
save(fig, '38-033')
