import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 35.0
text(ax, 44, 46, r'$1{,}414\times 1{,}414$', 'varie', 'l')
arrow(ax, (44, 42), (44, 37.5), 'varie')
box(ax, 8, 28, 2 * u, 8, 'resultat', label='2')
box(ax, 8, 16, 1.999396 * u, 8, 'varie', label='1,999396')
text(ax, 44, 8, r'proche de 2, mais $\neq 2$', 'limite', 'm')
save(fig, '22-020')
