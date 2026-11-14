import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$x=1$ : première ligne $1,\ 0,\ -3$', 'encre', 'm')
labs = [r'$1\times(1\times1-0\times1)=1$', r'$0\times\ldots=0$', r'$-3\times1=-3$']
for i, lab in enumerate(labs):
    y = 46 - i * 14
    box(ax, 2, y, 52, 10, 'sujet', label=lab, size='s')
    arrow(ax, (54.5, y + 5), (65.5, 30), 'varie')
text(ax, 76, 42, r'$1+0-3$', 'varie', 's')
box(ax, 66, 24, 20, 12, 'resultat', label=r'$-2$', size='l')
text(ax, 44, 6, r'$x^2(x^2-3)$ en $x=1$ : $-2$', 'resultat', 's')
save(fig, '70-080')
