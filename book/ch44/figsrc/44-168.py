import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
bw, x0 = 70, 9
box(ax, x0, 80, bw, 11, 'fixe', label=r'PGCD$(3,\,8)=1$')
box(ax, x0, 54, bw, 14, 'varie', label=r'Bézout : $3\times3+8\times(-1)=1$', weight='bold', size='s')
arrow(ax, (44, 80), (44, 68), 'fixe')
arrow(ax, (44, 54), (44, 44), 'fixe')
u = 6.5
x1 = 44 - 4.5 * u
for i in range(9):
    box(ax, x1 + i * u, 30, u, u, 'resultat' if i == 8 else 'fixe', r=0.2)
brace(ax, x1, x1 + 8 * u, 29, 'fixe', label=r'$8$ : un multiple de 8', down=True)
text(ax, x1 + 8.5 * u, 41, 'reste 1', 'resultat', 's')
text(ax, 44, 8, r'$3\times3=9$, reste 1 : inverse de 3 = 3', 'resultat', 's')
save(fig, '44-168')
