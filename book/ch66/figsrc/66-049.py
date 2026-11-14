import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
def col(x, role, head, div, quo, note):
    text(ax, x + 18, 73, head, role, 's')
    box(ax, x, 56, 36, 10, 'fixe', label=r'$x^2-1$')
    arrow(ax, (x + 18, 56), (x + 18, 50), role)
    box(ax, x, 40, 36, 10, 'varie', label=div)
    arrow(ax, (x + 18, 40), (x + 18, 34), role)
    box(ax, x, 22, 36, 12, role, label=quo)
    text(ax, x + 18, 14, note, role, 's')
col(3, 'resultat', 'diviseur unitaire', r'$\div\ (x-1)$', r'$x+1$', 'coefficients 1 et 1 : entiers')
col(49, 'limite', 'diviseur non unitaire', r'$\div\ (2x-2)$', r'$\frac{x}{2}+\frac{1}{2}$', r'coefficients $\frac{1}{2}$ : pas entiers')
save(fig, '66-049')
