import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
box(ax, 4, 30, 18, 8, 'varie', label='2    5', size='m', r=0.5); box(ax, 4, 22, 18, 8, 'fixe', label='1    3', size='m', r=0.5)
for x, y, s, r in [(28, 30, '3', 'varie'), (38, 30, '−5', 'fixe'), (28, 22, '−1', 'varie'), (38, 22, '2', 'fixe')]:
    box(ax, x, y, 10, 8, r, label=s, size='m', r=0.5)
box(ax, 56, 30, 18, 8, 'resultat', label='1    0', size='m', r=0.5); box(ax, 56, 22, 18, 8, 'fixe', label='0    1', size='m', r=0.5)
text(ax, 25, 34, r'$\times$', 'encre', 'l'); text(ax, 52, 34, '=', 'encre', 'l')
text(ax, 13, 17, r'$P$', 'sujet', 'm'); text(ax, 33, 17, r'$P^{-1}$', 'autre', 'm'); text(ax, 65, 17, r'$I$', 'resultat', 'm')
text(ax, 44, 8, r'$2 \times 3 + 5 \times (-1) = 1$', 'resultat', 'm')
save(fig, '43-044')
