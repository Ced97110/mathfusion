import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 19; O = (30, 30)
disc(ax, O[0], O[1], u, 'sujet')
for i in range(-1, 3):
    for j in range(-1, 2):
        x, y = O[0] + i*u, O[1] + j*u
        if (i, j) != (0, 0): disc(ax, x, y, 1.0, 'fixe')
disc(ax, O[0], O[1], 1.2, 'encre')
arrow(ax, (O[0]+1.5, O[1]), (O[0]+u-1.2, O[1]), 'sujet', lw=1.4)
text(ax, O[0]+u/2, O[1]+3, r'$v$', 'sujet', 'l')
text(ax, O[0]-3.5, O[1]-3, r'$O$', 'encre', 's')
text(ax, O[0], O[1]+9.5, 'disque vide', 'sujet', 's')
text(ax, O[0], 5, r'rayon $|v|$ : le plus court', 'sujet', 's')
text(ax, 77, 30+u+2, 'autres points', 'fixe', 's')
text(ax, 77, 30+u-2, 'plus loin', 'fixe', 's')
save(fig, '74-132')
