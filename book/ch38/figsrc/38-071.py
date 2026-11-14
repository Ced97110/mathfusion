import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians
from matplotlib.patches import Arc

s = 0.016
fig, ax = canvas(66)
AH, hh = 1796.0, 2420.0
# --- vue de dessus : triangle horizontal A, B, H (angle 146,8° en A, 21,45° en B) ---
A = (28, 13); B = (A[0] + 1000*s, A[1])
H = (A[0] + AH*s*cos(radians(146.8)), A[1] + AH*s*sin(radians(146.8)))
poly(ax, [A, B, H], 'fixe')
line(ax, [A, B], 'fixe', 1.2); line(ax, [B, H], 'fixe', 1.0); line(ax, [A, H], 'sujet', 2.2)
ax.add_patch(Arc(A, 12, 12, theta1=0, theta2=146.8, ec=COL['varie'], lw=1.0, zorder=3))
ax.add_patch(Arc(B, 14, 14, theta1=158.5, theta2=180, ec=COL['varie'], lw=1.0, zorder=3))
line(ax, [(A[0] + 2, A[1] + 11.3), (A[0] + 6*cos(radians(80)), A[1] + 6*sin(radians(80)))], 'varie', 0.6)
text(ax, A[0] + 2, A[1] + 13.5, '146,8°', 'varie', 's', weight='bold')
line(ax, [(B[0] - 3, B[1] + 9.2), (B[0] + 7*cos(radians(169)), B[1] + 7*sin(radians(169)))], 'varie', 0.6)
text(ax, B[0] - 2.5, B[1] + 11.2, '21,45°', 'varie', 's', weight='bold')
text(ax, (A[0] + B[0]) / 2, A[1] - 4.5, '1000 m', 'fixe', 's')
text(ax, (A[0] + H[0]) / 2 - 2.4, (A[1] + H[1]) / 2 - 3.2, 'AH ≈ 1796 m', 'sujet', 's', rot=-33.2, weight='bold')
text(ax, 22, 56, 'vue de dessus', 'encre', 's', weight='bold')
# --- vue de côté : triangle vertical A, H, ballon (rectangle en H) ---
A2 = (53, 13); H2 = (A2[0] + AH*s, 13); S = (H2[0], 13 + hh*s)
poly(ax, [A2, H2, S], 'fixe')
line(ax, [A2, H2], 'sujet', 2.2); line(ax, [H2, S], 'resultat', 2.2); line(ax, [A2, S], 'fixe', 1.0)
d = 2.2
line(ax, [(H2[0] - d, 13), (H2[0] - d, 13 + d), (H2[0], 13 + d)], 'fixe', 0.7)
disc(ax, S[0], S[1], 1.3, 'resultat'); text(ax, S[0] - 1, S[1] + 4, 'ballon', 'resultat', 's')
text(ax, (A2[0] + H2[0]) / 2, 8.5, 'AH ≈ 1796 m', 'sujet', 's', weight='bold')
text(ax, H2[0] - 2.8, 32, 'h ≈ 2420 m', 'resultat', 's', ha='right', weight='bold')
text(ax, 68, 56, 'vue de côté', 'encre', 's', weight='bold')
text(ax, 44, 2.5, 'AH est le résultat du 1er triangle, un côté du 2e', 'sujet', 's')
save(fig, '38-071')
