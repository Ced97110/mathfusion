import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="limite", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(54)
t40 = 0.8391
C = (6, 10); A = (C[0] + 22, C[1]); B = (C[0], C[1] + 22 * t40)
poly(ax, [C, A, B], 'fixe')
line(ax, [C, A], 'fixe', lw=1.6); line(ax, [C, B], 'fixe', lw=1.6); line(ax, [A, B], 'fixe', lw=1.6)
arc(ax, A, 5, 140, 180, 'sujet'); text(ax, A[0] - 7.5, A[1] + 2.8, '40°', 'sujet', 's', weight='bold')
arc(ax, B, 5, 270, 320, 'varie'); text(ax, B[0] + 4.2, B[1] - 8.2, '50°', 'varie', 's', weight='bold')
box(ax, 34, 33, 50, 9, 'varie', label='90° − 40° = 50°')
box(ax, 34, 19, 50, 9, 'sujet', label='tan 50° = 1,1918')
box(ax, 34, 3, 50, 9, 'autre', label='1 ÷ 0,8391 ≈ 1,1918')
arrow(ax, (59, 32.5), (59, 28.5), 'varie')
text(ax, 59, 15.5, '=', 'resultat', 'l', weight='bold')
text(ax, 44, 49, r'$\tan(90° - A) = 1\,/\tan A$', 'encre', 'l')
save(fig, '25-069')
