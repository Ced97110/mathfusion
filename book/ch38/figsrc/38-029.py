import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

fig, ax = canvas(70)
g = 36.0
h = 20.0                                   # 1 976 m -> 20 mm (0,0101 mm par mètre)
xs = 66.0
A = (xs - h / math.tan(math.radians(18)), g)
B = (xs - h / math.tan(math.radians(21.25)), g)
H = (xs, g); S = (xs, g + h)
poly(ax, [A, B, S], 'autre')
poly(ax, [B, H, S], 'sujet')
line(ax, [(A[0] - 3, g), (H[0] + 3, g)], 'fixe')
line(ax, [(H[0] - 2.2, g), (H[0] - 2.2, g + 2.2), (H[0], g + 2.2)], 'fixe', lw=0.7)
ax.add_patch(Arc(B, 2 * 8, 2 * 8, theta1=0, theta2=21.25, color=COL['varie'], lw=1.0, zorder=3))
text(ax, A[0] - 1, g + 4, 'A', 'autre', 's', ha='right')
text(ax, B[0], g - 3.5, 'B', 'sujet', 's')
text(ax, H[0], g - 3.5, 'H', 'sujet', 's')
text(ax, S[0], S[1] + 3, 'S', 'sujet', 's')
brace(ax, A[0], B[0], g - 5, 'fixe', label='1 000 m')
ax.add_patch(Arc(A, 2 * 9, 2 * 9, theta1=0, theta2=18, color=COL['autre'], lw=1.0, zorder=3))
text(ax, A[0] + 16, g + 10, '18°', 'autre', 's')
text(ax, B[0] + 17, g + 3.2, '21,25°', 'varie', 's')
text(ax, 38, S[1] + 6.5, 'BS ≈ 5 451 m', 'autre', 's', weight='bold')
text(ax, H[0] + 3, g + h / 2, 'h ≈ 1 976 m', 'resultat', 's', ha='left', weight='bold')
box(ax, 2, 4, 41, 11, 'autre', label='ABS → BS (loi des sinus)', size='s')
box(ax, 45, 4, 41, 11, 'sujet', label='BHS rectangle → h', size='s')
save(fig, '38-029')
