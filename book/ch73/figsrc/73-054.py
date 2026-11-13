import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'$n = 3$ : trois fois $d = 2$', 'sujet', 'm')
c = 13
for i in range(3):
    for j in range(3):
        d = i == j
        box(ax, 24 + j*c, 24 + (2-i)*c, c-1, c-1, 'sujet' if d else 'fixe', label='2' if d else '0', size='m', r=0.6)
text(ax, 44, 17, 'diagonale : 2, 2, 2', 'sujet', 's')
text(ax, 44, 8, r'$\det = 2 \times 2 \times 2 = 8$', 'resultat', 's')
save(fig, '73-054')
