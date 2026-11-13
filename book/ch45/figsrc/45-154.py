import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def couple(x, a, b):
    box(ax, x, 22, 13, 13, 'sujet', label=str(a), size='l'); box(ax, x + 14, 22, 13, 13, 'autre', label=str(b), size='l')
    text(ax, x + 13.5, 14, f'({a}, {b})', 'encre', 'm')
couple(6, 0, 1); couple(55, 1, 0)
text(ax, 12.5, 41, r'$g$', 'sujet', 'm'); text(ax, 26.5, 41, r'$h$', 'autre', 'm')
text(ax, 61.5, 41, r'$g$', 'sujet', 'm'); text(ax, 75.5, 41, r'$h$', 'autre', 'm')
text(ax, 44, 28.5, r'$\neq$', 'limite', 'xl')
text(ax, 44, 5, "l'ordre des cases compte", 'limite', 's')
save(fig, '45-154')
