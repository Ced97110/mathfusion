import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
c1, c2 = 52, 76
rows = [(56, '$x$', [(c1, 'sujet', '$x$')]), (44, '$x-1$', [(c2, 'autre', '$x-1$')]),
        (32, '$x(x-1)$', [(c1, 'sujet', '$x$'), (c2, 'autre', '$x-1$')])]
for y, lab, cells in rows:
    text(ax, 20, y + 4, lab, 'encre', 's')
    for c, r, s in cells: box(ax, c - 10, y, 20, 8, r, label=s, size='s')
line(ax, [(4, 27), (86, 27)], 'fixe')
text(ax, 20, 18, 'PPCM', 'resultat', 's')
box(ax, c1 - 10, 14, 20, 8, 'resultat', label='$x$', size='s')
box(ax, c2 - 10, 14, 20, 8, 'resultat', label='$x-1$', size='s')
text(ax, 44, 5, 'chaque facteur : une fois', 'fixe', 's')
save(fig, '21-120')
