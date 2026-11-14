import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

fig, ax = canvas(78)
k = 0.9                                     # mm par mètre
d = 50 * k
h = 50 * math.tan(math.radians(40)) * k     # 41,95 m
E = (8, 22); H = (E[0] + d, E[1]); S = (H[0], E[1] + h)
poly(ax, [E, H, S], 'sujet')
line(ax, [(H[0] - 2.2, H[1]), (H[0] - 2.2, H[1] + 2.2), (H[0], H[1] + 2.2)], 'fixe', lw=0.7)
ax.add_patch(Arc(E, 22, 22, theta1=0, theta2=40, color=COL['varie'], lw=1.1, zorder=3))
text(ax, E[0] + 17, E[1] + 3.2, r'$\theta$ = 40°', 'varie', 's', weight='bold')
text(ax, (E[0] + H[0]) / 2, E[1] - 3.2, 'd = 50 m', 'fixe', 'm', weight='bold')
text(ax, H[0] + 2.5, E[1] + h / 2, r'$h \approx$ 41,95 m', 'resultat', 's', ha='left', weight='bold')
text(ax, S[0], S[1] + 3, 'sommet', 'sujet', 's')
# trois actions
box(ax, 3, 3, 82, 9, 'sujet', label=r'$h = d\,\tan\theta$ = 50 × 0,8391 ≈ 41,95 m', size='s')
save(fig, '38-027')
