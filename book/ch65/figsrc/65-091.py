import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 73, 'racines 1, 2, 3, 4', 'sujet', 's')
rows = [
    (r'$t_1-t_2 = 3$', r'$(r_1-r_4)(r_2-r_3)$', r'$(-3)(-1)$'),
    (r'$t_1-t_3 = 4$', r'$(r_1-r_3)(r_2-r_4)$', r'$(-2)(-2)$'),
    (r'$t_2-t_3 = 1$', r'$(r_1-r_2)(r_3-r_4)$', r'$(-1)(-1)$'),
]
for j, (a, b, c) in enumerate(rows):
    y = 56 - j * 14
    box(ax, 2, y, 26, 9, 'autre', label=a, size='s')
    line(ax, [(29.5, y + 3.6), (32.5, y + 3.6)], 'fixe')
    line(ax, [(29.5, y + 5.4), (32.5, y + 5.4)], 'fixe')
    box(ax, 34, y, 32, 9, 'sujet', label=b, size='s')
    text(ax, 77, y + 4.5, c, 'sujet', 's')
box(ax, 4, 4, 80, 13, 'resultat', label=r'$3\times4\times1 = 12$ : $d = 12^2 = 144$ pour $f$ et $g$', size='s')
save(fig, '65-091')
