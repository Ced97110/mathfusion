import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 4, 44, 80, 10, 'sujet', label=r'$x-a=b$   donne   $x=b+a$')
for y, a, b, r in ((26, '8', '5', '5+8=13'), (6, '2', '-1', '-1+2=1')):
    box(ax, 2, y, 28, 10, 'fixe', label=r'$x-%s=%s$' % (a, b))
    arrow(ax, (31, y + 5), (45, y + 5), 'varie'); text(ax, 38, y + 9, r'$+\,%s$' % a, 'varie', 's')
    box(ax, 46, y, 40, 10, 'resultat', label=r'$x=%s$' % r)
save(fig, '16-064')
