import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
def cas(x, h, a, b, s):
    text(ax, x + 20, 68, h, 'sujet', 's', weight='bold')
    box(ax, x, 48, 19, 10, 'sujet', label=a, size='s'); text(ax, x + 20, 53, '+', 'encre', 'm')
    box(ax, x + 21, 48, 19, 10, 'autre', label=b, size='s')
    arrow(ax, (x + 20, 47), (x + 20, 37), 'varie')
    box(ax, x + 6, 26, 28, 10, 'resultat', label=s, size='m')
cas(2, r'$z=1+i,\ w=1$', r'$(1+i)^2=2i$', r'$1^2=1$', r'$1+2i$')
cas(46, r'$z=3,\ w=4$', r'$3^2=9$', r'$4^2=16$', r'$25$')
text(ax, 44, 16, r'$N(z+wj)=z^2+w^2$', 'encre', 'l')
text(ax, 44, 7, r'$z$ et $w$ complexes : $N$ peut être complexe', 'encre', 's')
save(fig, '77-132')
