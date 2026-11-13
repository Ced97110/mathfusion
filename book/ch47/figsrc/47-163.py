import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, r'$(1\ 2)\,N$ et $N\,(1\ 2)$', 'encre', 'm')
labs = ['(1 2)', '(1 3)', '(2 3)']
for y, name in ((30, r'$(1\ 2)\,N$'), (10, r'$N\,(1\ 2)$')):
    text(ax, 11, y + 5, name, 'resultat', 's')
    for i, l in enumerate(labs):
        box(ax, 24 + i * 19, y, 17, 10, 'resultat', label=l, size='s')
text(ax, 44, 25, r'$=$', 'resultat', 'xl')
text(ax, 44, 3.5, 'mêmes éléments : $N$ est normal', 'resultat', 's')
save(fig, '47-163')
