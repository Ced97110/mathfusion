import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
k = 3.2; cx = 30; yb = 8
B = (cx - 5 * k, yb); C = (cx + 5 * k, yb); A = (cx, yb + 5 * math.sqrt(3) * k)
mid = lambda P, Q: ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)
poly(ax, [A, B, C], 'sujet')
for V, S in ((A, mid(B, C)), (B, mid(C, A)), (C, mid(A, B))): line(ax, [V, S], 'resultat', lw=1.0, dash=True)
O = (cx, yb + 5 * math.sqrt(3) * k / 3)
disc(ax, O[0], O[1], 1.1, 'varie')
for t1, t2, dx in ((-120, -90, -1), (-90, -60, 1)):
    ax.add_patch(matplotlib.patches.Arc(A, 12, 12, theta1=t1, theta2=t2, ec=COL['varie'], lw=1.0, zorder=3))
    text(ax, A[0] + dx * 5.2, A[1] - 9.5, '30°', 'varie', 's')
line(ax, [(cx - 2, yb), (cx - 2, yb + 2), (cx, yb + 2)], 'fixe', lw=0.7)
text(ax, cx - 8, yb - 3.2, '5', 'fixe', 's'); text(ax, cx + 8, yb - 3.2, '5', 'fixe', 's')
arrow(ax, (60, O[1]), (O[0] + 1.8, O[1]), 'varie'); text(ax, 62, O[1], '$O$ = $I$', 'varie', 'm', ha='left')
text(ax, 62, 40, 'médiatrice', 'resultat', 's', ha='left'); text(ax, 62, 35.5, '= bissectrice', 'resultat', 's', ha='left')
save(fig, '37-133')
