import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 12, 42, 20, 11, 'sujet', label=r'$x$', size='xl')
for i, v in enumerate(('35', '25', '10')):
    cx = 8 + 14 * i
    box(ax, cx - 6, 22, 12, 8, 'sujet', label=v)
    arrow(ax, (22, 42), (cx, 30.5), 'sujet')
text(ax, 22, 12, 'variable : 3 valeurs', 'sujet', 's')
line(ax, [(47, 6), (47, 54)], 'fixe', dash=True)
box(ax, 62, 42, 20, 11, 'autre', label=r'$h$', size='xl')
box(ax, 62, 22, 20, 8, 'autre', label='5 890')
arrow(ax, (72, 42), (72, 30.5), 'autre')
text(ax, 72, 12, 'constante : 1 valeur', 'autre', 's')
save(fig, '12-016')
