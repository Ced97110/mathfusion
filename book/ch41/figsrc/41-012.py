import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Échelle 1 mm = 4 km. a = 180 -> 45 mm ; v = (50 ; 86,6) -> (12,5 ; 21,65) mm.
fig, ax = canvas(52)
k = 4.0
O = (8, 12)
dx, dy = 50 / k, 86.6 / k
A = (O[0] + 180 / k, O[1])
arrow(ax, O, A, 'sujet', lw=1.4)
# flèche v au départ
arrow(ax, O, (O[0] + dx, O[1] + dy), 'varie', lw=1.5)
line(ax, [O, (O[0] + dx, O[1]), (O[0] + dx, O[1] + dy)], 'fixe', lw=0.6, dash=True)
# copie au bout de a
Q = (A[0] + dx, A[1] + dy)
line(ax, [A, Q], 'varie', lw=1.2, dash=True)
arrow(ax, (Q[0] - (dx) * 0.1, Q[1] - dy * 0.1), Q, 'varie', lw=1.2)
line(ax, [A, (A[0] + dx, A[1]), Q], 'fixe', lw=0.6, dash=True)
text(ax, 4, 8, r'$O$', 'encre', 'm')
text(ax, 30, 8, r'$a$ : 180', 'sujet', 's')
text(ax, O[0] + dx / 2, 8, '50', 'fixe', 's')
text(ax, O[0] + dx + 2, O[1] + dy / 2, '86,6', 'fixe', 's', ha='left')
text(ax, A[0] + dx / 2 + 4, 8, '50', 'fixe', 's')
text(ax, Q[0] + 2, A[1] + dy / 2, '86,6', 'fixe', 's', ha='left')
text(ax, O[0] - 1, O[1] + dy / 2 + 4, r'$v$', 'varie', 'm', ha='right')
text(ax, 42, Q[1] + 6, 'copie de $v$ au bout de $a$', 'varie', 's')
text(ax, 62, Q[1] + 12, 'arrive : 230 est, 86,6 nord', 'resultat', 's')
save(fig, '41-012')
