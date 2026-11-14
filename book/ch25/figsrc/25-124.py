import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="varie", n=24):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role)
fig, ax = canvas(66)
A = (12, 14); C = (58, 14)
line(ax, [(4, 14), (84, 14)], 'fixe')
arrow(ax, A, (A[0], 60), 'sujet', lw=1.6)
arrow(ax, C, (C[0], 60), 'fixe', lw=1.6)
for X in (A, C):
    line(ax, [(X[0] + 3, 14), (X[0] + 3, 17), (X[0], 17)], 'fixe')
text(ax, 12, 9, r'$A$', 'sujet', 's'); text(ax, 58, 9, r'$C$', 'fixe', 's')
text(ax, 9, 30, 'visée à 90°', 'sujet', 's', ha='right') if False else text(ax, 10, 30, 'visée', 'sujet', 's', ha='right')
text(ax, 60, 30, 'verticale de C', 'fixe', 's', ha='left')
text(ax, 35, 30, 'ne se coupent', 'limite', 's'); text(ax, 35, 26, 'jamais', 'limite', 's')
ax.add_patch(Circle((35, 54), 4, ec=COL['limite'], fc='none', lw=0.9, ls='--', zorder=2))
text(ax, 35, 54, '×', 'limite', 'l'); text(ax, 43, 54, r'$B$', 'limite', 'm', ha='left')
text(ax, 35, 42, r'$B$ n’existe pas', 'limite', 'm', weight='bold')
save(fig, '25-124')
