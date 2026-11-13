import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
Arc = matplotlib.patches.Arc
B, C = (8, 46), (32, 46)
Arc(B, 32, 32, theta1=-55, theta2=55); 
for c, a1, a2 in ((B, -55, 55), (C, 125, 235)):
    ax.add_patch(Arc(c, 32, 32, theta1=a1, theta2=a2, ec=COL['varie'], lw=1.5, zorder=3))
Xt = (20, 46 + math.sqrt(16 ** 2 - 12 ** 2))
line(ax, [B, Xt], 'varie', lw=0.8, dash=True); line(ax, [C, Xt], 'varie', lw=0.8, dash=True)
text(ax, 0.5, 58, 'même rayon', 'varie', 's', ha='left')
line(ax, [B, C], 'sujet', lw=1.2); disc(ax, *B, 0.9, 'sujet'); disc(ax, *C, 0.9, 'sujet')
text(ax, 8, 41.5, '$B$', 'sujet', 'm'); text(ax, 32, 41.5, '$C$', 'sujet', 'm')
h = math.sqrt(16 ** 2 - 12 ** 2)
line(ax, [(20, 46 - h - 5), (20, 46 + h + 5)], 'resultat', lw=1.3)
text(ax, 22, 69, 'médiatrice', 'resultat', 'm')
A = (50, 34); L = 34
S1 = (A[0] + L, A[1]); S2 = (A[0] + L * math.cos(math.radians(60)), A[1] + L * math.sin(math.radians(60)))
line(ax, [A, S1], 'sujet', lw=1.2); line(ax, [A, S2], 'sujet', lw=1.2)
ax.add_patch(Arc(A, 20, 20, theta1=0, theta2=60, ec=COL['varie'], lw=0.9, zorder=3))
M = (A[0] + 10, A[1]); N = (A[0] + 10 * math.cos(math.radians(60)), A[1] + 10 * math.sin(math.radians(60)))
mid = ((M[0] + N[0]) / 2, (M[1] + N[1]) / 2); hh = math.sqrt(64 - 25)
X = (mid[0] + hh * math.cos(math.radians(30)), mid[1] + hh * math.sin(math.radians(30)))
for c in (M, N):
    a = math.degrees(math.atan2(X[1] - c[1], X[0] - c[0]))
    ax.add_patch(Arc(c, 16, 16, theta1=a - 25, theta2=a + 25, ec=COL['varie'], lw=1.5, zorder=3))
text(ax, 77, 55, 'même rayon', 'varie', 's')
line(ax, [A, (A[0] + 30 * math.cos(math.radians(30)), A[1] + 30 * math.sin(math.radians(30)))], 'resultat', lw=1.3)
text(ax, 46, 34, '$A$', 'sujet', 'm')
text(ax, 66, 69, 'bissectrice', 'resultat', 'm')
text(ax, 22, 16, '2 médiatrices → $O$', 'resultat', 's'); text(ax, 66, 16, '2 bissectrices → $I$', 'resultat', 's')
text(ax, 44, 6, 'règle sans graduation + compas', 'fixe', 's')
save(fig, '37-137')
