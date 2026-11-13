import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(74)
ox, oy, u = 32, 24, 14
Q = lambda x, y: (ox + x * u, oy + y * u)
line(ax, [Q(-1.8, 0), Q(2.9, 0)], 'fixe', lw=1.3)
line(ax, [Q(-1.6, -1.6), Q(2.7, 2.7)], 'fixe', lw=1.3)
text(ax, Q(2.9, 0)[0] + 1, Q(2.9, 0)[1] - 3, r'$L_1$', 'fixe', 'm', ha='left')
text(ax, Q(2.7, 2.7)[0] + 1, Q(2.7, 2.7)[1] + 1, r'$L_2$', 'fixe', 'm', ha='left')
r = math.sqrt(5) * u
a0, a1 = math.atan2(1, 2), math.atan2(2, -1)
pts = [(ox + r * math.cos(a0 + (a1 - a0) * k / 30), oy + r * math.sin(a0 + (a1 - a0) * k / 30)) for k in range(31)]
line(ax, pts[:-3], 'resultat', lw=1.4, dash=True)
arrow(ax, pts[-4], pts[-1], 'resultat', lw=1.4)
text(ax, Q(0.45, 2.0)[0], Q(0.45, 2.0)[1] + 6, '90°', 'resultat', 's')
arrow(ax, Q(2, 0.85), Q(2, -0.85), 'varie')
arrow(ax, Q(1.85, -0.85), Q(-0.85, 1.85), 'varie')
disc(ax, *Q(2, 1), 1.3, 'sujet'); disc(ax, *Q(2, -1), 1.3, 'varie'); disc(ax, *Q(-1, 2), 1.3, 'resultat')
text(ax, Q(2, 1)[0] + 3, Q(2, 1)[1] + 2, r'$P$', 'sujet', 'm', ha='left')
text(ax, Q(2, -1)[0] + 3, Q(2, -1)[1] - 2, r"$P'$", 'varie', 'm', ha='left')
text(ax, Q(-1, 2)[0] - 3, Q(-1, 2)[1] + 2, r"$P''$", 'resultat', 'm', ha='right')
text(ax, Q(2.15, 0.5)[0], Q(2.15, 0.5)[1], 'pli 1', 'varie', 's', ha='left')
text(ax, Q(-0.6, 0.6)[0], Q(-0.6, 0.6)[1], 'pli 2', 'varie', 's')
ax.plot([ox + 6, ox + 6 * math.cos(math.pi/4)*1.0 + 0], [oy, oy + 6 * math.sin(math.pi/4)], alpha=0)
t = [math.radians(d) for d in range(0, 46, 3)]
line(ax, [(ox + 6.5 * math.cos(a), oy + 6.5 * math.sin(a)) for a in t], 'encre', lw=0.7)
text(ax, ox + 11.5, oy + 3.3, '45°', 'encre', 's')
save(fig, '72-134')
