import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 18, 50, r'$[E,G]$', 'sujet', 'm'); text(ax, 70, 50, r'$[G,E]$', 'autre', 'm')
a = [['1', '0'], ['0', '-1']]; b = [['-1', '0'], ['0', '1']]
f = lambda s: s.replace('-', r'$-$') if s.startswith('-') else s
for r_ in range(2):
    for c_ in range(2):
        box(ax, 6 + c_ * 14, 14 + (1 - r_) * 14, 14, 14, 'sujet', label=r'$%s$' % a[r_][c_])
        box(ax, 58 + c_ * 14, 14 + (1 - r_) * 14, 14, 14, 'autre', label=r'$%s$' % b[r_][c_])
arrow(ax, (36, 28), (56, 28), 'varie', both=True)
text(ax, 46, 33, 'opposées', 'varie', 's')
text(ax, 44, 6, r'$[x,y] = -[y,x]$', 'resultat', 'm')
save(fig, '78-044')
