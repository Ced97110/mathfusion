import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 4, 44, 14, 9, 'fixe', label='7')
arrow(ax, (18, 48.5), (30, 48.5), 'fixe')
text(ax, 58, 48.5, 'vaut 7 : pas le choix', 'fixe', 'm')
line(ax, [(2, 38), (86, 38)], 'fixe', lw=0.5, dash=True)
disc(ax, 10, 20, 6, 'sujet', label='$x$', size='l')
for y, s, r in ((28, '$x$ = 35', 'rue 1'), (10, '$x$ = 25', 'rue 2')):
    arrow(ax, (16, 20), (36, y), 'varie')
    box(ax, 38, y - 4.5, 22, 9, 'varie', label=s)
    text(ax, 72, y, r, 'varie', 'm')
text(ax, 22, 33, 'vous décidez', 'varie', 's')
save(fig, '12-018')
