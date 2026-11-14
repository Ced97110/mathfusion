import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'entiers rangés par position', 'encre', 'm')
xs = [8 + i * 6.5 for i in range(12)]
for i, x in enumerate(xs):
    box(ax, x - 2.9, 17, 5.8, 38, 'sujet', r=0.6, lw=0.7)
    for k in range(3): disc(ax, x, 50 - k * 8, 1.5, 'varie')
    for k in range(2): disc(ax, x, 27.5 - k * 3.2, 0.6, 'fixe')
    text(ax, x, 12, r'$\bar{%d}$' % i, 'sujet', 's')
brace(ax, xs[0] - 2.9, xs[-1] + 2.9, 7.5, 'resultat', label='ensemble quotient : 12 éléments', depth=1.8)
save(fig, '43-075')
