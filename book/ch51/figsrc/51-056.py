import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def row(y, mid_lab, mid_role, op, end, cap):
    box(ax, 6, y, 16, 11, 'fixe', label='2', size='l')
    text(ax, 29, y + 5.5, op, 'encre', 'l')
    box(ax, 36, y, 20, 11, mid_role, label=mid_lab, size='l')
    text(ax, 63, y + 5.5, '=', 'encre', 'l')
    box(ax, 69, y, 14, 11, 'fixe', label=end, size='l')
    text(ax, 44, y - 5, cap, mid_role, 's')
row(44, r'$-2$', 'autre', '+', '0', "l'opposé défait l'addition")
row(14, r'$\frac{1}{2}$', 'sujet', r'$\times$', '1', "l'inverse défait la multiplication")
text(ax, 44, 61, r"l'inverse $a^{-1}$ et son voisin l'opposé", 'sujet', 'm')
save(fig, '51-056')
