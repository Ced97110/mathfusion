import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 55, r'$\tau=(r_2\ r_3)$', 'varie', 'xl')
xs = {1: 14, 2: 46, 3: 76}
disc(ax, xs[1], 30, 5, 'fixe', label='$r_1$', size='m')
disc(ax, xs[2], 30, 5, 'sujet', label='$r_2$', size='m')
disc(ax, xs[3], 30, 5, 'sujet', label='$r_3$', size='m')
arrow(ax, (xs[2] + 2, 35), (xs[3] - 2, 35), 'varie', curve=-0.45)
arrow(ax, (xs[3] - 2, 25), (xs[2] + 2, 25), 'varie', curve=-0.45)
brace(ax, 38, 84, 14, 'sujet', label='écrites dans le signe', down=True)
text(ax, xs[1], 20, 'reste en place,\nabsente du signe', 'fixe', 's')
save(fig, '65-016')
