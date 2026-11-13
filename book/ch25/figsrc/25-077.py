import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="limite", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(54)
C = (14, 12); A = (C[0] + 22, C[1]); B = (C[0], C[1] + 24)
poly(ax, [C, A, B], 'fixe')
line(ax, [C, A], 'fixe', lw=2.0); line(ax, [C, B], 'fixe', lw=2.0); line(ax, [A, B], 'fixe', lw=1.2, dash=True)
text(ax, C[0] + 11, C[1] - 3.2, '154 cm', 'fixe', 's'); text(ax, C[0] - 7, C[1] + 12, '168 cm', 'fixe', 's')
arc(ax, A, 6, 132.5, 180, 'varie'); text(ax, A[0] - 9.5, A[1] + 2.8, '?', 'varie', 'l', weight='bold')
box(ax, 48, 40, 36, 9, 'sujet', label='angle')
box(ax, 48, 12, 36, 9, 'resultat', label='rapport 1,0909', size='s')
arrow(ax, (58, 39.5), (58, 21.5), 'fixe'); text(ax, 54.5, 30.5, 'tan', 'fixe', 's', ha='right')
arrow(ax, (74, 21.5), (74, 39.5), 'varie', lw=1.6); text(ax, 76, 30.5, 'arctan', 'varie', 's', ha='left', weight='bold')
save(fig, '25-077')
