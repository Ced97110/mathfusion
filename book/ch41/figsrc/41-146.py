import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
ox, oy, s = 8, 26, 3.3
P = lambda x, y: (ox + x * s, oy + y * s)
arrow(ax, P(0, 0), P(20, 0), 'fixe', lw=0.7)
arrow(ax, P(0, 0), P(0, 14.5), 'fixe', lw=0.7)
A, B = P(5, 7), P(18, 13)
# déplacement d = <13, 6>
arrow(ax, A, B, 'autre', lw=1.2)
text(ax, 46, 66, r'$d=\langle 13,\ 6\rangle$ m', 'autre')
# force F = <5, 2> tracée au départ (3 mm par newton)
arrow(ax, A, (A[0] + 22.5, A[1] + 9), 'sujet', lw=1.2)
text(ax, A[0] + 19, A[1] - 3, r'$F=\langle 5,\ 2\rangle$ N', 'sujet')
disc(ax, A[0], A[1], 1.0, 'fixe')
disc(ax, B[0], B[1], 1.0, 'fixe')
text(ax, A[0] - 1, A[1] - 4, '(5 ; 7)', 'fixe', 's')
text(ax, B[0] + 1, B[1] + 4, '(18 ; 13)', 'fixe', 's')
box(ax, 6, 3, 76, 12, 'resultat', label=r'$5\times 13+2\times 6=77$ J')
save(fig, '41-146')
