import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
# e1 -> 2 f1 + f2 ; rho(f1) = (1,1), rho(f2) = (0,1) ; 2(1,1) + (0,1) = (2,3)
assert (2 * 1 + 0, 2 * 1 + 1) == (2, 3)
BX, BW, BH = 11, 76, 20
rows = [(76, 'sujet', '1', r'image du sac, en lots $f$ (nombres $a$)', r'$\eta(e_i)=\sum_j a_{ji}f_j$', r'$\eta(e_1)=2f_1+f_2$'),
        (42, 'varie', '2', 'chaque lot remplacé par son image', r'$\sum_j a_{ji}\,\rho(f_j)$', r'$2\,(1,1)+(0,1)$'),
        (8, 'resultat', '3', r'image en lots $g$ (nombres $a$ et $c$)', r'$\sum_j\sum_k a_{ji}c_{kj}g_k$', r'$(\rho\circ\eta)(e_1)=(2,3)$')]
for y, r, k, t, g, c in rows:
    box(ax, BX, y, BW, BH, r)
    disc(ax, 5.5, y + BH / 2, 3.4, r, label=k, size='m')
    text(ax, BX + BW / 2, y + 16.5, t, r, 's')
    text(ax, BX + BW / 2, y + 10, g, 'encre', 'm')
    text(ax, BX + BW / 2, y + 3.8, c, r, 's')
arrow(ax, (16, 75.5), (16, 62.5), 'varie')
text(ax, 20, 69, r'$\rho$ entre dans la somme', 'varie', 's', ha='left')
arrow(ax, (16, 41.5), (16, 28.5), 'fixe')
text(ax, 20, 35, r'$\rho(f_j)=\sum_k c_{kj}g_k$', 'fixe', 's', ha='left')
save(fig, '58-212')
