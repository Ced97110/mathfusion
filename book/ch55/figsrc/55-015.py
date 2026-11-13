import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 67, 'trois listes différentes', 'sujet', 's')
items = [(50, r'$x^3-x$' + '\n' + r'$0,-1,0,1$'), (28, r'$0$' + '\n' + r'$0,0,0,0$'), (6, r'$2x^3-2x$' + '\n' + r'$0,-2,0,2$')]
for y, lab in items:
    box(ax, 4, y, 36, 14, 'sujet', label=lab, size='s')
    arrow(ax, (40, y + 7), (56, 31), 'varie')
box(ax, 56, 24, 28, 14, 'autre', label='tableau\n' + r'$0,0,0$', size='s')
text(ax, 70, 17, 'un seul tableau', 'autre', 's')
save(fig, '55-015')
