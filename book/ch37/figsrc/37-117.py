import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 5.5; ox, oy = 7, 7
P = lambda x, y: (ox + u * x, oy + u * y)
for i in range(1, 9): line(ax, [P(i, 0), P(i, 5.6)], 'fixe', lw=0.25)
for j in range(1, 6): line(ax, [P(0, j), P(8.2, j)], 'fixe', lw=0.25)
arrow(ax, P(0, 0), P(8.4, 0), 'fixe'); arrow(ax, P(0, 0), P(0, 6.2), 'fixe')
A, B, C = P(1, 1), P(7, 1), P(6, 5)
poly(ax, [A, B, C], 'sujet')
for q in (A, B, C): disc(ax, q[0], q[1], 0.9, 'sujet')
text(ax, A[0] - 2.5, A[1] + 2.5, 'A', 'sujet', weight='bold'); text(ax, B[0] + 2.5, B[1] + 2.5, 'B', 'sujet', weight='bold'); text(ax, C[0] + 2.8, C[1] + 1.5, 'C', 'sujet', weight='bold')
bx, bw, h = 52, 34, 7.5
rows = [(r'A : $1\times(1-5)=-4$', 'sujet'), (r'B : $7\times(5-1)=28$', 'sujet'), (r'C : $6\times(1-1)=0$', 'sujet')]
text(ax, 44, 57, r'$x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)$', 'encre', 's')
for i, (lab, role) in enumerate(rows): box(ax, bx, 41 - i * 10, bw, h, role, label=lab, size='s')
box(ax, bx, 11, bw, 8, 'varie', label=r'somme $=24$', size='s')
text(ax, bx + bw / 2, 4, r'aire $=\frac{1}{2}\times|24|=12$', 'resultat', 's')
save(fig, '37-117')
