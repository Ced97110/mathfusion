import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def chain(y, k, role, mid, op1, op2, res, formula):
    box(ax, 3, y, 21, 9, 'sujet', label=k, size='s')
    box(ax, 38, y, 18, 9, 'fixe', label=mid, size='m')
    box(ax, 68, y, 17, 9, 'resultat', label=res, size='m')
    arrow(ax, (24, y + 4.5), (38, y + 4.5), 'varie'); text(ax, 31, y + 8, op1, 'varie', 's')
    arrow(ax, (56, y + 4.5), (68, y + 4.5), 'varie'); text(ax, 62, y + 8, op2, 'varie', 's')
    text(ax, 44, y - 4, formula, 'encre', 'm')
chain(42, r'$k$ = 6 pair', 'x', '3', r'$\div$ 2', 'opposé', r'$-3$', r'$-k/2$')
chain(12, r'$k$ = 7 impair', 'x', '8', '+ 1', r'$\div$ 2', '4', r'$(k+1)/2$')
save(fig, '43-132')
