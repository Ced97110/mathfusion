import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 20, 60, r'$n=2$ : 2 termes', 'sujet', 'm')
text(ax, 65, 60, r'$n=3$ : 6 termes', 'sujet', 'm')
for i, p in enumerate(['1 2', '2 1']):
    box(ax, 7, 44 - 11 * i, 26, 8, 'sujet', label=p)
P3 = ['1 2 3', '1 3 2', '2 1 3', '2 3 1', '3 1 2', '3 2 1']
for i, p in enumerate(P3):
    box(ax, 44 + 22 * (i % 2), 44 - 11 * (i // 2), 19, 8, 'sujet', label=p)
box(ax, 4, 5, 80, 11, 'resultat', label=r'$n\,! = n\times(n-1)\times\cdots\times1$')
save(fig, '76-098')
