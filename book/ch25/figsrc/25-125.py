import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="varie", n=24):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role)
fig, ax = canvas(62)
A = (8, 10); R = 40
t = [math.radians(a) for a in (80, 89)]
ax.add_patch(matplotlib.patches.Arc(A, 2 * R, 2 * R, theta1=60, theta2=90, ec=COL['fixe'], lw=0.8, ls='--'))
line(ax, [A, (26, 10)], 'fixe')
for a, r in zip(t, ('sujet', 'autre')):
    P = (A[0] + R * math.cos(a), A[1] + R * math.sin(a))
    line(ax, [A, P], r, lw=1.4)
    line(ax, [(P[0], 10), P], r, lw=1.0, dash=True)
text(ax, 5, 6, r'$A$', 'fixe', 's')
text(ax, 30, 57, 'hypoténuse = 1', 'fixe', 's', ha='left')
text(ax, 30, 46, '80° : adjacent 0,1736', 'sujet', 's', ha='left')
text(ax, 30, 41.5, 'opposé 0,9848', 'sujet', 's', ha='left')
text(ax, 30, 33, '89° : adjacent 0,0175', 'autre', 's', ha='left')
text(ax, 30, 28.5, 'opposé 0,9998', 'autre', 's', ha='left')
text(ax, 30, 20, 'adjacent → 0, opposé → 1', 'varie', 's', ha='left')
box(ax, 30, 3, 50, 9, 'resultat', label='tan = opposé/adjacent → 1/0', size='s')
save(fig, '25-125')
