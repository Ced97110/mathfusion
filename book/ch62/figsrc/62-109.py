import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# F2: (x^2)' = 2x and 2 = 0
box(ax, 6, 46, 24, 12, 'sujet', label=r'$x^2$', size='l')
arrow(ax, (31, 52), (55, 52), 'varie'); text(ax, 43, 57, 'dériver', 'varie', 's')
box(ax, 56, 46, 26, 12, 'varie', label=r'$2\,x$', size='l')
# the two elements of F2 on a loop: 1 + 1 comes back to 0
disc(ax, 28, 30, 4.5, 'fixe', label='0'); disc(ax, 60, 30, 4.5, 'fixe', label='1')
arrow(ax, (56, 33.5), (32, 33.5), 'varie', curve=0.5); text(ax, 44, 41, r'$+1$', 'varie', 's')
arrow(ax, (32, 26.5), (56, 26.5), 'varie', curve=0.5); text(ax, 44, 18.5, r'$+1$', 'varie', 's')
text(ax, 44, 30, r'$1+1=0$', 'encre', 's')
box(ax, 8, 4, 72, 11, 'resultat', label=r'$(x^2)^{\prime}=0$, mais $x^2$ n’est pas constant', size='s')
save(fig, '62-109')
