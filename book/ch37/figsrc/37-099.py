import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
u = 4.6; ox, oy = 6, 16
P = lambda x, y: (ox + u * x, oy + u * y)
A, B, C = P(0, 0), P(6, 0), P(5, 4)
poly(ax, [A, B, C], 'sujet')
from matplotlib.patches import Arc
ax.add_patch(Arc(A, 14, 14, theta1=0, theta2=38.66, ec=COL['varie'], lw=1.2, zorder=4))
text(ax, A[0] - 2.5, A[1] - 2.5, 'A', 'sujet', weight='bold')
text(ax, (A[0] + B[0]) / 2, A[1] - 3.5, r'$p = 6$', 'sujet')
text(ax, 14, 33, r'$q \approx 6{,}40$', 'sujet', ha='center')
text(ax, 23, 20.5, r'$\beta-\alpha$ = 38,66°', 'varie', 's')
bx, bw = 36, 51
box(ax, bx, 56, bw, 16, 'sujet', label='départ\n' + r'$\Delta=\frac{1}{2}\,pq\,\sin(\beta-\alpha)$', size='s')
box(ax, bx, 32, bw, 16, 'varie', label='étape clé : formule d’addition\n' + r'$\sin(\beta-\alpha)=\sin\beta\,\cos\alpha-\cos\beta\,\sin\alpha$', size='s')
box(ax, bx, 6, bw, 18, 'resultat', label='arrivée, sans angle\n' + r'$X_2Y_3-X_3Y_2 = 24$', size='s')
arrow(ax, (bx + bw / 2, 56), (bx + bw / 2, 48), 'fixe'); arrow(ax, (bx + bw / 2, 32), (bx + bw / 2, 24), 'fixe')
save(fig, '37-099')
