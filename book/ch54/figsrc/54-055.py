import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def row(y, mid, op, label):
    box(ax, 2, y, 22, 14, 'sujet', label=r'$\frac{3}{5}$', size='l')
    text(ax, 30, y + 7, op, 'encre', 'l')
    box(ax, 36, y, 22, 14, 'fixe', label=mid, size='l')
    text(ax, 64, y + 7, '=', 'encre', 'l')
    box(ax, 70, y, 16, 14, 'resultat', label=r'$\frac{3}{5}$', size='l')
    text(ax, 44, y - 4, label, 'fixe', 's')
row(48, r'$\frac{0}{1}$', '+', r'$0\times5+1\times3=3$ ; $1\times5=5$')
row(16, r'$\frac{1}{1}$', r'$\times$', r'$1\times3=3$ ; $1\times5=5$')
text(ax, 44, 68, 'ne change rien : zéro', 'fixe', 's')
text(ax, 44, 36, 'ne change rien : un', 'fixe', 's')
save(fig, '54-055')
