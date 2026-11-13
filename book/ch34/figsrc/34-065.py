import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def row(y, lhs, sign):
    text(ax, 14, y, lhs, 'encre', 'm')
    box(ax, 28, y - 5, 24, 10, 'fixe', True, label=r'$\sin A\,\cos B$')
    text(ax, 57, y, sign, 'varie', 'l', weight='bold')
    box(ax, 62, y - 5, 24, 10, 'varie', True, label=r'$\cos A\,\sin B$')
row(42, r'$\sin(A+B)=$', '+')
row(14, r'$\sin(A-B)=$', r'$-$')
arrow(ax, (74, 36.5), (74, 19.5), 'varie')
text(ax, 46, 28, r'$\sin B\ \rightarrow\ -\sin B$', 'varie', 's')
text(ax, 40, 5.5, 'inchangé', 'fixe', 's')
text(ax, 74, 5.5, 'change de signe', 'varie', 's')
save(fig, '34-065')
