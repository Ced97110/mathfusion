import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 9, 64, 70, 10, 'sujet', label='x − y multiple de 4 et de 3', size='s')
box(ax, 9, 44, 70, 13, 'varie', label='donc multiple de 12\n(4 et 3 sans facteur commun)', size='s', lw=1.6)
box(ax, 9, 26, 70, 10, 'resultat', label='x − y = 0, donc x = y', size='s')
arrow(ax, (44, 64), (44, 57.5), 'fixe'); arrow(ax, (44, 44), (44, 36.5), 'fixe')
f = lambda v: 44 + v * 2.7
y = 11
line(ax, [(f(-12), y), (f(12), y)], 'fixe', lw=0.8)
line(ax, [(f(-11), y), (f(11), y)], 'sujet', lw=3.0)
for v in (-12, 0, 12):
    disc(ax, f(v), y, 1.5, 'resultat' if v == 0 else 'fixe')
    text(ax, f(v), y - 5, str(v).replace('-', '−'), 'resultat' if v == 0 else 'fixe', 's')
text(ax, 44, y + 6, 'entre −11 et 11 : seul 0 est multiple de 12', 'sujet', 's')
save(fig, '60-019')
