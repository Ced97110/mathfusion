import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, 'restes par 7 : un corps', 'fixe', 's')
for i in range(7):
    box(ax, 3.1 + i * 11.9, 44, 10.4, 10, 'sujet' if i == 0 else 'resultat' if i == 1 else 'fixe', label=r'$\bar{%d}$' % i)
text(ax, 14.25, 38, r'$\bar0\neq\bar1$', 'resultat')
text(ax, 44, 30.5, r'donc $1\notin(7)$, $(7)\neq\mathbb{Z}$', 'resultat', 's')
text(ax, 44, 22, r'si $1\in(7)$ : une seule classe', 'limite', 's')
box(ax, 30, 6, 28, 10, 'limite', label=r'$\bar1=\bar0$')
save(fig, '52-118')
