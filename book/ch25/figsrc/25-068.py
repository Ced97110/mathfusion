import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="limite", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(56)
s = 5.0
C = (8, 24); A = (C[0] + 4 * s, C[1]); B = (C[0], C[1] + 3 * s)
poly(ax, [C, A, B], 'fixe'); line(ax, [A, B], 'fixe', lw=1.6)
line(ax, [C, A], 'fixe', lw=1.6); line(ax, [C, B], 'fixe', lw=1.6)
text(ax, C[0] + 2 * s, C[1] - 3.2, '4', 'fixe', 's'); text(ax, C[0] - 3, C[1] + 1.5 * s, '3', 'fixe', 's')
arc(ax, A, 5, 143.13, 180, 'sujet'); text(ax, A[0] + 3, A[1] - 2.5, 'A', 'sujet', 'm', weight='bold')
arc(ax, B, 5, 270, 323.13, 'autre'); text(ax, B[0] + 3.2, B[1] + 2.0, 'B', 'autre', 'm', weight='bold')
box(ax, 44, 40, 40, 11, 'sujet', label=r'$\tan A = 3\,/\,4 = 0{,}75$', size='s')
box(ax, 44, 22, 40, 11, 'autre', label=r'$\tan B = 4\,/\,3 \approx 1{,}333$', size='s')
arrow(ax, (64, 39.5), (64, 33.5), 'varie', both=True)
text(ax, 80, 36.5, 'renversées', 'varie', 's', ha='right')
text(ax, 44, 8, r'$3/4 \times 4/3 = 12/12 = 1$', 'resultat', 'm', weight='bold')
save(fig, '25-068')
