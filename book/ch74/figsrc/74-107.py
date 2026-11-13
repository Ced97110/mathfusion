import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
box(ax, 2, 62, 84, 22, 'autre', lw=1.1)
text(ax, 44, 79, r'$G_0$ : ce qui tourne ou retourne', 'autre', 's')
text(ax, 44, 69, r'$C_n$ ou $D_n$', 'autre', 'l')
box(ax, 2, 33, 40, 16, 'fixe', label=r'$G$ : le groupe', size='s')
arrow(ax, (22, 50), (22, 61), 'varie'); text(ax, 36, 55.5, r'$f\mapsto A$', 'varie', 's')
box(ax, 2, 2, 84, 24, 'sujet', lw=1.1)
text(ax, 44, 21, r'$T$ : les translations', 'sujet', 's')
for i in range(8):
    for j in range(2):
        disc(ax, 10 + i * 9.5, 13 - j * 6 + 3, 1.1, 'sujet')
arrow(ax, (22, 27), (22, 32), 'varie')
text(ax, 64, 41, 'les deux étages :', 'fixe', 's')
text(ax, 64, 36, 'une question chacun', 'fixe', 's')
save(fig, '74-107')
