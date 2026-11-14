import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
box(ax, 4, 90, 36, 10, 'sujet', True, r'$x+y=10$', 'l')
box(ax, 48, 90, 36, 10, 'autre', True, r'$x\times y=21$', 'l')
arrow(ax, (22, 90), (22, 82), 'varie')
text(ax, 26, 86, r'$y$ devient $10-x$', 'varie', 's', ha='left')
arrow(ax, (66, 90), (56, 82), 'autre')
rows = [(72, r'$x\times(10-x)=21$', 'fixe'), (52, r'$x^2-10x+21=0$', 'varie'), (32, r'$(x-3)(x-7)=0$', 'fixe')]
for y, s, r in rows:
    box(ax, 22, y, 44, 10, r, True, s, 'l')
arrow(ax, (44, 72), (44, 62), 'varie')
arrow(ax, (44, 52), (44, 42), 'varie')
text(ax, 70, 57, 'second degré', 'varie', 's', ha='left')
arrow(ax, (44, 32), (44, 22), 'resultat')
box(ax, 22, 12, 44, 10, 'resultat', True, r'$x=3$ ou $x=7$', 'l')
save(fig, '23-099')
