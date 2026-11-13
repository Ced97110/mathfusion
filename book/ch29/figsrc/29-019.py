import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(64)
c = (14, 8); R = 50
A = pt(c, R, 0); B = pt(c, R, 60)
poly(ax, [c, A, B], 'fixe')
line(ax, arcpts(c, R, -3, 64, 50), 'fixe', lw=0.7)
line(ax, arcpts(c, R, 0, 60, 50), 'varie', lw=2.0)
line(ax, [A, B], 'resultat', lw=2.0)
line(ax, [c, A], 'sujet', lw=1.2); line(ax, [c, B], 'sujet', lw=1.2)
for p in (c, A, B): disc(ax, p[0], p[1], 1.0, 'sujet')
text(ax, 38, 3.5, 'r', 'sujet', 'm'); text(ax, 22, 33, 'r', 'sujet', 'm')
text(ax, 25, 11, '60°', 'sujet', 's'); text(ax, A[0] - 8, 11, '60°', 'sujet', 's'); text(ax, B[0], B[1] - 8, '60°', 'sujet', 's')
text(ax, B[0] - 4, B[1] + 2.5, 'B′', 'sujet', 'm'); text(ax, A[0] + 4, A[1], 'A', 'sujet', 'm'); text(ax, 9, 5, 'O', 'sujet', 'm')
text(ax, 86, 42, 'arc AB′ > r', 'varie', 'm', ha='right'); text(ax, 86, 34, 'AB′ = r', 'resultat', 'm', ha='right')
text(ax, 86, 24, '1 rad < 60°', 'resultat', 'm', ha='right', weight='bold')
save(fig, '29-019')
