import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'applications de $F$ dans $F$ : $2^2 = 4$', 'sujet', 'm')
for i, v in enumerate(['(0, 0)', '(0, 1)', '(1, 0)', '(1, 1)']):
    box(ax, 12 + i * 17, 46, 13, 10, 'sujet', label=v, size='s')
text(ax, 44, 41, r'sorties $(f(0),\ f(1))$', 'sujet', 's')
text(ax, 44, 32, 'fini contre infini : pas de bijection', 'limite', 's')
for i, v in enumerate(['1', r'$x$', r'$x^2$', r'$x^3$', r'$\cdots$']):
    box(ax, 10 + i * 14, 12, 11, 10, 'autre', label=v, size='s')
text(ax, 44, 6, r'$F[x]$ : infini', 'autre', 's')
save(fig, '55-044')
