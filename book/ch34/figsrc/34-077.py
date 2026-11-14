import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 15, 58, 'fonction', 'sujet', 's'); text(ax, 57, 58, 'signe du milieu', 'varie', 's')
def row(y, lhs, t1, sign, t2):
    box(ax, 2, y - 5, 26, 10, 'sujet', True, label=lhs, size='s')
    box(ax, 31, y - 5, 24, 10, 'fixe', True, label=t1, size='s')
    text(ax, 60, y, sign, 'varie', 'l', weight='bold')
    box(ax, 65, y - 5, 21, 10, 'fixe', True, label=t2, size='s')
row(46, r'$\sin(A-B)=$', r'$\sin A\cos B$', r'$-$', r'$\cos A\sin B$')
row(18, r'$\cos(A-B)=$', r'$\cos A\cos B$', r'$+$', r'$\sin A\sin B$')
text(ax, 60, 36, r'comme dans $A-B$', 'varie', 's')
text(ax, 60, 8, 'opposé de −', 'varie', 's')
save(fig, '34-077')
