import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# 41-039 : tan θ = b/a, puis on vérifie le quadrant. ⟨1 ; 1⟩ -> 45° ; ⟨−1 ; 1⟩ -> la calculatrice dit −45° (faux), vrai : 135°
fig, ax = canvas(72)
C = (44, 38); u = 16
arrow(ax, (8, C[1]), (82, C[1]), 'fixe', lw=0.6)
arrow(ax, (C[0], 26), (C[0], 62), 'fixe', lw=0.6)
v1 = (C[0] + u, C[1] + u); v2 = (C[0] - u, C[1] + u)
bad = (C[0] + 12, C[1] - 12)
arrow(ax, C, v1, 'sujet', lw=1.6)
arrow(ax, C, v2, 'resultat', lw=1.6)
line(ax, [C, bad], 'limite', lw=1.2, dash=True)
ax.add_patch(Arc(C, 24, 24, theta1=0, theta2=45, ec=COL['sujet'], lw=1.0, zorder=3))
ax.add_patch(Arc(C, 14, 14, theta1=0, theta2=135, ec=COL['resultat'], lw=1.0, zorder=3))
ax.add_patch(Arc(C, 18, 18, theta1=-45, theta2=0, ec=COL['limite'], lw=1.0, zorder=3))
text(ax, v1[0] + 2, v1[1] + 3, '⟨1 ; 1⟩', 'sujet', 's', ha='left')
text(ax, v2[0] - 2, v2[1] + 3, '⟨−1 ; 1⟩', 'resultat', 's', ha='right')
text(ax, C[0] + 20, C[1] + 5, '45°', 'sujet', 's')
text(ax, C[0] - 15, C[1] + 4.5, '135°', 'resultat', 's')
text(ax, C[0] + 17, C[1] - 12, '−45° : faux', 'limite', 's', ha='left')
text(ax, 44, 18, '−1 ÷ 1 = −1  →  −45°', 'encre', 's')
text(ax, 44, 11, 'mais il va au nord-ouest', 'encre', 's')
text(ax, 44, 4.2, '−45° + 180° = 135°', 'resultat', 's')
save(fig, '41-039')
