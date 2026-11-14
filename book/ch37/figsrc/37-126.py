import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
B, C = (4, 26), (36, 26)
A = (4 + 12.16, 26 + 10.4)
a, b, c = 32.0, math.hypot(A[0] - C[0], A[1] - C[1]), math.hypot(A[0] - B[0], A[1] - B[1])
per = a + b + c
I = ((a * A[0] + b * B[0] + c * C[0]) / per, (a * A[1] + b * B[1] + c * C[1]) / per)
r = a * 10.4 / per
poly(ax, [A, B, C], 'fixe')
ax.add_patch(Circle(I, r, ec=COL['sujet'], fc=FILL['sujet'], lw=1.0, zorder=3))
text(ax, 20, 44, 'Δ > 0 : une mare', 'sujet', 's')
arrow(ax, (38, 33), (46, 33), 'varie'); text(ax, 42, 38, 'aplatir', 'varie', 's')
u = 3.5; y = 26; Bx, Ax, Cx = 48, 48 + 4 * u, 48 + 10 * u
line(ax, [(Bx, y), (Cx, y)], 'fixe', lw=1.2)
disc(ax, Ax, y, 0.9, 'sujet')
for x, l in ((Bx, '$B$'), (Ax, '$A$'), (Cx, '$C$')): text(ax, x, y - 4, l, 'fixe', 'm')
text(ax, 66, 44, 'Δ = 0 : aplati', 'fixe', 's')
text(ax, 66, 14, 'r = Δ ÷ s = 0 ÷ 10 = 0', 'sujet', 's')
text(ax, 66, 8, 'rayon 0 : un point', 'sujet', 's')
save(fig, '37-126')
