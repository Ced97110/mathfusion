import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def mat(x0, y0, v, name):
    text(ax, x0 + 10.5, y0 + 26, name, 'encre', 'l')
    for k in range(4):
        r, c = divmod(k, 2)
        box(ax, x0 + c * 11, y0 + (1 - r) * 11, 10, 10, 'sujet' if r == c else 'varie', label=str(v[k]), size='l')
mat(8, 22, [1, 2, 5, 6], r'$A$')
mat(56, 22, [1, 5, 2, 6], r'$A^T$')
arrow(ax, (33, 33), (53, 33), 'varie')
text(ax, 43, 37, 'transposer', 'varie', 's')
text(ax, 19, 14, r'$1\times6-2\times5=-4$', 'resultat', 's')
text(ax, 67, 14, r'$1\times6-5\times2=-4$', 'resultat', 's')
text(ax, 43, 6, 'même déterminant', 'resultat', 's')
save(fig, '52-291')
