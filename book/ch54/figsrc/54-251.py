import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
p = lambda v: v ** 4 - 2 * v ** 3 + v + 1
assert (p(1), p(-1)) == (1, 3)
box(ax, 4, 58, 80, 12, 'sujet', size='l', label=r'$p(x)=x^4-2x^3+x+1$')
text(ax, 44, 51, 'racines possibles : 1 et −1', 'fixe', 's')
box(ax, 4, 34, 38, 10, 'fixe', label=r'$p(1)=1\neq0$')
box(ax, 46, 34, 38, 10, 'fixe', label=r'$p(-1)=3\neq0$')
text(ax, 44, 27, 'aucune racine, mais ce n’est pas fini', 'varie', 's')
box(ax, 8, 6, 24, 10, 'varie', dash=True, label=r'$x^2+\cdots$')
text(ax, 38, 11, r'$\times$', 'encre', 'm')
box(ax, 44, 6, 24, 10, 'varie', dash=True, label=r'$x^2+\cdots$')
text(ax, 78, 11, '2 + 2 ?', 'varie', 's')
save(fig, '54-251')
